class Node:
    __slots__ = 'user_name', 'user_mail', '_next', '_previous'

    def __init__(self, user_name, user_mail, _next, _previous):
        self.user_name = user_name
        self.user_mail = user_mail
        self._next = _next
        self._previous = _previous


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def create_user(self, name, mail):
        new_user = Node(name, mail, None, None)
        if self.is_empty():
            self.head = new_user
            self.tail = new_user
        else:
            self.tail._next = new_user
            new_user._previous = self.tail
            self.tail = new_user
        self.size += 1

    def display(self):
        if self.is_empty():
            print('The list is empty\n')
            return False
        else:
            p = self.head
            while p is not None:
                print('User:', p.user_name)
                print('Mail:', p.user_mail, '\n')
                p = p._next

    def display_reverse(self):
        if self.is_empty():
            print('The list is empty\n')
            return False
        else:
            p = self.tail
            while p is not None:
                print('User:', p.user_name)
                print('Mail:', p.user_mail, '\n')
                p = p._previous

    def search(self, mail):
        if self.is_empty():
            print('The list is empty\n')
            return False
        else:
            p = self.head
            while p is not None:
                if p.user_mail == mail:
                    print('User with the mail', '"' + mail + '"', 'is found!')
                    print('User:', p.user_name)
                    print('Mail:', p.user_mail, '\n')
                    return True
                p = p._next
            print('User with mail', mail, 'is not found\n')
            return False


    def add_to_beginning(self, name, mail):
        new_user = Node(name, mail, None, None)
        if self.is_empty():
            self.head = new_user
            self.tail = new_user
        else:
            self.head._previous = new_user
            new_user._next = self.head
            self.head = new_user
        self.size += 1

    def add_user_to_random_place(self, add_name, add_mail, position):
        if position < 1 or position > len(self):
            print('The list contains', self.size, 'elements')
            print("You can't insert in non existing position!\n")
            return False
        inserting_user = Node(add_name, add_mail, None, None)
        p = self.head
        i = 0
        while i < position - 1:
            p = p._next
            i += 1
        if p == self.head:
            self.head._previous = inserting_user
            inserting_user._next = self.head
            self.head = inserting_user
            self.size += 1
            return inserting_user
        elif p == self.tail:
            inserting_user._next = self.tail
            inserting_user._previous = self.tail._previous
            self.tail._previous._next = inserting_user
            self.tail._previous = inserting_user
            self.size += 1
            return inserting_user
        inserting_user._next = p._next
        p._next._previous = inserting_user
        p._next = inserting_user
        inserting_user._previous = p
        self.size += 1

    def remove_user(self, mail):
        if self.is_empty():
            print('The list is empty\n')
            return False
        else:
            p = self.head
            while p is not None:
                if p.user_mail == mail:
                    break
                p = p._next
            if p is None:
                print('User with mail', mail, 'is not found\n')
                return False
            elif p == self.head:
                self.head = self.head._next
                p._next = None
                p = self.head
                self.size -= 1
                return p
            elif p == self.tail:
                self.tail = self.tail._previous
                self.tail._next = None
                self.size -= 1
                return p
            p._previous._next = p._next
            p._next._previous = p._previous
            self.size -= 1


user = DoublyLinkedList()
