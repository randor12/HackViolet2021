import mysql.connector


class Connector():
    def __init__(self):
        """
        Initialize Database Connection and Queries
        """
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="username",
            password="password"

        )

    def connect(self):
        """
        Connect to the DB
        """
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="username",
            password="password"

        )

    def add_account(self, schema, table, values):
        """
        Add accounts
        :param schema: database name
        :param table: table name
        :param values: string of values added to the database
        :return: True if successfully added, else False
        """
        try:
            cursor = self.mydb.cursor()
            query = 'INSERT INTO %s.%s VALUES(%s);' % (schema, table, values)
            cursor.execute(query)
            self.mydb.commit()
            return True
        except Exception as e:
            print(e.message)
            return False
