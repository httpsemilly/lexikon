from enum import Enum
import re

class TokenType(Enum):
  EOF = 'EOF'
  
  # KEYWORDS
  INT = 'int'
  LONG = 'long'
  SHORT = 'short'
  BYTE = 'byte'
  DOUBLE = 'double'
  FLOAT = 'float'
  BOOLEAN = 'boolean'
  CHAR = 'char'

  IF = 'if'
  ELSE = 'else'
  SWITCH = 'switch'
  CASE = 'case'
  DEFAULT = 'default'
  BREAK = 'break'
  CONTINUE = 'continue'
  RETURN = 'return'
  WHILE = 'while'
  FOR = 'for'
  DO = 'do'
  TRUE = 'true'
  FALSE = 'false'

  PUBLIC = 'public'
  PRIVATE = 'private'
  PROTECTED = 'protected'

  STATIC = 'static'
  FINAL = 'final'
  ABSTRACT = 'abstract'
  SYNCHRONIZED = 'synchronized'
  VOLATILE = 'volatile'
  TRANSIENT = 'transient'

  CLASS = 'class'
  INTERFACE = 'interface'
  EXTENDS = 'extends'
  IMPLEMENTS = 'implements'
  NEW = 'new'
  THIS = 'this'
  SUPER = 'super'
  INSTANCEOF = 'instanceof'
  ENUM = 'enum'

  TRY = 'try'
  CATCH = 'catch'
  FINALLY = 'finally'
  THROW = 'throw'
  THROWS = 'throws'
  ASSERT = 'assert'

  PACKAGE = 'package'
  IMPORT = 'import'
  EXPORTS = 'exports'
  MODULE = 'module'
  VOID = 'void'
  VAR = 'var'
  REQUIRES = 'requires'
  NATIVE = 'native'

  # OPERATORS
  INCREMENT = re.compile(r'\+\+')
  DECREMENT = re.compile(r'--')

  ADD_ASSIGN = re.compile(r'\+\=')
  MINUS_ASSIGN = re.compile(r'-\=')
  TIMES_ASSIGN = re.compile(r'\*\=')
  DIVIDE_ASSIGN = re.compile(r'/\=')
  MODULUS_ASSIGN = re.compile(r'%\=')

  EQUAL = re.compile(r'\=\=')
  NOT_EQUAL = re.compile(r'!\=')
  GREATER = re.compile(r'>')
  LESS = re.compile(r'<')
  GREATER_EQUAL = re.compile(r'>\=')
  LESS_EQUAL = re.compile(r'<\=')

  PLUS = re.compile(r'\+')
  MINUS = re.compile(r'-')
  TIMES = re.compile(r'\*')
  DIVIDE = re.compile(r'/')
  MODULUS = re.compile(r'%')

  DOUBLE_COLON = re.compile(r'\:\:')
  COLON = re.compile(r'\:')
  QUESTION_MARK = re.compile(r'\?')

  ASSIGN = re.compile(r'\=')

  AND = re.compile(r'&&')
  OR = re.compile(r'\|\|')
  NOT = re.compile(r'!')

  BIT_AND = re.compile(r'&')
  BIT_OR = re.compile(r'\|')
  BIT_XOR = re.compile(r'\^')

  # DELIMITERS
  LEFT_PAREN = re.compile(r'\(')
  RIGHT_PAREN = re.compile(r'\)')
  LEFT_BRACE = re.compile(r'\{')
  RIGHT_BRACE = re.compile(r'\}')
  LEFT_SQUARE = re.compile(r'\[')
  RIGHT_SQUARE = re.compile(r'\]')
  COMMA = re.compile(r',')
  SEMICOLON = re.compile(r';')
  DOT = re.compile(r'\.')
  
  # LITERALS
  IDENTIFIER = re.compile(r'[_a-zA-Z][_a-zA-Z0-9]*')
  STRING = re.compile(r'"([^"\\]|\\.)*"|\'([^\'\\]|\\.)*\'')
  NUMBER = re.compile(r'\d+\.\d+|\d+')
