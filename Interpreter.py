from Token_class import TokenType


class Interpreter:

    def __init__(self):

        self.variables = {}

    def visit(self, node):

        node_type = type(node).__name__

        # =========================
        # NUMBER
        # =========================

        if node_type == "NumberNode":

            return node.value

        # =========================
        # VARIABLE
        # =========================

        elif node_type == "VariableNode":

            if node.name not in self.variables:

                raise Exception(
                    f"Semantic Error: "
                    f"{node.name} is undefined."
                )

            value = self.variables[node.name]

            print(f"LOAD {node.name} -> {value}")

            return value

        # =========================
        # ASSIGNMENT
        # =========================

        elif node_type == "AssignNode":

            value = self.visit(node.value)

            self.variables[node.name] = value

            print(f"ASSIGN {node.name} = {value}")

            return value

        # =========================
        # PRINT
        # =========================

        elif node_type == "PrintNode":

            value = self.visit(node.value)

            print(f"PRINT -> {value}")

            return value

        # =========================
        # IF
        # =========================

        elif node_type == "IfNode":

            condition = self.visit(node.condition)

            print(f"IF condition = {condition}")

            if condition:

                result = self.visit(node.expr)

                print(f"IF RESULT -> {result}")

                return result

            print("IF condition was FALSE")

            return None

        # =========================
        # WHILE
        # =========================

        elif node_type == "WhileNode":

            count = self.visit(node.count)

            print(f"WHILE LOOP x{count}")

            results = []

            iteration = 1

            while count > 0:

                result = self.visit(node.expr)

                print(
                    f"Iteration {iteration} "
                    f"-> {result}"
                )

                results.append(result)

                iteration += 1

                count -= 1

            print(f"WHILE RESULTS -> {results}")

            return results

        # =========================
        # ARRAY
        # =========================

        elif node_type == "ArrayNode":

            arr = []

            for el in node.elements:

                arr.append(
                    self.visit(el)
                )

            self.variables[node.name] = arr

            print(
                f"ARRAY {node.name} = {arr}"
            )

            return arr

        # =========================
        # BINARY OPERATIONS
        # =========================

        elif node_type == "BinOpNode":

            left = self.visit(node.left)

            right = self.visit(node.right)

            match node.op.type:

                case TokenType.PLUS:

                    result = left + right

                    print(
                        f"{left} + {right} = {result}"
                    )

                    return result

                case TokenType.MINUS:

                    result = left - right

                    print(
                        f"{left} - {right} = {result}"
                    )

                    return result

                case TokenType.ASTERIK:

                    result = left * right

                    print(
                        f"{left} * {right} = {result}"
                    )

                    return result

                case TokenType.SLASH:

                    if right == 0:

                        raise Exception(
                            "Runtime Error: Division by zero."
                        )

                    result = left / right

                    print(
                        f"{left} / {right} = {result}"
                    )

                    return result

                case TokenType.POW:

                    result = left ** right

                    print(
                        f"{left} ^ {right} = {result}"
                    )

                    return result

                case TokenType.MODULUS:

                    result = left % right

                    print(
                        f"{left} % {right} = {result}"
                    )

                    return result