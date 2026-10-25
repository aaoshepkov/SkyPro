class Calculator:

    def sum(self, a, b):
        return a+b

    def div(self, a, b):
        if b == 0:
            raise ArithmeticError("Нельзя делить на ноль")
        return a/b

    def mul(self, a, b):
        return a*b

    def sub(self, a, b):
        return a-b

    def avg(self, arr):
        len_of_arr = len(arr)
        if len_of_arr == 0:
            return 0

        res = 0
        for i in arr:
            res += i
        avg = self.div(res, len_of_arr)
        return avg