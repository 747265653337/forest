import math, random

class BlumBlumShub():

    # x(n+1) = (x(n)**2) % M

    # get big primes with miller-rabin test
    def miller_rabin_test(self, num_to_check, amnt_of_checks=40):

        # remove the 2 base cases, which interfere with the code
        if num_to_check == 2 or num_to_check == 3:
            return True

        # remove obvious cases
        if num_to_check % 2 == 0:
            return False

        # ha I can now assign multiple variables on one line
        r, d = 0, num_to_check - 1

        # get r and d for num_to_check = 2^r * d + 1
        while d % 2 == 0:
            r += 1
            d //= 2
        for _ in range(amnt_of_checks):
            a = random.randint(2, num_to_check - 2)
            x = pow(a, d, num_to_check)
            # if num_to_check is a prime it passes for nearly all bases
            if x == 1 or x == num_to_check - 1:
                continue
            # if it didn't it should pass this test
            for _ in range(r - 1):
                x = pow(x, 2, num_to_check)
                if x == num_to_check - 1:
                    break
            else:
                return False
        return True

    # get prime for that p % 4 == 3
    def getPrime(self, bits):
        candidate = random.getrandbits(bits) | 1 #ensures odd number

        while 1:
            if self.miller_rabin_test(candidate) and candidate & 3 == 3:
                return candidate
            candidate += 2


    def getM(self, bits):
        p1 = self.getPrime(bits//2)
        while 1:
            p2 = self.getPrime(bits//2)
            if p1 != p2:
                return p1 * p2

    def getSeed(self, bits):
        return random.getrandbits(bits)
    
    def nextpseudorand(self):
        self.state = self.state**2 % self.M
        return self.state

    def __init__(self, bits = 32):
        self.M = self.getM(bits)
        self.seed = self.getSeed(bits)
        self.state = self.seed
        print('initialized')

if __name__ == "__main__":
    BBS = BlumBlumShub(32)
    for _ in range(200):
        print(len(str(bin(BBS.nextpseudorand()))))
        