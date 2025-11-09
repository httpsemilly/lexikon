from .token_type import TokenType
from .token import Token
from .keywords import KEYWORDS
import re

OPERATORS_AND_DELIMITERS = [
        TokenType.INCREMENT, TokenType.DECREMENT,
        TokenType.ADD_ASSIGN, TokenType.MINUS_ASSIGN, TokenType.TIMES_ASSIGN,
        TokenType.DIVIDE_ASSIGN, TokenType.MODULUS_ASSIGN,
        TokenType.EQUAL, TokenType.NOT_EQUAL,
        TokenType.GREATER_EQUAL, TokenType.LESS_EQUAL,
        TokenType.AND, TokenType.OR,
        TokenType.DOUBLE_COLON,
        TokenType.PLUS, TokenType.MINUS, TokenType.TIMES, TokenType.DIVIDE, TokenType.MODULUS,
        TokenType.ASSIGN, TokenType.NOT, TokenType.GREATER, TokenType.LESS,
        TokenType.BIT_AND, TokenType.BIT_OR, TokenType.BIT_XOR,
        TokenType.COLON, TokenType.QUESTION_MARK,
        TokenType.LEFT_PAREN, TokenType.RIGHT_PAREN,
        TokenType.LEFT_BRACE, TokenType.RIGHT_BRACE,
        TokenType.LEFT_SQUARE, TokenType.RIGHT_SQUARE,
        TokenType.SEMICOLON, TokenType.COMMA, TokenType.DOT
]

class Lexer:
  def __init__(self, source: str) -> None:
    self.source: str = source
    self.length: int = len(source)
    self.position: int = 0
    self.line: int = 1
    self.column: int = 1
    self.current_char: str | None = None

    if self.length > 0:
      self.current_char = source[0]

  def peek(self) -> str | None:
    next_position: int = self.position + 1

    if next_position < self.length:
      return self.source[next_position]
    else:
      return None

  def advance(self) -> None:
    if self.current_char is not None:
      if self.current_char == '\n':
        self.line += 1
        self.column = 1
      else:
        self.column += 1

    self.position += 1

    if self.position < self.length:
      self.current_char = self.source[self.position]
    else:
      self.current_char = None

  def skip_whitespace(self) -> None:
    while self.current_char is not None and self.current_char.isspace():
      self.advance()

  def skip_comment(self) -> None:
    if self.current_char is not None and self.current_char == '/':
      if self.peek() == '/':
        while self.current_char is not None and self.current_char != '\n':
          self.advance()
      elif self.peek() == '*':
        while self.current_char is not None and not (self.current_char == '*' and self.peek() == '/'):
          self.advance()

        if self.current_char is not None:
          self.advance()
          self.advance()

  def read_number(self) -> Token:
    current_line = self.line
    current_column = self.column
    match = TokenType.NUMBER.value.match(self.source, self.position)

    if match:
      number_str = match.group()

      if '.' in number_str:
        token_type = TokenType.FLOAT
      else:
        token_type = TokenType.INTEGER

      self.position += len(number_str)

      if self.position < self.length:
        self.current_char = self.source[self.position]
      else:
        self.current_char = None

      self.column += len(number_str)
    
      return Token(token_type, number_str, current_line, current_column)

  def read_identifier_or_keyword(self) -> Token:
    current_line = self.line
    current_column = self.column
    match = TokenType.IDENTIFIER.value.match(self.source, self.position)

    if match:
      identifier_str = match.group()

      token_type = KEYWORDS.get(identifier_str, TokenType.IDENTIFIER)

      self.position += len(identifier_str)

      if self.position < self.length:
        self.current_char = self.source[self.position]
      else:
        self.current_char = None

      self.column += len(identifier_str)

      return Token(token_type, identifier_str, current_line, current_column)

  def read_string(self) -> Token:
    current_line = self.line
    current_column = self.column
    match = TokenType.STRING.value.match(self.source, self.position)

    if match:
      string = match.group()

      token_type = TokenType.STRING

      self.position += len(string)

      if self.position < self.length:
        self.current_char = self.source[self.position]
      else:
        self.current_char = None

      self.column += len(string)

      return Token(token_type, string, current_line, current_column)

  def read_operator_or_delimiter(self) -> Token:
      current_line = self.line
      current_column = self.column
  
      for token_type in OPERATORS_AND_DELIMITERS:
        if isinstance(token_type.value, re.Pattern):
          match = token_type.value.match(self.source, self.position)
  
          if match:
            lexeme = match.group()
  
            self.position += len(lexeme)
            self.column += len(lexeme)
  
            if self.position < self.length:
              self.current_char = self.source[self.position]
            else:
              self.current_char = None
  
            return Token(token_type, lexeme, current_line, current_column)
  
      raise Exception(f"Invalid character '{self.current_char}' at line {current_line}, column {current_column}")

  def next_token(self) -> Token:
    self.skip_whitespace()

    while self.current_char is not None and self.current_char == '/' and (self.peek() == '/' or self.peek() == '*'):
      self.skip_comment()
      self.skip_whitespace()

    if self.current_char is None:
        return Token(TokenType.EOF, '', self.line, self.column)

    token_line = self.line
    token_column = self.column

    if self.current_char.isdigit():
      return self.read_number()
    elif self.current_char.isalpha() or self.current_char == '_':
      return self.read_identifier_or_keyword()
    elif self.current_char == '"':
      return self.read_string()
    else:
      return self.read_operator_or_delimiter()
