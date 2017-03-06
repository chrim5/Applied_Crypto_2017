"""
Goal: compute powers a,b (discrete log)
by brute force
Example parameter
A = 7
B = 5
p = 11
g = 6
5**3 % 13 = 3
"""


class BruteLogDH:
    def compute(self, A, B, p, g, r):
        a = None
        b = None
        # Compute powers a,b (discrete log)
        for i in xrange(r):
            a = g ** i % p
            if (A == a):
                a = i
                print "a: %s" % (i)
                break
        for i in xrange(r):
            b = g ** i % p
            if (B == b):
                b = i
                print "b: %s" % (i)
                break
        # Test DH key
        kb = B ** a % p
        ka = A ** b % p
        if (ka == kb): print "Key valid, k: %s" % (ka)

    def __init__(self, A, B, p, g, r):
        self.B = B
        self.A = A
        self.p = p
        self.g = g
        self.range = r
        self.compute(A, B, p, g, r)
