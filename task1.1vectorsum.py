from math import sqrt

class Vector:
    def __init__(self, vector_list):
        self.vector_list = vector_list

    def __str__(self):
        return ', '.join([str(el) for el in self.vector_list])

    def __add__(self, other):
        return Vector(list(self.vector_list[i] + other.vector_list[i] for i in range(3)))

    def vector_len(self):
        v_len = 0
        for i in range(3):
            v_len += self.vector_list[i]**2
        v_len = sqrt(v_len)
        return v_len

if __name__ == '__main__':
    a = Vector([10, 10, 10])
    b = Vector([0, 0, -10])
    print(a)
    print(b)
    print(a + b)
    print(a.vector_len())
    print(b.vector_len())
    print((a + b).vector_len())

