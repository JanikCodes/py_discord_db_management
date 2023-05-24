from py_discord_db_management.classes.column import Column


class Table:
    def __init__(self, database, table_name):
        self.__table_name = table_name
        self.__columns = self.get_columns_from_table(database, table_name)

    def get_table_name(self):
        return self.__table_name

    def get_columns(self):
        return self.__columns

    def get_columns_from_table(self, database, table_name):
        columns = []

        sql = f"DESCRIBE {table_name};"
        database.cursor.execute(sql)
        res = database.cursor.fetchall()
        if res:
            for row in res:
                columns.append(Column(field=row[0], type=row[1], null=row[2], key=row[3], default=row[4], extra=row[5]))

        return columns