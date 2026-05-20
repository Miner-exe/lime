class TACGenerator:

    def __init__(self):

        self.code = []

        self.temp_count = 0

    def new_temp(self):

        self.temp_count += 1

        return f"t{self.temp_count}"

    def generate(self, node):

        node_type = type(node).__name__

        # Number
        if node_type == "NumberNode":

            return str(node.value)

        # Variable
        elif node_type == "VariableNode":

            return node.name

        # Assignment
        elif node_type == "AssignNode":

            value = self.generate(node.value)

            self.code.append(
                f"{node.name} = {value}"
            )

            return node.name

        # Print
        elif node_type == "PrintNode":

            value = self.generate(node.value)

            self.code.append(
                f"PRINT {value}"
            )

        # Binary Operations
        elif node_type == "BinOpNode":

            left = self.generate(node.left)

            right = self.generate(node.right)

            temp = self.new_temp()

            self.code.append(
                f"{temp} = {left} {node.op.literal} {right}"
            )

            return temp