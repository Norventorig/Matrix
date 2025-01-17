class MatrixElem:
    def __init__(self, string_index: int, table_index: int) -> None:
        self._value = None
        self._string_index = string_index
        self._table_index = table_index

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value: int) -> None:
        self._value = new_value

    @property
    def string_index(self):
        return self._string_index

    @property
    def table_index(self):
        return self._table_index
