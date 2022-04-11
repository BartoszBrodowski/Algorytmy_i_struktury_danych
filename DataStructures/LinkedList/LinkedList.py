from tkinter import Y


class Node:
    def __init__(self, k):
        self.key = k

        # Błąd z Node(None) nie działa, bo tworzy się rekurencja, która tworzy nieskończenie wiele obiektów typu Node
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def wstaw(self, s):
        newElement = Node(s)
        temp = self.head

        newElement.next = self.head

        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = newElement

        else:
            newElement.next = newElement

        self.head = newElement

    def drukuj(self):
        x = self.head
        if self.head.next is not None:
            print("Head:" + str(x.key))
            while True:
                print(x.key, end=" ")
                x = x.next
                if (x == self.head):
                    print('\n')
                    break
        else:
            print('None')

    def szukaj(self, s):
        temp = self.head
        if s == temp.key:
            print('Head jest rowny s')
            return temp.key

        if temp is not None:
            while temp.next != self.head:
                if temp.key == s:
                    print("Znaleziono obiekt o wartosci: " + str(s))
                    return temp
                else:
                    temp = temp.next
        else:
            print('None')

    def usuń(self, s):
        temp = self.head

        # Sprawdzanie head'a
        if temp is not None:
            if (temp.key == s):
                self.head = temp.next
                return

        while temp is not None:
            if temp.key == s:
                break
            prev = temp
            temp = temp.next
            # next = temp.next
            # next.prev1 = temp.prev

        if temp == None:
            return

        # Tutaj temp już jest zinkrementowany, więc prev = 1, temp = 2,
        # dlatego 1.next = 2.next, czyli 1.next = 3, przez co wymazujemy drugi element
        prev.next = temp.next


l = LinkedList()

l.wstaw(6)
l.wstaw(5)
l.wstaw(4)

l.wstaw('LOL')
l.wstaw(7)

l.drukuj()

l.usuń(7)
l.drukuj()
# TODO USUWANIE PIERWSZEGO ELEMENTU DODAJE GO NA KONIEC
