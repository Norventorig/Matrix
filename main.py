from abc import ABC


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


class Matrix:
    def __init__(self, strings_len: int, tables_len: int) -> None:
        self._m_max = strings_len
        self._n_max = tables_len

        self.determinator = None

        self._values = list()

        for m in range(1, self._m_max + 1):
            for n in range(1, self._n_max + 1):
                self._values.append(MatrixElem(string_index=m, table_index=n))

        self._values = tuple(self._values)

    def __str__(self):
        tables_counter = 0
        output = '\n'

        for i in self:
            tables_counter += 1

            if tables_counter > self.n_max:
                output += '\n'
                tables_counter = 1

            output += f'{i.value}\t'

        return output

    def __iter__(self):
        self.value_index = -1

        return self

    def __next__(self):
        if self.value_index + 1 > ((self.n_max * self.m_max) - 1):
            raise StopIteration

        self.value_index += 1

        return self.matrix[self.value_index]

    @property
    def matrix(self):
        return self._values

    @property
    def n_max(self):
        return self._n_max

    @property
    def m_max(self):
        return self._m_max

    @staticmethod
    def __operation(op_sign: str, first_matrix: object, another_matrix: object) -> object:
        if isinstance(another_matrix, Matrix) and isinstance(first_matrix, Matrix):
            if another_matrix.n_max == first_matrix.n_max and another_matrix.m_max == first_matrix.m_max:
                output_matrix = Matrix(strings_len=first_matrix.m_max, tables_len=first_matrix.n_max)

                matrix_1_values = [i.value for i in first_matrix]
                matrix_2_values = [i.value for i in another_matrix]

                if op_sign == "+":
                    gen = ((matrix_1_values[count] + matrix_2_values[count], i) for count, i in enumerate(output_matrix))

                elif op_sign == "-":
                    gen = ((matrix_1_values[count] - matrix_2_values[count], i) for count, i in enumerate(output_matrix))

                elif op_sign == "*":
                    gen = ((matrix_1_values[count] * matrix_2_values[count], i) for count, i in enumerate(output_matrix))

                elif op_sign == "/":
                    gen = ((matrix_1_values[count] / matrix_2_values[count], i) for count, i in enumerate(output_matrix))

                else:
                    raise Exception("\nНеправильный вызов функции!\n")

                for i in gen:
                    i[1].value = i[0]

                return output_matrix

            else:
                print("\nНевозможно сложение матриц разного разряда!\n")
                return None

        else:
            print("\nВ метод класса передан не экземпляр класса Matrix!\n")
            return None

    @classmethod
    def plus(cls, first_matrix: object, another_matrix: object) -> object:
        return cls.__operation(first_matrix=first_matrix, another_matrix=another_matrix, op_sign="+")

    @classmethod
    def minus(cls, first_matrix: object, another_matrix: object) -> object:
        return cls.__operation(first_matrix=first_matrix, another_matrix=another_matrix, op_sign="-")

    @classmethod
    def multiply(cls, first_matrix: object, another_matrix: object) -> object:
        return cls.__operation(first_matrix=first_matrix, another_matrix=another_matrix, op_sign="*")

    @classmethod
    def separate(cls, first_matrix: object, another_matrix: object) -> object:
        return cls.__operation(first_matrix=first_matrix, another_matrix=another_matrix, op_sign="/")


class FindDeterminator(ABC):
    @classmethod
    def find_determinator(cls, matrix: Matrix):
        if matrix.n_max != matrix.m_max:
            return None

        else:
            for i in (i.value for i in matrix.matrix):
                if i is None:
                    return None

            if matrix.n_max == 2:
                return matrix.matrix[0].value * matrix.matrix[3].value - matrix.matrix[1].value * matrix.matrix[2].value

            elif matrix.n_max >= 3:
                return cls.determinator_rec(matrix=matrix)

    @classmethod
    def determinator_rec(cls, matrix: Matrix):
        if matrix.n_max == 3:
            return (matrix.matrix[0].value * matrix.matrix[4].value * matrix.matrix[8].value +
                    matrix.matrix[3].value * matrix.matrix[7].value * matrix.matrix[2].value +
                    matrix.matrix[1].value * matrix.matrix[5].value * matrix.matrix[6].value -
                    matrix.matrix[2].value * matrix.matrix[4].value * matrix.matrix[6].value -
                    matrix.matrix[7].value * matrix.matrix[5].value * matrix.matrix[0].value -
                    matrix.matrix[3].value * matrix.matrix[1].value * matrix.matrix[8].value)

        else:
            determinator = 0

            for i in range(matrix.n_max):
                i_matrix_elem = matrix.matrix[i]

                side_matrix = Matrix(matrix.n_max - 1, matrix.m_max - 1)
                side_matrix_values = [j.value for j in matrix
                                      if
                                      j.table_index != i_matrix_elem.table_index
                                      and j.string_index != i_matrix_elem.string_index]

                generator = ((index, i_value) for index, i_value in enumerate(side_matrix))
                for i_tuple in generator:
                    i_tuple[1].value = side_matrix_values[i_tuple[0]]

                determinator += i_matrix_elem.value * ((-1) ** (2 + i)) * FindDeterminator.find_determinator(side_matrix)

            return determinator


def matrix_creation():
    while True:
        try:
            strings_len = int(input("\nВведите M матрицы: "))
            table_len = int(input("Введите N матрицы: "))

        except ValueError:
            print('\nВводите цифры!\n')

        else:
            matrix = Matrix(strings_len=strings_len, tables_len=table_len)
            break

    for i_elem in matrix:
        while True:
            try:
                value = int(input(f"\nВведите значение a{i_elem.string_index}{i_elem.table_index}: "))

            except ValueError:
                print("\nВводите цифры!\n")

            else:
                i_elem.value = value
                break

    return matrix


while True:
    matrix = matrix_creation()
    print(f'\nМатрица: {matrix}\nОпределитель: {FindDeterminator.find_determinator(matrix)}')
