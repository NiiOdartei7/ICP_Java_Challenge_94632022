
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:

    def __init__(self):
        self.head = None

    def addNode(self, x):
        Newnode = Node(x)

        self.head = Node("List Start")
        current = self.head
        while current.next != None:
            current = current.next

        current.next = Newnode

    def printlist(self):
        current = self.head.next
        while(current != None):
            print(current.data)
            if current.next == None:
                print(".")
            else:
                print(",")
            current = current.next
        print(" ")

class HashTable:
    MaxArraySize = 20

    def __init__(self):
        self.items = [None]*self.MaxArraySize
        self.l_items = Linkedlist()

    def add(self, x):
        hash_func = x%self.MaxArraySize

        if self.items[hash_func] == None:
            self.items[hash_func] = self.l_items

            self.l_items.addNode(x)

        else:
            self.l_items.addNode(x)

    def printHashTable(self):

        for i in range(self.MaxArraySize - 1):
            if self.items[i] == self.l_items:
                print("At index ", i, " the list is ", self.l_items.printlist())





def main():

    a = HashTable()

    a.add(10)
    a.add(11)
    a.add(12)
    a.add(13)

    a.printHashTable()


main()








        


