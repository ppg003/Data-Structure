"""
对于(1-2)*(4+5)，如果用逆波兰表示法，应该是这样：1 2 – 4 5 + *
"""
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s : %(message)s"
)


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


def rpn(stack, expression):
    def plus(a, b):
        logging.debug("%s + %s = %s" % (a, b, a + b))
        return a + b

    def minus(a, b):
        logging.debug("%s - %s = %s" % (a, b, a - b))
        return a - b

    def multi(a, b):
        logging.debug("%s * %s = %s" % (a, b, a * b))
        return a * b

    def divis(a, b):
        res = None
        try:
            res = a / b
        except ZeroDivisionError:
            print("b=0")
        logging.debug("%s / %s = %s" % (a, b, res))
        return res

    list_operation = {
        "+": plus,
        "-": minus,
        "*": multi,
        "/": divis,
    }

    i = 0
    while i < len(expression):
        if isinstance(expression[i], int):
            stack.push(expression[i])
        else:
            b = stack.peek()
            stack.pop()
            a = stack.peek()
            stack.pop()
            res = list_operation[expression[i]](a, b)
            stack.push(res)
        i += 1
    return stack.peek()


expression = [1, 2, "-", 4, 5, "+", "*"]
x = Stack(20)
print(rpn(x, expression))