from Token_class import Token, TokenType
from typing import Any


KEYWORDS = {
    "print": TokenType.PRINT,
    "if": TokenType.IF,
    "then": TokenType.THEN,
    "while": TokenType.WHILE,
    "do": TokenType.DO,
    "array": TokenType.ARRAY
}


class Lexer:

    def __init__(self, source: str) -> None:

        self.source = source

        self.position: int = -1
        self.read_position: int = 0
        self.line_no: int = 1

        self.current_char: str | None = None

        self.__read_char()

    def __read_char(self) -> None:

        if self.read_position >= len(self.source):
            self.current_char = None

        else:
            self.current_char = self.source[self.read_position]

        self.position = self.read_position

        self.read_position += 1

    def skip_whitespace(self) -> None:

        while self.current_char in [' ', '\t', '\n', '\r']:

            if self.current_char == '\n':
                self.line_no += 1

            self.__read_char()

    def __new_token(self, tt: TokenType, literal: Any) -> Token:

        return Token(
            type=tt,
            literal=literal,
            line_no=self.line_no,
            position=self.position
        )

    def __is_digit(self, ch: str) -> bool:

        return '0' <= ch <= '9'

    def __is_letter(self, ch: str) -> bool:

        return ch.isalpha() or ch == "_"

    def __read_number(self) -> Token:

        dot_count = 0

        output = ""

        while (
            self.current_char is not None and
            (
                self.__is_digit(self.current_char) or
                self.current_char == "."
            )
        ):

            if self.current_char == ".":
                dot_count += 1

            output += self.current_char

            self.__read_char()

        if dot_count == 0:

            return self.__new_token(
                TokenType.INT,
                int(output)
            )

        return self.__new_token(
            TokenType.FLOAT,
            float(output)
        )

    def __read_identifier(self) -> Token:

        output = ""

        while (
            self.current_char is not None and
            (
                self.__is_letter(self.current_char) or
                self.__is_digit(self.current_char)
            )
        ):

            output += self.current_char

            self.__read_char()

        if output in KEYWORDS:

            return self.__new_token(
                KEYWORDS[output],
                output
            )

        return self.__new_token(
            TokenType.IDENTIFIER,
            output
        )

    def next_token(self) -> Token:

        tok = None

        self.skip_whitespace()

        match self.current_char:

            case '+':
                tok = self.__new_token(TokenType.PLUS, '+')

            case '-':
                tok = self.__new_token(TokenType.MINUS, '-')

            case '*':
                tok = self.__new_token(TokenType.ASTERIK, '*')

            case '/':
                tok = self.__new_token(TokenType.SLASH, '/')

            case '^':
                tok = self.__new_token(TokenType.POW, '^')

            case '%':
                tok = self.__new_token(TokenType.MODULUS, '%')

            case '=':
                tok = self.__new_token(TokenType.EQUAL, '=')

            case ';':
                tok = self.__new_token(TokenType.SEMICOLON, ';')

            case '(':
                tok = self.__new_token(TokenType.LPAREN, '(')

            case ')':
                tok = self.__new_token(TokenType.RPAREN, ')')

            case '[':
                tok = self.__new_token(TokenType.LBRACKET, '[')

            case ']':
                tok = self.__new_token(TokenType.RBRACKET, ']')

            case ',':
                tok = self.__new_token(TokenType.COMMA, ',')

            case '"':
                raise Exception(
                    "Semantic Error: Strings are not allowed."
                )

            case None:
                tok = self.__new_token(TokenType.EOF, "")

            case _:

                if self.__is_digit(self.current_char):

                    return self.__read_number()

                elif self.__is_letter(self.current_char):

                    return self.__read_identifier()

                else:

                    tok = self.__new_token(
                        TokenType.ILLEGAL,
                        self.current_char
                    )

        self.__read_char()

        return tok