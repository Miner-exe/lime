# CodeGen.py

class CodeGenerator:

    def __init__(self):
        self.instructions = []

    def emit(self, instruction):
        self.instructions.append(instruction)

    def generate_assignment(self, var, value):

        self.emit(f"MOV {var}, {value}")

    def generate_add(self, a, b):

        self.emit(f"ADD {a}, {b}")

    def generate_sub(self, a, b):

        self.emit(f"SUB {a}, {b}")

    def generate_mul(self, a, b):

        self.emit(f"MUL {a}, {b}")

    def generate_div(self, a, b):

        self.emit(f"DIV {a}, {b}")

    def show_code(self):

        print("\n=== GENERATED CODE ===")

        for ins in self.instructions:
            print(ins)