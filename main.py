from src.lexer import Lexer
from src.token_type import TokenType
from src.symbol_table import SymbolTable
import sys

def main():
  if len(sys.argv) < 2:
   print("Usage: python main.py <arquivo.java>")
   exit(1)

  file_path = sys.argv[1]

  try:
    with open(file_path, 'r', encoding='utf-8') as file: 
      source_code = file.read()
  except FileNotFoundError:
    print(f"Error: File '{file_path}' not found!")
    return

  print(f"=== Analyzing: {file_path} ===\n")

  try:
    lexer = Lexer(source_code)
  except Exception as e:
    print(f"Error creating lexer: {e}")
    return

  symbol_table = SymbolTable()
  tokens = []
  token = None

  try:
    while token is None or token.type != TokenType.EOF:
      token = lexer.next_token()
      tokens.append(token)

      if token.type == TokenType.IDENTIFIER:
        symbol_table.add(token.lexeme, token.line, token.column)
  except Exception as e:
    print(f"Error during lexical analysis: {e}")
    return

  print("=== Tokens found ===\n")
  for token in tokens:
    if token.type != TokenType.EOF:
      print(f"{token.type.name:15} | {token.lexeme:10} | Line {token.line}, Column {token.column}")
      
  print(f"\nTotal: {len(tokens) - 1} tokens")
  print("\n")
  print(symbol_table)

if __name__ == "__main__":
    main()
