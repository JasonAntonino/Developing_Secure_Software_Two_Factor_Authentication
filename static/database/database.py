import os
import sqlite3
from static.database.tables import account as user
from static.database.tables import otp as otptable
DATABASE = 'dbmain'

class Database:

    def __init__(self):
        self.delete_db()
        self.db = sqlite3.connect(DATABASE, check_same_thread=False)
        c = self.db.cursor()
        self.init_tables()

    def init_tables(self):
        user.account_init(self.db)
        otptable.otp_init(self.db)

    def delete_db(self):
        if os.path.exists(DATABASE):
            os.remove(DATABASE)

    # Creates a new account
    def addNewAccount(self, username, fullname, email, sequence, imageid):
        userid = user.account_generateid(self.db)
        user.account_newAccount(self.db, userid, username, fullname, email, sequence, imageid)

    def userExistsCheck(self, username):
        return user.account_usernameexists(self.db, username)

    def loginValidation(self, username, sequence, imageid):
        userExists = user.account_usernameexists(self.db, username)

        if userExists:
            userId = user.account_getUserIdByUsername(self.db, username)
            dbSequence = user.account_getSequenceByUserId(self.db, userId)
            dbImageId = user.account_getImageIdByUserId(self.db, userId)

            if dbSequence == sequence and dbImageId == imageid:
                return 1
            else:
                return 0
        else:
            return 0

    def getUserIdByUsername(self, username):
        return user.account_getUserIdByUsername(self.db, username)

    def getEmailByUserId(self, userid):
        return user.account_getEmailByUserId(self.db, userid)

    def addNewOtp(self, username, otp, timestamp):
        userid = otptable.otp_generateid(self.db)
        otptable.otp_newAccount(self.db, userid, username, otp, timestamp)

    def getUsernamesInOtp(self):
        return otptable.otp_getAllUsernames(self.db)
    
    def renewOtpOfUser(self, username, otp, timestamp):
        otptable.otp_updateOtpAndTimestampOfUsername(self.db, username, otp, timestamp)

    def getOtpByUserId(self, userId):
        return otptable.otp_getOtpByUserId(self.db, userId)

    def getTimestampByUserId(self, userId):
        return otptable.otp_getTimestampByUserId(self.db, userId)