
class Column:
    def __init__(self, field, type, null, key, default, extra):
        self.field = field
        self.type = type
        self.null = null
        self.key = key
        self.default = default
        self.extra = extra