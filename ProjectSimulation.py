import HashTableLinked as htb
import BinaryHashTable as bht
import matplotlib.pyplot as plt
import timeit
import numpy

'''
This file contains the the simulation of the insertions into the two hashtables
Running this file produces a line graph which shows
'''

def main():

    a = htb.HashTable()
    b = bht.HashTable()

#Insertions for Linkedlist Hashtable

    for i in range(1024):
        m = 0 #accumilator to add the time for every single insertion
        start_1 = timeit.default_timer()
        a.insert(numpy.random.randint(16385,65335))
        end_1 = timeit.default_timer()
        ftime1 = end_1 - start_1 #used to find the time elapsed
        m += ftime1

    average_time_1 = m/1024


    for i in range(1024):
        k = 0
        start_2 = timeit.default_timer()
        a.insert(numpy.random.randint(16385,65335))
        end_2 = timeit.default_timer()
        ftime2 = end_2 - start_2
        k += ftime2

    average_time_2 = k/1024

    for i in range(1024):
        c = 0
        start_3 = timeit.default_timer()
        a.insert(numpy.random.randint(16385,65335))
        end_3 = timeit.default_timer()
        ftime3 = end_3 - start_3
        c += ftime3

    average_time_3 = c/1024

    for i in range(1024):
        d = 0
        start_4 = timeit.default_timer()
        a.insert(numpy.random.randint(16385,65335))
        end_4 = timeit.default_timer()
        ftime4 = end_4 - start_4
        d += ftime4

    average_time_4 = d/1024

    for i in range(1024):
        e = 0
        start_5 = timeit.default_timer()
        a.insert(numpy.random.randint(16385,65335))
        end_5 = timeit.default_timer()
        ftime5 = end_5 - start_5
        e += ftime5

    average_time_5 = e/1024

    for i in range(1024):
        f = 0
        start_6 = timeit.default_timer()
        a.insert(numpy.random.randint(16385,65335))
        end_6 = timeit.default_timer()
        ftime6 = end_6 - start_6
        f += ftime6

    average_time_6 = f/1024

    for i in range(1024):
        g = 0
        start_7 = timeit.default_timer()
        a.insert(numpy.random.randint(16385,65335))
        end_7 = timeit.default_timer()
        ftime7 = end_7 - start_7
        g += ftime7

    average_time_7 = g/1024

    for i in range(1024):
        h = 0
        start_8 = timeit.default_timer()
        a.insert(numpy.random.randint(16385,65335))
        end_8 = timeit.default_timer()
        ftime8 = end_8 - start_8
        h += ftime8

    average_time_8 = h/1024

#Simulation for the Binary Search tree Hashtable

    for i in range(1024):
        a = 0
        start_1 = timeit.default_timer()
        b.insert(numpy.random.randint(16385, 65335))
        end_1 = timeit.default_timer()
        ftime1 = end_1 - start_1
        a += ftime1

    ave_time_1 = a / 1024

    for i in range(1024):
        k = 0
        start_2 = timeit.default_timer()
        b.insert(numpy.random.randint(16385,65335))
        end_2 = timeit.default_timer()
        ftime2 = end_2 - start_2
        k += ftime2

    ave_time_2 = k / 1024

    for i in range(1024):
        c = 0
        start_3 = timeit.default_timer()
        b.insert(numpy.random.randint(16385, 65335))
        end_3 = timeit.default_timer()
        ftime3 = end_3 - start_3
        c += ftime3

    ave_time_3 = c / 1024

    for i in range(1024):
        d = 0
        start_4 = timeit.default_timer()
        b.insert(numpy.random.randint(16385, 65335))
        end_4 = timeit.default_timer()
        ftime4 = end_4 - start_4
        d += ftime4

    ave_time_4 = d / 1024

    for i in range(1024):
        e = 0
        start_5 = timeit.default_timer()
        b.insert(numpy.random.randint(16385, 65335))
        end_5 = timeit.default_timer()
        ftime5 = end_5 - start_5
        e += ftime5

    ave_time_5 = e / 1024

    for i in range(1024):
        f = 0
        start_6 = timeit.default_timer()
        b.insert(numpy.random.randint(16385,65335))
        end_6 = timeit.default_timer()
        ftime6 = end_6 - start_6
        f += ftime6

    ave_time_6 = f / 1024

    for i in range(1024):
        g = 0
        start_7 = timeit.default_timer()
        b.insert(numpy.random.randint(16385,65335))
        end_7 = timeit.default_timer()
        ftime7 = end_7 - start_7
        g += ftime7

    ave_time_7 = g / 1024

    for i in range(1024):
        h = 0
        start_8 = timeit.default_timer()
        b.insert(numpy.random.randint(16385,65335))
        end_8 = timeit.default_timer()
        ftime8 = end_8 - start_8
        h += ftime8

    ave_time_8 = h / 1024

    xvalues = [average_time_1, average_time_2, average_time_3, average_time_4, average_time_5, average_time_6,
               average_time_7, average_time_8]

    xvalues2 = [ave_time_1, ave_time_2, ave_time_3, ave_time_4, ave_time_5, ave_time_6,
               ave_time_7, ave_time_8]


    xticks = ["1024", "2048",  "3072", "4096", "5120", "6144", "7168", "8192"]
    xval = [0,1,2,3,4,5,6,7]
    plt.plot(xvalues)
    plt.plot(xvalues2)
    plt.legend(["Linked List", "Binary Search Tree"])
    plt.xlabel("Number of key insertions")
    plt.ylabel("Average time in seconds")
    plt.xticks(xval,xticks)
    plt.title("Average time for two hashing collsion methods")
    plt.show()

main()


