from MatrixElem_class import MatrixElem


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

    @classmethod
    def matrix_creation(cls):
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
    def find_determinator(cls, matrix: object) -> float:
        if isinstance(matrix, Matrix) and matrix.n_max == matrix.m_max:
            for i in matrix.matrix:
                if i.value is None:
                    raise Exception

            if matrix.n_max == 1:
                return matrix.matrix[0].value

            elif matrix.n_max == 2:
                return matrix.matrix[0].value * matrix.matrix[3].value - matrix.matrix[1].value * matrix.matrix[2].value

            elif matrix.n_max == 3:
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

                    determinator += i_matrix_elem.value * ((-1) ** (2 + i)) * Matrix.find_determinator(
                        side_matrix)

                return determinator

        else:
            raise Exception

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

                        i_elem_value += (first_object.matrix[first_object_index].value *
                                         second_object.matrix[second_object_index].value)

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

    @classmethod
    def equation(cls, first_object: object, second_object: object) -> object:
        if isinstance(second_object, Matrix) and isinstance(first_object, Matrix):
            if first_object.n_max == first_object.m_max and first_object.n_max == second_object.m_max:
                determinator_a = Matrix.find_determinator(first_object)
                output_matrix = Matrix(second_object.m_max, second_object.n_max)

                for i_second_object_index in range(second_object.m_max):
                    temp_matrix = Matrix(first_object.m_max, first_object.n_max)

                    for j_m in range(first_object.m_max):
                        for j_n in range(first_object.n_max):
                            if j_n == i_second_object_index:
                                temp_matrix.matrix[j_m * temp_matrix.n_max + j_n].value = second_object.matrix[j_m].value

                            else:
                                temp_matrix.matrix[j_m * temp_matrix.n_max + j_n].value = \
                                    first_object.matrix[j_m * temp_matrix.n_max + j_n].value

                    output_matrix.matrix[i_second_object_index].value = \
                        Matrix.find_determinator(temp_matrix) / determinator_a

                return output_matrix

            else:
                return None
