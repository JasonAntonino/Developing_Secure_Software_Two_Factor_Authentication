import os
import sqlite3
from static.database.tables import account as user
DATABASE = 'dbmain'

class Database:

    def __init__(self):
        self.delete_db()
        self.db = sqlite3.connect(DATABASE, check_same_thread=False)
        c = self.db.cursor()
        self.init_tables()

    def init_tables(self):
        user.account_init(self.db)

    def delete_db(self):
        if os.path.exists(DATABASE):
            os.remove(DATABASE)

    # Creates a new account
    def addNewAccount(self, username, fullname, email, sequence):
        userid = user.account_generateid(self.db)
        user.account_newAccount(self.db, userid, username, fullname, email, sequence)

    def userExistsCheck(self, username):
        return user.account_usernameexists(self.db, username)

    def loginValidation(self, username, sequence):
        userExists = user.account_usernameexists(self.db, username)

        if userExists:
            userId = user.account_getUserIdByUsername(self.db, username)
            dbSequence = user.account_getSequenceByUserId(self.db, userId)

            if dbSequence == sequence:
                return 1
            else:
                return 0
        else:
            return 0

    def getUserIdByUsername(self, username):
        return user.account_getUserIdByUsername(self.db, username)