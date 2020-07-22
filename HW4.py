
#### Complete the code to built the ComplexNum Class
#### the necessary operator overloading: +, -, *

class ComplexNum:
    def __init__(self, x=0, y=0):
        if type(x)==int and type(y)==int:
            self.x = x
            self.y = y
        else:
            print('input must be integers!')

    def __str__(self):
        if self.y >= 0:
            return "{0} + {1}i".format(self.x, self.y)
        else:
            return "{0} - {1}i".format(self.x, -1*self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return ComplexNum(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return ComplexNum(x, y)

    def __mul__(self, other):
        x = (self.x * other.x) - (self.y * other.y)
        y = (self.x * other.y) + (self.y * other.x)
        return ComplexNum(x, y)

if __name__ == '__main__':
	C1 = ComplexNum(1, 2)
	C2 = ComplexNum(3, 4)

	C3 = C1 + C2
	print(C3)
	C4 = C1 - C2
	print(C4)
	C5 = C1 * C2
	print(C5)