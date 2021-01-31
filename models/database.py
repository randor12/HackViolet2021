import mysql.connector
import os
import bcrypt
from dotenv import load_dotenv
from .loginInfo import LoginInfo
from .msgInfo import MsgInfo

env_path = ".env"
load_dotenv(env_path)


class Connector():
    def __init__(self):
        """
        Initialize Database Connection and Queries
        """
        self.default_schema = 'hack_violet_2021'
        # ADD MYSQL DATABASE INFORMATION TO `.env` file
        self.user = os.getenv('USER_DATABASE')

        self.passVal = os.getenv('PASS_DATABASE')

        self.mydb = None

    def connect(self):
        """
        Connect to the DB
        """
        self.mydb = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.passVal

        )

    def destroy(self):
        self.mydb.close()

    def add_account(self, values):
        """
        Add accounts
        :param schema: database name
        :param table: table name
        :param values: string of values added to the database
        :return: True if successfully added, else False
        """
        try:
            idVal = self.get_recent_acct_id()
            self.connect()
            values = str(idVal) + ', ' + values
            schema = self.default_schema
            table = 'accounts'
            query = 'INSERT INTO %s.%s VALUES(%s);' % (schema, table, values)
            print(query)
            cursor = self.mydb.cursor()
            cursor.execute(query)
            self.mydb.commit()
            cursor.close()
            self.destroy()
            return True
        except Exception as e:
            print(str(e))
            return False

    def remove_account(self, email):
        """
        Remove from accounts

        :param email: email to be removed
        :type email: str
        """
        try:
            self.connect()
            table = 'accounts'
            schema = self.default_schema
            query = "DELETE FROM %s.%s WHERE email like '%s';" % (
                schema, table, email)
            print(query)
            cursor = self.mydb.cursor()
            cursor.execute(query)
            self.mydb.commit()
            cursor.close()
            self.destroy()
            return True
        except Exception as e:
            print(str(e))
            return False

    def get_recent_acct_id(self):
        try:
            self.connect()
            cursor = self.mydb.cursor()
            query = "SELECT id FROM hack_violet_2021.accounts order by id DESC limit 1;"
            cursor.execute(query)
            loginInfo = cursor.fetchall()
            print(loginInfo if loginInfo is not None else "null")
            id = 0
            if loginInfo is not None:

                for i in loginInfo:
                    print(i)
                    id = i[0]

            self.destroy()
            return id + 1
        except Exception as e:
            print(e.message)
            return 1

    def select_account(self, email):
        """
        Get information on the login info by email

        :param email: email to search by
        :type email: string
        :return: Returns the login info
        """
        try:
            self.connect()
            cursor = self.mydb.cursor()
            query = "SELECT * FROM hack_violet_2021.accounts WHERE email LIKE '%s';" % email
            cursor.execute(query)
            loginInfo = cursor.fetchall()
            print(loginInfo)
            m = LoginInfo()
            for i in loginInfo:
                # login info

                print(i)
                m.set_id(i[0])
                m.set_email(i[1])
                m.set_user(i[2])
                m.set_pass(i[3])
                m.set_salt(i[4])
                m.set_fname(i[5])
                m.set_lname(i[6])

            cursor.close()
            self.destroy()
            return m
        except Exception as e:
            print(e)
            return None

    def select_msg(self, id, feed):
        """
        Select corresponding messages

        :param id: id number corresponding to messages related to users
        :type id: int
        :param feed: boolean value (0 or 1) on if message is from feed or DM
        :type feed: int
        """
        try:
            self.connect()
            query = "SELECT * FROM hack_violet_2021.msgs WHERE (sentID = %d or sentID = %d) and feed = %d;" % (
                id, id, feed)
            cursor = self.mydb.cursor()
            loginInfo = cursor.execute(query).fetchall()

            cursor.close()
            self.destroy()
            return loginInfo
        except Exception as e:
            print(e.message)
            return None

    def get_feed_msgs(self) -> list:
        """
        Get the feed messages
        """
        try:
            self.connect()
            query = "SELECT * FROM hack_violet_2021.msgs WHERE feed = 1;"
            cursor = self.mydb.cursor()
            loginInfo = cursor.execute(query).fetchall()

            allMsgs = []

            for m in loginInfo:
                # login info
                msgData = MsgInfo()
                msgData.set_mID(m[0])
                msgData.set_aID(m[1])
                msgData.set_message(m[2])
                msgData.set_feed(m[3])
                msgData.set_sentID(m[4])

                allMsgs.append(msgData)

            cursor.close()
            self.destroy()
            return allMsgs
        except Exception as e:
            print(e.message)
            return None

    def get_recent_msg_id(self):
        try:
            self.connect()
            cursor = self.mydb.cursor()
            query = "SELECT mID FROM hack_violet_2021.msgs order by mID DESC limit 1;"
            loginInfo = cursor.execute(query).fetchall()
            id = 1
            if loginInfo is None:
                return 1

            for i in loginInfo:
                id = i

            cursor.close()
            self.destroy()
            return id + 1
        except Exception as e:
            print(e.message)
            return None

    def add_msg(self, uID, msg, feed, sentID):
        """
        Add a message to the feed

        :param uID: user ID of the sender
        :type uID: int
        :param msg: message sent by the user
        :type msg: str
        :param feed: 0 if sent through DM else 1
        :type feed: int
        :param sentID: ID Number the message was sent to, else -1 if no user
        :type sentID: id
        """
        try:
            idVal = self.get_recent_msg_id()
            self.connect()
            cursor = self.mydb.cursor()
            table = 'msgs'
            values = str(idVal) + ", " str(uID) + ", '" + msg + "', " + \
                str(feed) + ", " + str(sentID)
            query = 'INSERT INTO %s.%s VALUES(%s);' % (
                self.default_schema, table, values)
            cursor.execute(query)
            self.mydb.commit()
            cursor.close()
            self.destroy()
            return True
        except Exception as e:
            print(str(e))
            return False

    def remove_msg(self, mID):
        """
        Remove of message
        :param mID: message ID
        :return: returns True if successfully removed, else false
        """
        try:
            self.connect()
            cursor = self.mydb.cursor()
            table = 'msgs'
            query = 'DELETE FROM %s.%s WHERE mID = %d;' % (
                self.default_schema, table, int(mID))
            cursor.execute(query)
            self.mydb.commit()
            cursor.close()
            self.destroy()
            return True
        except Exception as e:
            print(str(e))
            return False

    def subscribe(self, uID, oID):
        """
        Subscribe to other users to see their messages

        : param uID: user id that is following someone
        : type uID: int
        : param oID: user being followed
        : type oID: int
        """
        try:
            self.connect()
            cursor = self.mydb.cursor()
            table = 'subscribe'
            idVal = self.most_recent_sub()
            values = str(idVal) + ", " + str(uID) + ", " + str(oID)
            query = 'INSERT INTO %s.%s VALUES(%s);' % (
                self.default_schema, table, values)
            cursor.execute(query)
            self.mydb.commit()
            cursor.close()
            self.destroy()
            return True
        except Exception as e:
            print(e.message)
            return False

    def most_recent_sub(self):
        try:
            cursor = self.mydb.cursor()
            query = "SELECT sID FROM hack_violet_2021.subscribe order by sID DESC limit 1;"
            loginInfo = cursor.execute(query)
            id = 1
            for i in loginInfo:
                id = i
            cursor.close()
            return id
        except Exception as e:
            print(e.message)
            return None

    def unsubscribe(self, uID, oID):
        """
        Unsubscribe from the person's feed

        : param uID: user unfollowing someone
        : type uID: int
        : param oID: person being unfollowed
        : type oID: int
        """
        try:
            cursor = self.mydb.cursor()
            query = "DELETE FROM hack_violet_2021.subscribe WHERE fllwID = %d;" % uID
            loginInfo = cursor.execute(query)
            id = 1
            for i in loginInfo:
                id = i
            cursor.close()
            return id
        except Exception as e:
            print(e.message)
            return None


def saltHash(password: str):
    """Hash a password for storing."""
    salt = bcrypt.gensalt()
    hashVal = bcrypt.hashpw(password, salt)
    return hashVal, salt
