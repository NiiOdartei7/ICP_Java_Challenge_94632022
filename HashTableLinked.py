import numpy
import math
import timeit

'''
This file contains the implementation of a hashtable using linked lists
as a collision resolution method
'''

#Node class which contains a value and a reference to the next value
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class HashTable:
    MaxArraySize = 509

    def __init__(self):
        self.buckets = [None]*self.MaxArraySize
        self.size = 0

    '''
    This is an implementation of the midsquare hashing methods
    It squares the value, turns the squared value into a string, finds the middle of the string
    turns it back into an int and uses that as the key
    '''
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


        head = node
        while node is not None:
            head = node
            node = node.next

        head.next = Node(x)


    def printHashTable(self):
        for i in range(self.MaxArraySize):
            current = self.buckets[i]
            if self.buckets[i] is not None:
                print("At index ", i,"the value ", current.data," is located")
                current = current.next
                print(" ")






        


