from Token_class import TokenType


class Interpreter:

    def __init__(self):

        self.variables = {}

    def visit(self, node):

        if type(node).__name__ == "NumberNode":

            return node.value

        elif type(node).__name__ == "VariableNode":

            return self.variables[node.name]

        elif type(node).__name__ == "AssignNode":

            value = self.visit(node.value)

            self.variables[node.name] = value

            return value

        elif type(node).__name__ == "PrintNode":

            value = self.visit(node.value)

            print(value)

            return value

        elif type(node).__name__ == "BinOpNode":

            left = self.visit(node.left)

            right = self.visit(node.right)

            match node.op.type:

                case TokenType.PLUS:
                    return left + right

                case TokenType.MINUS:
                    return left - right

                case TokenType.ASTERIK:
                    return left * right

                case TokenType.SLASH:
                    return left / right

                case TokenType.POW:
                    return left ** right

                case TokenType.MODULUS:
                    return left % right