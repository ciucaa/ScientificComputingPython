class Rectangle:
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)

    def __str__(self):
        string = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
        return string

    def set_width(self, width):
        self.width = width 
        return width

    def set_height(self, height):
        self.height = height
        return height

    def get_area(self):
        area = self.height * self.width
        return area

    def get_perimeter(self):
        perimeter = 2 * self.height + 2 * self.width
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** 0.5)
        return diagonal

    def get_picture(self):
        line = ""
        lines = ""
        if int(self.width) > 50:
            return "Too big for picture."
        elif int(self.height) > 50:
            return "Too big for picture."
        else:
            for i in range(self.width):
                line += "*"

            for h in range(self.height):
                lines += line + '\n'
            return lines
        
    def get_amount_inside(self, shape):
        if shape.height <= self.height:
            if shape.width <= self.width:
                amount = int(self.width / shape.width) * int(self.height/shape.height)
                return amount      
        else:
          return 0

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        string = "Square(side=" + str(self.width) + ")"
        return string