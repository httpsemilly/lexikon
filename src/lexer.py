from .token_type import TokenType
from .token import Token
from .keywords import KEYWORDS

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

