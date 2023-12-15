class A:
    def ___init____ (self, num1,num2):
        self.num1= num1
        self. num2= num2

class B:
    def ___ init____ (self,num1,num2):
        super().____init ____(num1,num2):

    def fetch_last_digit(self):
        last_digit_num1 = self.num1 % 10
        last _digit_num2= self.num2 % 10
        return last_digit_num1, last_digit_num2

class c(B):
    def __init____ (self,num1,num2):
        super().____init __(num1,num2):

    def multiply_last_digit(self):
        last_digit_num1, last_digit_num2=self.fetch_last_digits()
         result = last _digit_num1 * last_ digit_num2
        return result

        num1 = 123
        num2 = 456

        obj_a =A(num1, num2)
        obj_b =A(num1, num2)
        obj_c =A(num1, num2)

last_digits =obj_b.fetch_last_digits()
 print("Last digit:",last digits)

 result = obj_c.multiply_last_digits()
 print("Result of multiplying last digit:", result)