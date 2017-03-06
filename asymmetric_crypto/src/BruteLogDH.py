import sys

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
    def compute(self, A, B, p, g, range):
        a = None
        b = None
        # Compute powers a,b (discrete log)
        for i in xrange(range):
            a = g ** i % p
            if (A == a):
                a = i
                print "a: %s" % (i)
                break
        for i in xrange(range):
            b = g ** i % p
            if (B == b):
                b = i
                print "b: %s" % (i)
                break
        # Test DH key
        kb = B ** a % p
        ka = A ** b % p
        if (ka == kb): print "Key valid, k: %s" % (ka)

    if __name__ == '__main__':
        if len(sys.argv) == 5:
            A = sys.argv[1]
            B = sys.argv[2]
            p = sys.argv[3]
            g = sys.argv[4]
            range = sys.argv[5]
        else:
            print('Please provide all arguments for A,B,p,g,range')
            sys.exit(1)

        # Example bruteLog(7, 5, 11, 6, 10)
        compute(A, B, p, g, range)
