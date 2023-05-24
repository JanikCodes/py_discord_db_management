
class Column:
    def __init__(self, field, type, null, key, default, extra):
        self.__field = field
        self.__type = type
        self.__null = null
        self.__key = key
        self.__default = default
        self.__extra = extra

    def get_field(self):
        return self.__field

    def get_type(self):
        return self.__type

    def get_null(self):
        return self.__null

    def get_key(self):
        return self.__key

    def get_default(self):
        return self.__default

    def get_extra(self):
        return self.__extra