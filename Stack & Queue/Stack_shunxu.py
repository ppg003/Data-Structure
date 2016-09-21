
class Stack(object):

    def __init__(self, structure_max):
        self.structure_max = structure_max
        self.datas = []
        self.top = -1

    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    def push(self, data):
        if self.top < self.structure_max - 1:
            self.datas.append(data)
            self.top += 1
        else:
            raise MemoryError("out of index.")

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            self.datas.pop()
        else:
            raise MemoryError("Stack is empty")

    def peek(self):
        if self.isEmpty():
            return None
        return self.datas[self.top]

    def size(self):
        return self.top + 1

    def print_stack(self):
        print("\n")
        print(" _____________")
        if self.isEmpty():
            print("|_____________| <-- Top&Bottom")
        else:
            for i in range(self.top, -1, -1):
                print("|____", end="")
                print(str(self.datas[i]).center(5, "_"), end="")
                if i == self.top and i == 0:
                    print("____| <-- Top&Bottom")
                elif i == self.top:
                    print("____| <-- Top")
                elif i == 0:
                    print("____| <-- Bottom")
                else:
                    print("____|")
structure_max = 10
x = Stack(structure_max)
for i in range(structure_max):
    x.push(i)

x.print_stack()

x.pop()
x.pop()
x.pop()

x.print_stack()

x.pop()
x.print_stack()
x.pop()

x.print_stack()