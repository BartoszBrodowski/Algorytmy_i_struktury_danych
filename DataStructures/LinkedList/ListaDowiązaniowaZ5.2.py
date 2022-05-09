import random
import copy


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
                print("\n" + "Szukany element zostal znaleziony: " + str(x.value))
                return x
            else:
                x = x.next
        print('Nie znaleziono elementu')
        return None

    def usuń(self, s):
        # Usuwa jeden węzeł z danym słowem
        # x = self.sentinel.next
        # while x != self.sentinel:
        #     if x.value == s:
        #         x.prev.next = x.next
        #         x.next.prev = x.prev
        #         x = None
        #         return x
        #     else:
        #         x = x.next

        # Usuwa wszystkie węzły z danym słowem
        x = self.sentinel.next
        while x != self.sentinel:
            if x.value == s:
                x.prev.next = x.next
                x.next.prev = x.prev
                x.value = None
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
        # temp = self.sentinel.prev.next
        # temp2 = self.sentinel.prev
        # self.sentinel.prev.next = l2.sentinel.next
        # self.sentinel.prev = l2.sentinel.prev
        # l2.sentinel.prev.next = self.sentinel
        # l2.sentinel.prev = temp2

        # Potrzeba głębokiej kopii aby nie zmieniać pierwotnych list na której wywołujemy funkcje
        L3 = copy.deepcopy(self)
        L2_copy = copy.deepcopy(l2)

        temp = L3.sentinel.prev
        L3.sentinel.prev.next = L2_copy.sentinel.next
        L3.sentinel.prev = L2_copy.sentinel.prev
        L2_copy.sentinel.prev.next = L3.sentinel
        L2_copy.sentinel.prev = temp

        x = L3.sentinel.next
        while x != L3.sentinel:
            print(x.value, end=" ")
            x = x.next

        return L3


print("---ZADANIE 1. a) Wstaw---")

l = LinkedList()
l.wstaw('TELEPORT')
l.wstaw('LOGARYTM')
l.wstaw('LOGARYTM')
l.wstaw('WALKA')
l.wstaw('KORONA')
l.wstaw('KORONA')
print("\n")

print("---ZADANIE 1. b) Drukuj---")
print("\n")
l.drukuj()

print("\n")
print("---ZADANIE 1. c) Szukaj---")

l.szukaj('TELEPORT')
l.szukaj('WARCABY')

# Wykomentowane, ponieważ zadanie 2 pokazuje wtedy wynik na wybrakowanej liście,
# bo tworzy kopię listy dowiązaniowej l

print("\n")
print("---ZADANIE 1. d) Usun---")
l.usuń('KORONA')
l.drukuj()
print("\n")

print("\n")
print("---ZADANIE 2. Bezpowtorzen---")
print("\n")
l.bezpowtorzeń()

print("\n")
print("---ZADANIE 3. Scal---")
print("\n")

lista_slow = ["drzewo", "jablko", "gruszka", "orzech"]

L2 = LinkedList()
for i in range(4):
    L2.wstaw(lista_slow[i])

l.scal(L2)
print("\n")

l.drukuj()
print("\n")

L2.drukuj()
