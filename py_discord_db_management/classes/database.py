import mysql.connector
import warnings

from py_discord_db_management.classes.table import Table


class Database:
    def __init__(self, host, user, password, port, database_name, charset):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database_name = database_name
        self.charset = charset

        self.mydb = self.__init_database()
        self.cursor = self.mydb.cursor(buffered=True)

        self.tables = self.__get_all_tables()

    def __init_database(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port,
            database=self.database_name,
            charset=self.charset
        )
    def __get_all_tables(self):
        tables = []

        sql = f"SHOW TABLES;"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        if res:
            for row in res:
                tables.append(Table(self, row[0]))

        return tables

    def set_table_hidden(self, table_name):
        for table in self.tables:
            if table.get_table_name().lower() == table_name.lower():
                # we found the table
                table.set_hidden(True)
                return

        warnings.warn(f"Couldn't find table with name: {table_name}")
    def set_column_default_value(self, table_name, column_name, value):
        for table in self.tables:
            if table.get_table_name().lower() == table_name.lower():
                # we found the table
                for column in table.get_columns():
                    if column.get_field().lower() == column_name.lower():
                        # we found the column
                        column.set_default(value)
                        return

                warnings.warn(f"Couldn't find column with name: {column_name}")
        warnings.warn(f"Couldn't find table with name: {table_name}")
    def get_is_connected(self):
        return self.mydb.is_connected()

    def add_data_to_table(self, table, columns):
        val_str = ', '.join(['%s'] * len(columns))

        sql = f'INSERT INTO {table.get_table_name()} VALUES({val_str});'

        column_data = [column.get_attached_data() for column in columns]
        self.cursor.execute(sql, column_data)
        self.mydb.commit()

    def get_charset(self):
        return self.charset