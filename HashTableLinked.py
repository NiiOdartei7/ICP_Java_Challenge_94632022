mport numpy
import math
import timeit


class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class HashTable:
    MaxArraySize = 509


    def __init__(self):
        self.buckets = [None]*self.MaxArraySize
        self.size = 0

    def hash(self, x):

        if x == 0:
            return 0

        elif x <= 3:
            return x

        else:
            key = x * x
            a  = str(key)
            output = a[len(a) // 2]

            g = int(output)
            hash_func = g % self.MaxArraySize



            return hash_func

    def insert(self, x):

        self.size += 1

        index = self.hash(x)

        node = self.buckets[index]

        if node is None:
            self.buckets[index] = Node(x)
            return

        prev = node
        while node is not None:
            prev = node
            node = node.next

        prev.next = Node(x)


    def printHashTable(self):
        for i in range(self.MaxArraySize):
            current = self.buckets[i]
            if self.buckets[i] is not None:
                print("At index ", i,"the value ", current.data," is located")
                current = current.next
                print(" ")

def sim():
    b = HashTable()

    for i in range(1024):
        a = 0
        start_1 = timeit.default_timer()
        b.insert(numpy.random.randint(16385,65335))
        end_1 = timeit.default_timer()
        ftime1 = end_1 - start_1
        a += ftime1

    print(a/1024)

    for i in range(1024):
        a = 0
        start_2 = timeit.default_timer()
        b.insert(numpy.random.randint(16385.65335))
        end_2 = timeit.default_timer()
        ftime2 = end_2 - start_2
        a += ftime2

    print(a/1024)

    for i in range(1024):
        a = 0
        start_3 = timeit.default_timer()
        b.insert(numpy.random.randint(16385.65335))
        end_3 = timeit.default_timer()
        ftime3 = end_3 - start_3
        a += ftime3

    print(a/1024)

    for i in range(1024):
        a = 0
        start_4 = timeit.default_timer()
        b.insert(numpy.random.randint(16385.65335))
        end_4 = timeit.default_timer()
        ftime4 = end_4 - start_4
        a += ftime4

    print(a/1024)

    for i in range(1024):
        a = 0
        start_5 = timeit.default_timer()
        b.insert(numpy.random.randint(16385.65335))
        end_5 = timeit.default_timer()
        ftime5 = end_5 - start_5
        a += ftime5

    print(a/1024)

    for i in range(1024):
        a = 0
        start_6 = timeit.default_timer()
        b.insert(numpy.random.randint(16385.65335))
        end_6 = timeit.default_timer()
        ftime6 = end_6 - start_6
        a += ftime6

    print(a/1024)

    for i in range(1024):
        a = 0
        start_7 = timeit.default_timer()
        b.insert(numpy.random.randint(16385.65335))
        end_7 = timeit.default_timer()
        ftime7 = end_7 - start_7
        a += ftime7

    print(a/1024)

    for i in range(1024):
        a = 0
        start_8 = timeit.default_timer()
        b.insert(numpy.random.randint(16385.65335))
        end_8 = timeit.default_timer()
        ftime8 = end_8 - start_8
        a += ftime8

    print(a/1024)

sim()







        


