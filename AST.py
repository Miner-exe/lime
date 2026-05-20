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


class IfNode:

    def __init__(self, condition, expr):
        self.condition = condition
        self.expr = expr

    def __repr__(self):

        return (
            f"(if {self.condition} "
            f"then {self.expr})"
        )


class WhileNode:

    def __init__(self, count, expr):
        self.count = count
        self.expr = expr

    def __repr__(self):

        return (
            f"(while {self.count} "
            f"do {self.expr})"
        )


class ArrayNode:

    def __init__(self, name, elements):
        self.name = name
        self.elements = elements

    def __repr__(self):

        return (
            f"(array {self.name} = "
            f"{self.elements})"
        )


class BinOpNode:

    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):

        return (
            f"({self.left} "
            f"{self.op.literal} "
            f"{self.right})" 
        )