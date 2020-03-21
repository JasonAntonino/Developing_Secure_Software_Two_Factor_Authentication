import os
import sqlite3
import csv
from static.database.tables import csvparam as csvparameter

# account table details:
# USERID        : user id
# USERUSERNAME  : username
# USERFULLNAME  : full name
# USEREMAIL     : email
# USERSEQUENCE  : sequence (password)
# USERIMAGE     : image used id

CONTENT_PATH = './static/database/content/'
CSV_USER = 'account.csv'
ACCOUNT_FULLPATH = CONTENT_PATH + CSV_USER

SCRIPT_CREATE = 'CREATE TABLE ACCOUNT (USERID integer PRIMARY KEY'
SCRIPT_CREATE += ', USERUSERNAME VARCHAR(32)'
SCRIPT_CREATE += ', USERFULLNAME TEXT'
SCRIPT_CREATE += ', USEREMAIL VARCHAR(32)'
SCRIPT_CREATE += ', USERSEQUENCE VARCHAR(100)'
SCRIPT_CREATE += ', USERIMAGE VARCHAR(1)'
SCRIPT_CREATE += ')'

def account_init(db):
    # Creates the table
    account_create(db)

    with open(ACCOUNT_FULLPATH) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=csvparameter.CSV_DELIMITER, quotechar=csvparameter.CSV_QUOTE, quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)
        id = 0
        for row in csv_reader:
            if len(row) == 5:
                id += 1
                account_insert(db, id, row[0], row[1], row[2], row[3], row[4])

def account_create(db):
    c = db.cursor()
    c.execute(SCRIPT_CREATE)
    db.commit()

def account_insert(db,id,username,fullname,email,sequence,imageid):
    c = db.cursor()
    c.execute('INSERT INTO ACCOUNT (USERID, USERUSERNAME, USERFULLNAME, USEREMAIL, USERSEQUENCE, USERIMAGE) VALUES (?,?,?,?,?,?)', (id,username,fullname,email,sequence,imageid))
    db.commit()

def account_newAccount(db,id,username,fullname,email,sequence,imageid):
    with open(ACCOUNT_FULLPATH, 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=csvparameter.CSV_DELIMITER, quotechar=csvparameter.CSV_QUOTE, quoting=csv.QUOTE_MINIMAL)
        writer.writerows([[username,fullname,email,sequence,imageid]])
    id = account_generateid(db)
    account_insert(db,id,username,fullname,email,sequence,imageid)

def account_generateid(db):
    c = db.cursor()
    c.execute('SELECT MAX(USERID)+1 FROM ACCOUNT')
    return c.fetchall()[0][0]

def account_usernameexists(db, username):
    c = db.cursor()
    c.execute('SELECT 1 FROM ACCOUNT WHERE USERUSERNAME = (?)', (username,))
    return len(c.fetchall()) > 0

def account_getUserIdByUsername(db, username):
    c = db.cursor()
    c.execute('SELECT USERID FROM ACCOUNT WHERE USERUSERNAME = (?)', (username,))
    userId = c.fetchall()[0][0]
    return userId

def account_getSequenceByUserId(db, userId):
    c = db.cursor()
    c.execute('SELECT USERSEQUENCE FROM ACCOUNT WHERE USERID = (?)', (userId,))
    sequence = c.fetchall()[0][0]
    return sequence

def account_getImageIdByUserId(db, userId):
    c = db.cursor()
    c.execute('SELECT USERIMAGE FROM ACCOUNT WHERE USERID = (?)', (userId,))
    imageid = c.fetchall()[0][0]
    return imageid

def account_getEmailByUserId(db, userId):
    c = db.cursor()
    c.execute('SELECT USEREMAIL FROM ACCOUNT WHERE USERID = (?)', (userId,))
    email = c.fetchall()[0][0]
    return email