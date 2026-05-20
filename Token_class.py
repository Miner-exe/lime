from enum import Enum


class TokenType(Enum):

    ILLEGAL = "ILLEGAL"
    EOF = "EOF"

    INT = "INT"
    FLOAT = "FLOAT"

    IDENTIFIER = "IDENTIFIER"

    PLUS = "+"
    MINUS = "-"
    ASTERIK = "*"
    SLASH = "/"
    POW = "^"
    MODULUS = "%"

    EQUAL = "="

    LPAREN = "("
    RPAREN = ")"

    LBRACKET = "["
    RBRACKET = "]"

    COMMA = ","

    SEMICOLON = ";"

    PRINT = "PRINT"

    IF = "IF"
    THEN = "THEN"

    WHILE = "WHILE"
    DO = "DO"

    ARRAY = "ARRAY"


class Token:

    def __init__(
        self,
        type: TokenType,
        literal,
        line_no,
        position
    ):

        self.type = type
        self.literal = literal
        self.line_no = line_no
        self.position = position

    def __repr__(self):

        return (
            f"token[{self.type} : "
            f"{self.literal} : "
            f"Line {self.line_no}]"
        )