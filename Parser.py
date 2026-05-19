from Token_class import TokenType
from AST import *


class Parser:

    def __init__(self, lexer):

        self.lexer = lexer

        self.current_token = self.lexer.next_token()

    def eat(self, token_type):

        if self.current_token.type == token_type:

            self.current_token = self.lexer.next_token()

        else:

            raise Exception(
                f"Unexpected token {self.current_token.type}"
            )

    def factor(self):

        token = self.current_token

        if token.type in (TokenType.INT, TokenType.FLOAT):

            self.eat(token.type)

            return NumberNode(token.literal)

        elif token.type == TokenType.IDENTIFIER:

            self.eat(TokenType.IDENTIFIER)

            return VariableNode(token.literal)

        elif token.type == TokenType.LPAREN:

            self.eat(TokenType.LPAREN)

            node = self.expr()

            self.eat(TokenType.RPAREN)

            return node

    def power(self):

        node = self.factor()

        while self.current_token.type == TokenType.POW:

            op = self.current_token

            self.eat(TokenType.POW)

            node = BinOpNode(node, op, self.factor())

        return node

    def term(self):

        node = self.power()

        while self.current_token.type in (
            TokenType.ASTERIK,
            TokenType.SLASH,
            TokenType.MODULUS
        ):

            op = self.current_token

            self.eat(op.type)

            node = BinOpNode(node, op, self.power())

        return node

    def expr(self):

        node = self.term()

        while self.current_token.type in (
            TokenType.PLUS,
            TokenType.MINUS
        ):

            op = self.current_token

            self.eat(op.type)

            node = BinOpNode(node, op, self.term())

        return node

    def statement(self):

        # print(...)
        if self.current_token.type == TokenType.PRINT:

            self.eat(TokenType.PRINT)

            self.eat(TokenType.LPAREN)

            value = self.expr()

            self.eat(TokenType.RPAREN)

            return PrintNode(value)

        # assignment
        if self.current_token.type == TokenType.IDENTIFIER:

            name = self.current_token.literal

            self.eat(TokenType.IDENTIFIER)

            if self.current_token.type == TokenType.EQUAL:

                self.eat(TokenType.EQUAL)

                value = self.expr()

                return AssignNode(name, value)

            else:

                node = VariableNode(name)

                while self.current_token.type in (
                    TokenType.PLUS,
                    TokenType.MINUS,
                    TokenType.ASTERIK,
                    TokenType.SLASH,
                    TokenType.MODULUS,
                    TokenType.POW
                ):

                    op = self.current_token

                    self.eat(op.type)

                    node = BinOpNode(node, op, self.expr())

                return node

        return self.expr()

    def parse(self):

        statements = []

        while self.current_token.type != TokenType.EOF:

            stmt = self.statement()

            statements.append(stmt)

            if self.current_token.type == TokenType.SEMICOLON:

                self.eat(TokenType.SEMICOLON)

        return statements