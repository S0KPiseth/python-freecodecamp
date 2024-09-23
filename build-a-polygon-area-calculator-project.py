import math
class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height
    def set_width(self, num):
        self.width=num
    def set_height(self, num):
        self.height = num
    def get_area(self):
        return self.width*self.height
    def get_diagonal(self):
        return math.sqrt(pow(self.width,2)+pow(self.height,2))

    def get_perimeter(self):
        return 2*(self.width+self.height)
    def get_picture(self):
        if self.width >50 or self.height>50:
            return 'Too big for picture.'
        else:
            colums = []
            rows = []
            picture=''
            for colum in range(self.width):
                colums.append("*")
            for row in range(self.height):
                rows.append(colums)
            for i in rows:
                
                picture += "".join(i)+"\n"
            return picture


    def get_amount_inside(self, shape):
        return math.floor(self.get_area()/shape.get_area())
    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(width=self.side,height=self.side)
    def set_side(self, num):
        self.__init__(num)

    def set_width(self, num):
        self.side =num
        super().set_width(num)
        super().set_height(num)
    def set_height(self, num):
        self.set_width(num)
    def get_diagonal(self):
        return math.sqrt(2)*self.side
    def __repr__(self):
        return f"Square(side={self.side})"



rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))