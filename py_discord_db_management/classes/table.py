from py_discord_db_management.classes.column import Column


class Table:
    def __init__(self, database, table_name):
        self.__table_name = table_name
        self.__columns = self.get_columns_from_table(database, table_name)

        self.__hidden = False

    def set_hidden(self, new_visibility):
        self.__hidden = new_visibility

    def get_hidden(self):
        return self.__hidden

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
                default_val_string = None if not row[4] else row[4].decode('utf-8')
                columns.append(Column(field=row[0], type=row[1], null=row[2], key=row[3], default=default_val_string, extra=row[5]))

        return columns