import numpy
import math


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

        if x == 0:
            return 0

        elif x <= 3:
            return x

        else:
            key = x * x
            a  = str(key)
            output = a[0] + a[1]

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

def main():
    a = HashTable()
    a.insert(15)
    a.insert(20)
    a.insert(13)
    a.printHashTable()

main()







        


