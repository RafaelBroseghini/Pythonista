import math

class BloomFilter(object):
    def __init__(self, count, falsePosPct=0):
        m = -1 * (count * math.log(falsePosPct/100)) / ((math.log(2)) ** 2)
        k = (m/count)*math.log(2)
    
        self.bA = bytearray(int(m+7)//8)
        self.numHashes = int(k + 0.5)
    
    def add(self, word):
        for i in range(self.numHashes):
            hv = hash(word + str(i))
            bitIndex = hv % len((self.bA)*8)
            bAindex = bitIndex // 8
            exponent = bitIndex % 8

            mask = 2 ** exponent

            self.bA[bAindex] |= mask
    
    def __contains__(self, word):
        for i in range(self.numHashes):
            hv = hash(word + str(i))
            bitIndex = hv % len((self.bA)*8)

            bAindex = bitIndex // 8
            exponent = bitIndex % 8

            mask = 2 ** exponent

            value = self.bA[bAindex] & mask

            if value == 0:
                return False
            
        return True
    
    def __str__(self):
        rv = str(self.numHashes) + " " + str(len(self.bA)) + "\n"
        for i in range(len(self.bA)-1, -1, -1):
            rv += bin(self.bA[i])
        return rv


def main():
    b = BloomFilter(5,1)

    b.add("dog")
    b.add("cow")
    b.add("cat")

    print(b)

    print("dog" in b)
    print("school" in b)

if __name__ == '__main__':
    main()
