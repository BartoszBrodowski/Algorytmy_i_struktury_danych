import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        
        # Robimy node, aby działały metody next i prev
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    # def first_node(self):
    #     # Jeśli next element wartownika to on sam, lista jest pusta
    #     if self.sentinel.next == self.sentinel:
    #         return None
    #     else:
    #         return self.sentinel.next
    
    def wstaw(self, s):
        new_element = Node(s)
        if self.sentinel.next == self.sentinel:
            self.sentinel.next = new_element
            self.sentinel.prev = new_element
            new_element.next = self.sentinel
            new_element.prev = self.sentinel
        else:
            new_element.next = self.sentinel.next
            self.sentinel.next.prev = new_element
            self.sentinel.next = new_element
            new_element.prev = self.sentinel

    def drukuj(self):
        x = self.sentinel.next
        while x != self.sentinel:
            print(x.value, end=" ")
            x = x.next

    def szukaj(self, s):
        x = self.sentinel.next
        while x != self.sentinel:
            if x.value == s:
                print("\n" + "Szukany element został znaleziony: " + str(x.value))
                return x
            else:
                x = x.next

    def usuń(self, s):
        x = self.sentinel.next
        while x != self.sentinel:
            if x.value == s:
                x.prev.next = x.next
                x.next.prev = x.prev
                x = None
                return x
            else:
                x = x.next

    def bezpowtorzeń(self):
        x = self.sentinel.prev
        zbior = {}
        if x == self.sentinel:
            return self

        nowa_lista = LinkedList()

        while x != self.sentinel:
            if x.value in zbior.keys():
                x = x.prev
                continue
            else:
                zbior[x.value] = 'Jest'
                nowa_lista.wstaw(x.value)
                x = x.prev

        nowa_lista.drukuj()
        return nowa_lista

    def scal(self, l2): 
        temp = self.sentinel.prev
        self.sentinel.prev.next = l2.sentinel.next
        l2.sentinel.prev.next = temp
        self.drukuj()
        return self

l = LinkedList()
l.wstaw('What')
l.wstaw('WW')
l.wstaw('WW')
l.wstaw('LOL')
l.wstaw('K')
l.wstaw('K')
l.drukuj()
print("\n")
l.bezpowtorzeń()

lista_slow = ["drzewo", "jablko", "gruszka", "orzech"]
l1 = LinkedList()
l2 = LinkedList()
for i in range(4):
    l1.wstaw(lista_slow[i%4])
    l2.wstaw(lista_slow[(i+2)%4])
print('\n')
l1.drukuj()
print('\n')
l2.drukuj()
print('\n')

l.scal(l2)