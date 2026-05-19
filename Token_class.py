from enum import Enum
from typing import Any

class TokenType(Enum):
    #special tokens
    EOF = "EOF"
    ILLEGAL = "ILLEGAL"

    #data types
 
    INT = "INT"
    FLOAT = "FLOAT"

    #arithmatic symbols
    PLUS = "PLUS"
    MINUS = "MINUS"
    ASTERIK = "ASTERIK"
    SLASH = "SLASH"
    POW = "POW"
    MODULUS = "MODULUS"

    #Symbols

    SEMICOLON = "SEMICOLON"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"

class Token:
    def __init__(self, type: TokenType, literal: Any, line_no: int, position: int) -> None:
        self.type = type
        self.literal = literal
        self.line_no = line_no
        self.position = position

    def __str__(self) -> str:
        return f"token[{self.type} : {self.literal} : Line {self.line_no} : Postition {self.position}]"
           
    def __repr__(self) -> str:
        return str(self)
