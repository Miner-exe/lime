from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter
from Token_class import TokenType


if __name__ == "__main__":

    with open("tests/lexer.lime", "r") as f:
        code = f.read()

    # ==============================
    # SOURCE CODE
    # ==============================

    print("\nSource Code:\n")

    print(code)

    # ==============================
    # LEXER
    # ==============================

    print("\nLexer:\n")

    lexer = Lexer(code)

    tokens = []

    while True:

        tok = lexer.next_token()

        tokens.append(tok)

        print(tok)

        if tok.type == TokenType.EOF:
            break

    # ==============================
    # PARSER
    # ==============================

    print("\nParser:\n")

    lexer = Lexer(code)

    parser = Parser(lexer)

    tree = parser.parse()

    print(tree)

    # ==============================
    # INTERPRETER
    # ==============================

    print("\nInterpreter:\n")

    interpreter = Interpreter()

    result = None

    for stmt in tree:

        result = interpreter.visit(stmt)

    # ==============================
    # FINAL RESULT
    # ==============================

    print("\nFinal Result:\n")

    print(result)