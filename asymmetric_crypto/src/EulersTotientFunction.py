class EulersTotientFunction:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def phi(self):
        a = self.n
        b = a - 1
        c = 0
        while b:
            if not self.gcd(a, b) - 1:
                c += 1
            b -= 1
        return c

    def __init__(self, n):
        self.n = n

"""
for i in range(11,41140):
    print phi(i)
"""
