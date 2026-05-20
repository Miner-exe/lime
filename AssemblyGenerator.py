class AssemblyGenerator:

    def generate(self, tac_code):

        asm = []

        for line in tac_code:

            parts = line.split()

            if len(parts) < 3:
                continue

            # PRINT
            if parts[0] == "PRINT":

                asm.append(
                    f"OUT {parts[1]}"
                )

            # Assignment
            elif len(parts) == 3:

                asm.append(
                    f"MOV {parts[0]}, {parts[2]}"
                )

            # Arithmetic
            elif len(parts) == 5:

                dest = parts[0]

                left = parts[2]

                op = parts[3]

                right = parts[4]

                if op == "+":

                    asm.append(
                        f"ADD {dest}, {left}, {right}"
                    )

                elif op == "-":

                    asm.append(
                        f"SUB {dest}, {left}, {right}"
                    )

                elif op == "*":

                    asm.append(
                        f"MUL {dest}, {left}, {right}"
                    )

                elif op == "/":

                    asm.append(
                        f"DIV {dest}, {left}, {right}"
                    )

                elif op == "%":

                    asm.append(
                        f"MOD {dest}, {left}, {right}"
                    )

                elif op == "^":

                    asm.append(
                        f"POW {dest}, {left}, {right}"
                    )

        return asm