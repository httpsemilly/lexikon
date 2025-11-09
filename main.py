from src.lexer import Lexer
from src.token_type import TokenType
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

  tokens = []
  token = None

  try:
    while token is None or token.type != TokenType.EOF:
      token = lexer.next_token()
      tokens.append(token)
  except Exception as e:
    print(f"Error during lexical analysis: {e}")
    return

  print("=== Tokens found ===\n")
  for token in tokens:
    if token.type != TokenType.EOF:
      print(f"{token.type.name:15} | {token.lexeme:10} | Line {token.line}, Column {token.column}")
      
  print(f"\nTotal: {len(tokens) - 1} tokens")

if __name__ == "__main__":
    main()
