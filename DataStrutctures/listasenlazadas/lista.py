from Nodo import *

class Lista:
    def __init__(self):
        self.head = None

    def push(self, dato):
        new_node = Nodo(dato)
        new_node.setSiguiente(self.head)
        self_head = new_node
    
    def addAtBeginning(self, dato):
        temp = Nodo(dato)
        temp.setSiguiente(self.head)
        self.head = temp

    def addAtEnd(self,dato):
        newNodo = Nodo(dato)
        
        if self.head == None:
            self.head = newNodo
            return

        last = self.head

        while last.getSiguiente() != None:
            last = last.getSiguiente()
        
        last.setSiguiente(newNodo)

    def addAfterNPosition(self, dato, posicion):
        new_nodo = Nodo(dato)
        if posicion == 0:
            new_nodo.setSiguiente(self.head)
            self.head = new_nodo
            return
        else:
            aux = self.head
            while posicion > 0:
                posicion = posicion - 1
                aux = aux.getSiguiente()

            new_nodo.setSiguiente(aux.getSiguiente()) 
            aux.setSiguiente(new_nodo)

    def printList(self):
        aux = self.head

        while aux != None:
            print (aux.getDato(),end=" > ",)
            aux = aux.getSiguiente()
        
        print()

    def countList(self):
        aux, cont = self.head,0

        while aux != None:
            cont = cont + 1
            aux  = aux.getSiguiente()

        return cont

    def reverse(self):
        prev,curr,next = None, self.head, None

        while curr is not None:
            next = curr.getSiguiente()
            curr.setSiguiente(prev)
            prev = curr
            curr = next

        self.head = prev

        return self.head

    def reverse2(self,nodo,k):
        p,c,n = nodo,nodo.getSiguiente(),nodo.getSiguiente().getSiguiente()
        newTail = c

        while c and k>0:
            c.setSiguiente(p)
            k -= 1
            if k == 0: break

            p = c

            if n:
                c = n
                n = n.getSiguiente()
            else: break

        nodo.setSiguiente(c)
        newTail.setSiguiente(n)

        return

    def reverseKGroup(self,head,k):
        '''
        :type head : Nodo
        :type k: int
        :rtype :Nodo 
        '''
        
        while not head and not head.getSiguiente():
            return head

        if k == 1:
            return head

        dummy = Nodo(-1)
        dummy.setSiguiente(head)
        record = dummy
        left = head
        right = head.getSiguiente()
        count =1

        while True:
            while right and count < k: # reverse the links within a group
                tmp = right.getSiguiente()
                right.setSiguiente(left)
                prev = left
                left = right
                right = tmp
                count += 1
            
            if count == k: # rotate the group
                tmp = dummy.getSiguiente()
                dummy.setSiguiente(left)
                tmp.setSiguiente(right)
                dummy  = tmp
                count = 1
                left = right
                if right:
                    right = right.getSiguiente()

            else:
                if count >= 2:
                    left.setSiguiente(None)
                    if count > 2: # the last group has size < k and we need to reverse the links within the group again
                        while True:
                            tmp = prev.getSiguiente()
                            prev.setSiguiente(left)

                            if tmp .getSiguiente() == prev:
                                return record.getSiguiente()

                            left = prev
                            prev = tmp

                return record.getSiguiente()

    # Python implementation on bubble sort on linked lists

    def bub_sort_exhange(self):
        end = None
        while end != self.head:
            r = p = self.head
            while p.getSiguiente() != end:
                q = p.getSiguiente()
                if p.getDato() > q.getDato():
                    p.setSiguiente(q.getSiguiente())
                    q.setSiguiente(p)

                    if p != self.head:
                        r.setSiguiente(q)
                    else:
                        self.head = q
                
                    p,q = q,p

                r = p
                p = p.getSiguiente()
            
            end = p 

    # Python implementation for binary search algorithm on Linked Lists
    # method to find elements in the middle using fast and slow pointers
    def middleNode(self, start, last):
        if start is None: 
            return None

        slow = start
        fast = start.getSiguiente()

        while fast != last:
            fast = fast.getSiguiente()
            if fast != last:
                slow = slow.getSiguiente()
                fast = fast.getSiguiente()

        return slow

    #Method to find item in the linked list using binary search
    def binarySearch(self, head, value):
        start = head
        last = None

        while last == None or last != start:
            mid = self.middleNode(start,last)

            #Middle is empty or not
            if mid == None: return None
            
            if mid.getDato() == value: 
                return mid
            elif mid.getDato() > value:
                start = mid.getSiguiente()
            else:
                last = mid
        
        return None




if __name__ == '__main__':
    listita = Lista()
    
    
    listita.head = Nodo(25)
    e2 = Nodo(10)
    e3 = Nodo(4)
    
    listita.head.setSiguiente(e2)
    e2.setSiguiente(e3)
    
    #listita.printList()
    
    listita.addAtBeginning(20)
    listita.addAtBeginning(11)
    listita.addAtBeginning(49)

    #listita.printList()

    listita.addAtEnd(5)
    listita.addAtEnd(14)
    listita.addAtEnd(8)

    #listita.printList()

    listita.addAfterNPosition(6,3)
    listita.addAfterNPosition(30,7)
    
    listita.printList()
    print("\nLinked List elements",listita.countList())

    listita.head = listita.reverse()
    listita.printList()

    listita.head = listita.reverseKGroup(listita.head,3)
    listita.printList()

    listita.bub_sort_exhange()
    listita.printList()

    if listita.binarySearch(listita.head, 49) == None :
        print("Value is not found")
    else:
        print("Value is found")

    

