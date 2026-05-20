from Token_class import TokenType
from AST import *


class Parser:

    def __init__(self, lexer):

        self.lexer = lexer

        self.current_token = self.lexer.next_token()

        self.peek_token = self.lexer.next_token()

    # =========================
    # ERROR
    # =========================

    def error(self, msg):

        raise Exception(
            f"Parser Error: {msg}"
        )

    # =========================
    # ADVANCE
    # =========================

    def advance(self):

        self.current_token = self.peek_token

        self.peek_token = self.lexer.next_token()

    # =========================
    # EAT
    # =========================

    def eat(self, token_type):

        if self.current_token.type == token_type:

            self.advance()

        else:

            self.error(
                f"Expected {token_type} "
                f"but got {self.current_token.type}"
            )

    # =========================
    # FACTOR
    # =========================

    def factor(self):

        token = self.current_token

        # NUMBER
        if token.type in (
            TokenType.INT,
            TokenType.FLOAT
        ):

            self.eat(token.type)

            return NumberNode(token.literal)

        # VARIABLE
        elif token.type == TokenType.IDENTIFIER:

            self.eat(TokenType.IDENTIFIER)

            return VariableNode(token.literal)

        # PARENTHESES
        elif token.type == TokenType.LPAREN:

            self.eat(TokenType.LPAREN)

            node = self.expr()

            self.eat(TokenType.RPAREN)

            return node

        self.error("Invalid factor")

    # =========================
    # POWER
    # =========================

    def power(self):

        node = self.factor()

        while self.current_token.type == TokenType.POW:

            op = self.current_token

            self.eat(TokenType.POW)

            node = BinOpNode(
                node,
                op,
                self.factor()
            )

        return node

    # =========================
    # TERM
    # =========================

    def term(self):

        node = self.power()

        while self.current_token.type in (
            TokenType.ASTERIK,
            TokenType.SLASH,
            TokenType.MODULUS
        ):

            op = self.current_token

            self.eat(op.type)

            node = BinOpNode(
                node,
                op,
                self.power()
            )

        return node

    # =========================
    # EXPRESSION
    # =========================

    def expr(self):

        node = self.term()

        while self.current_token.type in (
            TokenType.PLUS,
            TokenType.MINUS
        ):

            op = self.current_token

            self.eat(op.type)

            node = BinOpNode(
                node,
                op,
                self.term()
            )

        return node

    # =========================
    # PRINT
    # =========================

    def print_statement(self):

        self.eat(TokenType.PRINT)

        self.eat(TokenType.LPAREN)

        value = self.expr()

        self.eat(TokenType.RPAREN)

        return PrintNode(value)

    # =========================
    # IF
    # =========================

    def if_statement(self):

        self.eat(TokenType.IF)

        condition = self.expr()

        self.eat(TokenType.THEN)

        stmt = self.statement()

        return IfNode(condition, stmt)

    # =========================
    # WHILE
    # =========================

    def while_statement(self):

        self.eat(TokenType.WHILE)

        count = self.expr()

        self.eat(TokenType.DO)

        stmt = self.statement()

        return WhileNode(count, stmt)

    # =========================
    # ARRAY
    # =========================

    def array_statement(self):

        self.eat(TokenType.ARRAY)

        name = self.current_token.literal

        self.eat(TokenType.IDENTIFIER)

        self.eat(TokenType.EQUAL)

        self.eat(TokenType.LBRACKET)

        elements = []

        if self.current_token.type == TokenType.RBRACKET:

            self.eat(TokenType.RBRACKET)

            return ArrayNode(name, elements)

        while True:

            elements.append(
                self.expr()
            )

            if self.current_token.type == TokenType.COMMA:

                self.eat(TokenType.COMMA)

            elif self.current_token.type == TokenType.RBRACKET:

                break

            else:

                self.error(
                    "Expected ',' or ']' in array."
                )

        self.eat(TokenType.RBRACKET)

        return ArrayNode(name, elements)

    # =========================
    # ASSIGNMENT
    # =========================

    def assignment(self):

        name = self.current_token.literal

        self.eat(TokenType.IDENTIFIER)

        self.eat(TokenType.EQUAL)

        value = self.expr()

        return AssignNode(name, value)

    # =========================
    # STATEMENT
    # =========================

    def statement(self):

        # PRINT
        if self.current_token.type == TokenType.PRINT:

            return self.print_statement()

        # IF
        elif self.current_token.type == TokenType.IF:

            return self.if_statement()

        # WHILE
        elif self.current_token.type == TokenType.WHILE:

            return self.while_statement()

        # ARRAY
        elif self.current_token.type == TokenType.ARRAY:

            return self.array_statement()

        # ASSIGNMENT
        elif (
            self.current_token.type == TokenType.IDENTIFIER
            and self.peek_token.type == TokenType.EQUAL
        ):

            return self.assignment()

        # NORMAL EXPRESSION
        return self.expr()

    # =========================
    # PARSE
    # =========================

    def parse(self):

        statements = []

        while self.current_token.type != TokenType.EOF:

            stmt = self.statement()

            statements.append(stmt)

            if self.current_token.type == TokenType.SEMICOLON:

                self.eat(TokenType.SEMICOLON)

        return statements