class Matrix:

    def __init__(self):
        self.r1 = 0
        self.c1 = 0
        self.r2 = 0
        self.c2 = 0
        self.constant = 0
        should_continue = self.users_choice()
        while should_continue:
            should_continue = self.users_choice()

    def make_matrix(self, r, c):
        matrix = []
        for i in range(int(r)):
            row = list(map(float, input().split()))
            matrix.append(row)

        return matrix

    def constant_method(self, matrix, constant):
        result = []
        for i in range(int(self.r1)):
            row = []
            for j in range(int(self.c1)):
                row.append(matrix[i][j] * float(constant))
            result.append(row)
        return result

    def constant_multiplication(self):
        self.r1, self.c1 = input("Enter size of matrix: ").split()
        print("Enter matrix")
        matrix = self.make_matrix(self.r1, self.c1)
        self.constant = input("Enter constant: ")
        constant = self.constant
        result = self.constant_method(matrix, constant)

        print("The result is:")
        for row in result:
            for element in row:
                print(element, end=" ")
            print()
        print()

    def users_choice(self):
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        print("Your choice: ")
        user_input = int(input())
        print()
        if user_input == 1:
            self.matrix_addition()
            return True
        elif user_input == 2:
            self.constant_multiplication()
            return True
        elif user_input == 3:
            self.matrix_multiplication()
            return True
        elif user_input == 4:
            self.transpose_choice()
            return True
        elif user_input == 5:
            self.determinant_calculator()
            return True
        elif user_input == 6:
            self.inverse_matrix()
            return True
        elif user_input == 0:
            return False

    def matrix_addition(self):
        self.r1, self.c1 = input("Enter size of first matrix: ").split()
        print("Enter first matrix")
        matrix1 = self.make_matrix(self.r1, self.c1)
        self.r2, self.c2 = input("Enter size of second matrix: ").split()
        print("Enter second matrix")
        matrix2 = self.make_matrix(self.r2, self.c2)

        if self.r1 != self.r2 or self.c1 != self.c2:
            print("The operation cannot be performed.")
            return []
        else:
            result = []
            for i in range(int(self.r1)):
                row = []
                for j in range(int(self.c1)):
                    row.append(matrix1[i][j] + matrix2[i][j])
                result.append(row)
            print("The result is:")
            for row in result:
                for element in row:
                    print(element, end=" ")
                print()
            print()

    def matrix_multiplication(self):
        print("Enter size of first matrix: ")
        self.r1, self.c1 = input().split()
        print("Enter first matrix")
        matrix1 = self.make_matrix(self.r1, self.c1)
        print("Enter size of second matrix: ")
        self.r2, self.c2 = input().split()
        print("Enter second matrix")
        matrix2 = self.make_matrix(self.r2, self.c2)
        result = [[0 for i in range(int(self.c2))] for j in range(int(self.r1))]
        for i in range(int(self.r1)):
            for j in range(int(self.c2)):
                for k in range(int(self.c1)):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
        print("The result is:")
        for row in result:
            for element in row:
                print(element, end=" ")
            print()

    def main_diagonal_method(self, matrix, m, n):
        new_matrix = []
        for i in range(int(m)):
            new_list = []
            for j in range(int(n)):
                row = matrix[j]
                element = row[i]
                new_list.append(element)
            new_matrix.append(new_list)
        return new_matrix

    def main_diagonal(self):
        self.r1, self.c1 = input("Enter size of matrix: ").split()
        m = self.r1
        n = self.c1
        print("Enter matrix")
        matrix = self.make_matrix(self.r1, self.c1)
        # new_matrix = []
        # for i in range(int(m)):
        #     new_list = []
        #     for j in range(int(n)):
        #         row = matrix[j]
        #         element = row[i]
        #         new_list.append(element)
        #     new_matrix.append(new_list)
        new_matrix = self.main_diagonal_method(matrix, m, n)

        print("The result is:")
        for x in new_matrix:
            for element in x:
                print(element, end=" ")
            print()
        print()

    def side_diagonal(self):
        self.r1, self.c1 = input("Enter size of matrix: ").split()
        m = self.r1
        n = self.c1
        print("Enter matrix")
        matrix = self.make_matrix(self.r1, self.c1)
        new_matrix = []
        for i in range(int(m)):
            new_list = []
            for j in range(int(n)):
                row = matrix[j]
                element = row[i]
                new_list.append(element)

            new_list.reverse()
            new_matrix.append(new_list)

        new_matrix.reverse()

        print("The result is:")
        for x in new_matrix:
            for element in x:
                print(element, end=" ")
            print()
        print()

    def vertical_line(self):
        self.r1, self.c1 = input("Enter size of matrix: ").split()
        m = self.r1
        n = self.c1
        print("Enter matrix")
        matrix = self.make_matrix(self.r1, self.c1)

        new_list = []
        for j in range(int(n)):
            row = matrix[j]
            row.reverse()
            new_list.append(row)
        new_matrix = new_list

        print("The result is:")
        for x in new_matrix:
            for element in x:
                print(element, end=" ")
            print()
        print()

    def horizontal_line(self):
        self.r1, self.c1 = input("Enter size of matrix: ").split()
        m = self.r1
        n = self.c1
        print("Enter matrix")
        matrix = self.make_matrix(self.r1, self.c1)

        new_list = []
        for j in range(int(n)):
            row = matrix[j]
            new_list.append(row)
        new_list.reverse()
        new_matrix = new_list

        print("The result is:")
        for x in new_matrix:
            for element in x:
                print(element, end=" ")
            print()
        print()

    def transpose_choice(self):
        print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
        print("Your choice: ")
        transpose_input = int(input())
        if transpose_input == 1:
            self.main_diagonal()
        elif transpose_input == 2:
            self.side_diagonal()
        elif transpose_input == 3:
            self.vertical_line()
        elif transpose_input == 4:
            self.horizontal_line()

    def determinant(self, matrix, result=0):
        matrix_list = list(range(len(matrix)))
        if len(matrix) == 1:
            return matrix[0][0]
        elif len(matrix) == 2 and len(matrix[0]) == 2:
            determinant = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
            return determinant

        for fc in matrix_list:
            matrix_copy = matrix
            matrix_copy = matrix_copy[1:]
            height = len(matrix_copy)

            for i in range(height):
                matrix_copy[i] = matrix_copy[i][0:fc] + matrix_copy[i][fc + 1:]

            alternate_sign = (-1) ** (fc % 2)
            sub_det = self.determinant(matrix_copy)
            result += alternate_sign * matrix[0][fc] * sub_det

        return result

    def reduced_matrix(self, matrix, m, n):
        matrix = matrix[:int(m)] + matrix[int(m) + 1:]
        for i in range(0, len(matrix)):
            matrix[i] = matrix[i][:int(n)] + matrix[i][int(n) + 1:]
        return matrix

    def determinant_calculator(self):
        self.r1, self.c1 = input("Enter size of matrix: ").split()
        print("Enter matrix")
        matrix = self.make_matrix(self.r1, self.c1)
        result = self.determinant(matrix)
        print("The result is: ")
        print(result)

    def cofactor_calculator(self, matrix, m, n):
        cofactor_matrix = []
        for i in range(int(m)):
            cofactor_row = []
            for j in range(int(n)):
                reduced_matrix = self.reduced_matrix(matrix, i, j)
                cofactor_elem = (-1) ** (int(i) + int(j)) * self.determinant(reduced_matrix)
                cofactor_row.append(cofactor_elem)
            cofactor_matrix.append(cofactor_row)
        return cofactor_matrix

    def inverse_matrix(self):
        self.r1, self.c1 = input("Enter size of matrix: ").split()
        i = self.r1
        j = self.c1
        print("Enter matrix")
        matrix = self.make_matrix(self.r1, self.c1)
        det_matrix = self.determinant(matrix)
        ct = self.cofactor_calculator(matrix, i, j)
        ct = self.main_diagonal_method(ct, i, j)
        if det_matrix == 0:
            print("This matrix doesn't have an inverse.")
        else:
            inverse_matrix = self.constant_method(ct, 1 / det_matrix)  # (1 / det_matrix) * ct

            print("The result is:")
            for x in inverse_matrix:
                for element in x:
                    if element == 0.0 or element == -0.0:
                        print(0, end=" ")
                    else:
                        print(int(element * 100) / 100, end=" ")
                print()
            print()


test = Matrix()
