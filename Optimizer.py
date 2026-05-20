class Optimizer:

    def optimize(self, tac_code):

        optimized = []

        for line in tac_code:

            parts = line.split()

            # constant folding
            if (
                len(parts) == 5 and
                parts[2].isdigit() and
                parts[4].isdigit()
            ):

                left = int(parts[2])

                op = parts[3]

                right = int(parts[4])

                result = None

                if op == "+":
                    result = left + right

                elif op == "-":
                    result = left - right

                elif op == "*":
                    result = left * right

                elif op == "/":
                    result = left / right

                optimized.append(
                    f"{parts[0]} {parts[1]} {result}"
                )

            else:

                optimized.append(line)

        return optimized