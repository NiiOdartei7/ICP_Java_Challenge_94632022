import numpy


class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class HashTable:
    MaxArraySize = 20


    def __init__(self):
        self.buckets = [None]*self.MaxArraySize
        self.size = 0

    def hash(self, x):

        hash_func = x % self.MaxArraySize
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

            index = self.hash(i)
            node = self.buckets[index]
            if node is not None:
                current = node
                while (current != None):
                    print("At index ", i,"the value ", current.data," is located")
                    current = current.next
                print(" ")

def main():

    a = HashTable()

    for i in range(10):
        a.insert(numpy.random.randint(1,100))
    a.printHashTable()

main()








        


