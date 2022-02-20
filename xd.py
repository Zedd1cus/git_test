class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float) and cls.MIN_COORD <= x <= cls.MAX_COORD

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами')

    def get_coord(self):
        return self.__x, self.__y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left


pt = Point(1, 2)
pt.set_coord(10, 20)
pt.set_coord(-10, 100)
print(pt.__dict__)