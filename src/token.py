from .token_type import TokenType

class Token:
  def __init__(self, type: TokenType, lexeme: str, line: int, column: int) -> None:
    self.type: TokenType = type
    self.lexeme: str = lexeme
    self.line: int = line
    self.column: int = column

  def __str__(self) -> str:
    return f'{self.type.name}: {self.lexeme} at line {self.line}, column {self.column}'
