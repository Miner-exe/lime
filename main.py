from Lexer import Lexer

LEXER_DEBUG: bool = True
if __name__ == '__main__':
    with open("tests/lexer.lime" , "r") as f:
     code: str = f.read()   

    if LEXER_DEBUG:
       debug_lex: Lexer = Lexer(source=code)
       while debug_lex.current_char is not None:
          print(debug_lex.next_token())
          