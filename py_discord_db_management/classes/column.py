
class Column:
    def __init__(self, field, type, null, key, default, extra):
        self.__field = field
        self.__type = type
        self.__null = null
        self.__key = key
        self.__default = default
        self.__extra = extra

        # variable that is used to attach values to that specific column
        self.__attached_data = None
        self.__hidden = False

    def get_hidden(self):
        return self.__hidden

    def set_hidden(self, new_visibility):
        self.__hidden = new_visibility

    def set_attached_data(self, attached_data):
        # value is empty
        if not attached_data:
            self.__attached_data = self.__default
        else:
            self.__attached_data = attached_data

    def set_default(self, new_default):
        self.__default = new_default

    def get_attached_data(self):
        return self.__attached_data

    def get_field(self):
        return self.__field

    def get_type(self):
        return self.__type

    def get_nullable(self):
        # allow to force a custom primary key
        if self.__extra == 'auto_increment':
            return True

        if self.__null == 'YES':
            return True

        if self.__null == 'NO':
            if self.__default or self.__default == 0:
                return True
            return False

    def get_key(self):
        return self.__key

    def get_default(self):
        return self.__default

    def get_extra(self):
        return self.__extra