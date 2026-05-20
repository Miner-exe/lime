from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter
from Token_class import TokenType

from TAC import TACGenerator
from Optimizer import Optimizer
from RegisterAllocator import RegisterAllocator
from AssemblyGenerator import AssemblyGenerator


if __name__ == "__main__":

    try:

        with open("tests/lexer.kor", "r") as f:
            code = f.read()

        print("\nSource Code:\n")

        print(code)

        # =========================
        # LEXER
        # =========================

        print("\nLexer:\n")

        lexer = Lexer(code)

        while True:

            tok = lexer.next_token()

            print(tok)

            if tok.type == TokenType.EOF:
                break

        # =========================
        # PARSER
        # =========================

        print("\nParser:\n")

        lexer = Lexer(code)

        parser = Parser(lexer)

        tree = parser.parse()

        print(tree)

        # =========================
        # TAC
        # =========================

        print("\nThree Address Code:\n")

        tac = TACGenerator()

        for stmt in tree:
            tac.generate(stmt)

        for line in tac.code:
            print(line)

        # =========================
        # OPTIMIZER
        # =========================

        print("\nOptimizer:\n")

        optimizer = Optimizer()

        optimized = optimizer.optimize(tac.code)

        for line in optimized:
            print(line)

        # =========================
        # REGISTER ALLOCATION
        # =========================

        print("\nRegister Allocation:\n")

        allocator = RegisterAllocator()

        allocated = allocator.allocate(optimized)

        for line in allocated:
            print(line)

        # =========================
        # ASSEMBLY
        # =========================

        print("\nAssembly Code:\n")

        asm = AssemblyGenerator()

        assembly = asm.generate(optimized)

        for line in assembly:
            print(line)

        # =========================
        # INTERPRETER
        # =========================

        print("\nInterpreter:\n")

        interpreter = Interpreter()

        result = None

        for stmt in tree:

            result = interpreter.visit(stmt)

        print("\nFinal Result:\n")

        print(result)

    except Exception as e:

        print("\n================ ERROR ================\n")

        print(e)