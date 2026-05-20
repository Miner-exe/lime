class RegisterAllocator:

    def __init__(self):

        self.registers = ["R1", "R2", "R3"]

        self.map = {}

        self.index = 0

    def allocate(self, tac_code):

        output = []

        for line in tac_code:

            parts = line.split()

            if len(parts) >= 3:

                dest = parts[0]

                if dest not in self.map:

                    reg = self.registers[
                        self.index % len(self.registers)
                    ]

                    self.map[dest] = reg

                    self.index += 1

                output.append(
                    f"{line}    [{self.map[dest]}]"
                )

        return output