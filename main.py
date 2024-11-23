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

    @classmethod
    def plus(cls, first_object: object, second_object: object) -> object:
        if isinstance(second_object, Matrix) and isinstance(first_object, Matrix):
            if second_object.n_max == first_object.n_max and second_object.m_max == first_object.m_max:

                output_matrix = Matrix(strings_len=first_object.m_max, tables_len=first_object.n_max)

                matrix_1_values = [i.value for i in first_object]
                matrix_2_values = [i.value for i in second_object]

                gen = ((matrix_1_values[count] + matrix_2_values[count], i) for count, i in enumerate(output_matrix))
                for i in gen:
                    i[1].value = i[0]

                return output_matrix

            else:
                print("\nНевозможно для матриц разного разряда!\n")
                return None

        else:
            print("\nВ метод класса передан не экземпляр класса Matrix!\n")
            return None

    @classmethod
    def minus(cls, first_object: object, second_object: object) -> object:
        if isinstance(second_object, Matrix) and isinstance(first_object, Matrix):
            if second_object.n_max == first_object.n_max and second_object.m_max == first_object.m_max:

                output_matrix = Matrix(strings_len=first_object.m_max, tables_len=first_object.n_max)

                matrix_1_values = [i.value for i in first_object]
                matrix_2_values = [i.value for i in second_object]

                gen = ((matrix_1_values[count] - matrix_2_values[count], i) for count, i in enumerate(output_matrix))
                for i in gen:
                    i[1].value = i[0]

                return output_matrix

            else:
                print("\nНевозможно для матриц разного разряда!\n")
                return None

        else:
            print("\nВ метод класса передан не экземпляр класса Matrix!\n")
            return None

    @classmethod
    def multiplication(cls, first_object: int, second_object: object) -> object:
        if isinstance(second_object, Matrix):
            output_matrix = Matrix(second_object.m_max, second_object.n_max)

            matrix_2_values = [i.value for i in second_object]

            gen = ((first_object * matrix_2_values[count], i) for count, i in enumerate(output_matrix))
            for i in gen:
                i[1].value = i[0]

            return output_matrix

        else:
            print("\nВ метод класса передан не экземпляр класса Matrix!\n")
            return None

    @classmethod
    def matrix_multiplication(cls, first_object: object, second_object: object) -> object:
        if isinstance(second_object, Matrix) and isinstance(first_object, Matrix):
            if second_object.m_max == first_object.n_max:

                print(f"Произведение матриц: {first_object}\n{second_object}")

                output_matrix = Matrix(strings_len=first_object.m_max, tables_len=second_object.n_max)

                first_object_first_index = 0 - first_object.n_max
                second_object_first_index = -1

                for count, i in enumerate(output_matrix):
                    print(f'\na{i.string_index}{i.table_index} = ', end='')

                    if count % output_matrix.n_max == 0:
                        second_object_first_index = -1
                        first_object_first_index += first_object.n_max

                    second_object_first_index += 1

                    i_elem_value = 0
                    first_object_index = first_object_first_index
                    second_object_index = second_object_first_index

                    for _ in range(first_object.n_max):
                        print(f"{first_object.matrix[first_object_index].value} * "
                              f"{second_object.matrix[second_object_index].value}", end=' + ')

                        i_elem_value += first_object.matrix[first_object_index].value * \
                                        second_object.matrix[second_object_index].value

                        first_object_index += 1
                        second_object_index += second_object.n_max

                    i.value = i_elem_value
                    print(f'0 = {i.value}')

                return output_matrix

            else:
                print("\nНевозможно для матриц разного разряда!\n")
                return None

        else:
            print("\nВ метод класса передан не экземпляр класса Matrix!\n")
            return None


class FindDeterminator(ABC):
    @classmethod
    def find_determinator(cls, matrix: Matrix):
        if matrix.n_max != matrix.m_max:
            print('\nМатрица не квадратная!\n')
            return None

        else:
            for i in matrix.matrix:
                if i.value is None:
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
    while True:
        try:
            answer = int(input("\n1)Сложение матриц"
                               "\n2)Вычитание матриц"
                               "\n3)Умножение матриц"
                               "\n4)Умножение матрицы"
                               "\n5)Решение линейного уравнения"
                               "\n6)Найти детерминатор матрицы"
                               "\nВаш вариант: "))

            if answer > 6 or answer < 1:
                raise ValueError

        except ValueError:
            print('\nВвод не корректен\n')

        else:
            if answer == 1:
                first_parameter = matrix_creation()
                second_parameter = matrix_creation()

                print('\n', Matrix.plus(first_object=first_parameter, second_object=second_parameter))

            elif answer == 2:
                first_parameter = matrix_creation()
                second_parameter = matrix_creation()

                print('\n', Matrix.minus(first_object=first_parameter, second_object=second_parameter))

            elif answer == 3:
                first_parameter = matrix_creation()
                second_parameter = matrix_creation()

                print('\n', Matrix.matrix_multiplication(first_object=first_parameter, second_object=second_parameter))

            elif answer == 4:
                while True:
                    try:
                        first_parameter = int(input("\nВведите число на которое будет умножена матрица: "))

                    except ValueError:
                        print('\nВвод не корректен\n')

                    else:
                        break

                second_parameter = matrix_creation()

                print('\n', Matrix.multiplication(first_object=first_parameter, second_object=second_parameter))

            elif answer == 5:
                print('\nСоздание матрицы A:')
                first_parameter = matrix_creation()

                print('\nСоздание матрицы B:')
                second_parameter = matrix_creation()

            elif answer == 6:
                first_parameter = matrix_creation()
                print('\n', FindDeterminator.find_determinator(first_parameter))
