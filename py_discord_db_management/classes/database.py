import mysql.connector

from py_discord_db_management.classes.table import Table


class Database:
    def __init__(self, host, user, password, port, database_name, charset):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database_name = database_name
        self.charset = charset

        self.mydb = self.init_database()
        self.cursor = self.mydb.cursor(buffered=True)

        self.tables = self.__get_all_tables()

    def init_database(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port,
            database=self.database_name,
            charset=self.charset
        )

    def get_is_connected(self):
        return self.mydb.is_connected()

    def __get_all_tables(self):
        tables = []

        sql = f"SHOW TABLES;"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        if res:
            for row in res:
                tables.append(Table(self, row[0]))

        return tables

    def add_data_to_table(self, table, tb_data):

        val_str = str()

        for index, data in enumerate(tb_data):
            if not index == len(tb_data):
                val_str += "%s, "
            else:
                # last element
                val_str += "%s"

        print(f'INSERT INTO {table.get_table_name()} VALUES({val_str});')

        sql = f'INSERT INTO {table.get_table_name()} VALUES({val_str});'
        self.cursor.execute(sql, tb_data)
        self.mydb.commit()
