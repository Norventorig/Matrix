from abc import ABC


class Matrix_elem:
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
                self._values.append(Matrix_elem(string_index=m, table_index=n))

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
        self.m_ind = 1
        self.n_ind = 0

        return self

    def __next__(self):
        if self.n_ind + 1 <= self.n_max:
            self.n_ind += 1

        elif self.n_ind + 1 > self.n_max and self.m_ind + 1 <= self.m_max:
            self.n_ind = 1
            self.m_ind += 1

        else:
            raise StopIteration

        for i in self._values:
            if i.string_index == self.m_ind and i.table_index == self.n_ind:
                return i

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


class find_determinator(ABC):
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
    def determinator_rec(cls, matrix):
        if matrix.n_max == 3:
            return (matrix.matrix[0].value * matrix.matrix[4].value * matrix.matrix[8].value +
                    matrix.matrix[3].value * matrix.matrix[7].value * matrix.matrix[2].value +
                    matrix.matrix[1].value * matrix.matrix[5].value * matrix.matrix[6].value -
                    matrix.matrix[2].value * matrix.matrix[4].value * matrix.matrix[6].value -
                    matrix.matrix[7].value * matrix.matrix[5].value * matrix.matrix[0].value -
                    matrix.matrix[3].value * matrix.matrix[1].value * matrix.matrix[8].value)

        else:
            determinator = 0

            for count, i in enumerate(matrix):
                if count == matrix.n_max:
                    return determinator

                side_matrix = Matrix(matrix.m_max-1, matrix.n_max-1)
                index = 0

                for i_elem in side_matrix:

                    index += 1
                    j_index = 0

                    for j_elem in matrix:
                        if j_elem.string_index != i.string_index and j_elem.table_index != i.table_index:
                            j_index += 1

                            if j_index == index:
                                i_elem.value = j_elem.value

                determinator += i.value * (-1 ** (2 + count)) * find_determinator.find_determinator(side_matrix)

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
    print('\t\t\t\tMATRIX _A_ CREATION PROCESS STARTED!')
    a_matrix = matrix_creation()
    print(a_matrix, '\n\n\t\t\t\tMATRIX _A_ CREATION PROCESS FINISHED!\n', find_determinator.find_determinator(a_matrix))

# print('\n\t\t\t\tMATRIX _B_ CREATION PROCESS STARTED!')
# b_matrix = matrix_creation()
# print(b_matrix, '\n\n\t\t\t\tMATRIX _B_ CREATION PROCESS FINISHED!')
#
# print('\n\t\t\t\tMATRIX _C_ = MATRIX _A_ + MATRIX _B_ CREATION PROCESS STARTED!')
# c_matrix = Matrix.plus(a_matrix, b_matrix)
# print(c_matrix, '\n\n\t\t\t\tMATRIX _C_ CREATION PROCESS FINISHED!')
#
# print('\n\t\t\t\tMATRIX _D_ = MATRIX _A_ - MATRIX _B_ CREATION PROCESS STARTED!')
# d_matrix = Matrix.minus(first_matrix=a_matrix, another_matrix=b_matrix)
# print(d_matrix, '\n\n\t\t\t\tMATRIX _D_ CREATION PROCESS FINISHED!')
#
# print('\n\t\t\t\tMATRIX _E_ = MATRIX _A_ * MATRIX _B_ CREATION PROCESS STARTED!')
# e_matrix = Matrix.multiply(a_matrix, b_matrix)
# print(e_matrix, '\n\n\t\t\t\tMATRIX _E_ CREATION PROCESS FINISHED!')
#
# print('\n\t\t\t\tMATRIX _F_ = MATRIX _A_ / MATRIX _B_ CREATION PROCESS STARTED!')
# c_matrix = Matrix.plus(a_matrix, b_matrix)
# print(c_matrix, '\n\n\t\t\t\tMATRIX _F_ CREATION PROCESS FINISHED!')
