class NumberNode:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


class VariableNode:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class AssignNode:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"({self.name} = {self.value})"


class PrintNode:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"print({self.value})"


class BinOpNode:

    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"({self.left} {self.op.literal} {self.right})"