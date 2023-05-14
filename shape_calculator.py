class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h
    def __repr__(self):
        name = self.__class__.__name__
        if name=="Rectangle":
            return name+'(width='+str(self.width)+', height='+str(self.height)+')'
        elif name=="Square":
            return name+'(side='+str(self.width)+')'
    def set_width(self, w):
        self.width = w
        name = self.__class__.__name__
        if name=="Square":
            self.height = w
        return True
    def set_height(self, h):
        self.height = h
        name = self.__class__.__name__
        if name=="Square":
            self.width = h
        return True
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return 2*(self.width+self.height)
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    def get_picture(self):
        if self.width>50 or self.height>50:
            return "Too big for picture."
        else:
            row = ''
            for i in range(self.width):
                row = row+'*'
            row=row+'\n'
            rect = ''
            for i in range(self.height):
                rect=rect+row
            return rect
    def get_amount_inside(self,other):
        width_remainder = self.width % other.width
        width_divisor = self.width - width_remainder
        width_mult = int(width_divisor/other.width)
        height_remainder = self.height % other.height
        height_divisor = self.height - height_remainder
        height_mult = int(height_divisor/other.height)
        return width_mult*height_mult



class Square(Rectangle):
    def __init__(self, w):
        self.width = w
        self.height = w
    def set_side(self, w):
        self.width = w
        self.height = w
        return True