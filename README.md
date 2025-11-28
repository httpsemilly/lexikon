
# LEXIKON: Lexer para linguagem Java

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Descrição

Um analisador léxico (lexer) para a linguagem Java desenvolvido em Python como projeto acadêmico para a disciplina de Compiladores. Este projeto implementa a fase de análise léxica de um compilador, responsável por converter código fonte em uma sequência de tokens.

## Objetivos Acadêmicos

- Compreender os fundamentos de compiladores
- Implementar a fase de análise léxica
- Trabalhar com expressões regulares
- Desenvolver habilidades em processamento de linguagens

## Funcionalidades

- Reconhecimento de tokens Java
- Suporte a números (inteiros e ponto flutuante)
- Identificação de palavras-chave e identificadores
- Reconhecimento de operadores e delimitadores
- Tratamento de strings literais
- Ignorar comentários e espaços em branco
- Controle de linha e coluna para mensagens de erro

## Estrutura do projeto

```
lexikon/
├── src/
│ ├── token.py
│ ├── token_type.py
│ ├── symbol.py
│ ├── symbol_table.py
│ ├── keywords.py
│ └── lexer.py
├── examples/
│ └── Calculator.java
│── main.py
└── README.md
```
## Rodando localmente

### Pré-requisitos

- Python 3.8 ou superior

### Execução via terminal

```bash
python main.py examples/Calculator.java
```

### Exemplo de uso
#### 1. Crie um arquivo Java na pasta examples:

```java
// examples/MeuPrograma.java

public class MeuPrograma {
    public static void main(String[] args) {
        int resultado = 10 + 5 * 2;
        System.out.println("Resultado: " + resultado);
    }
}
```

#### 2. Execute o lexer:

```bash
python main.py examples/MeuPrograma.java
```

#### 3. Saída esperada (exemplo):

```text
PUBLIC      | public      | Line 1, Column 1
CLASS       | class       | Line 1, Column 8
IDENTIFIER  | MeuPrograma | Line 1, Column 14
LEFT_BRACE  | {           | Line 1, Column 26
PUBLIC      | public      | Line 2, Column 5 
STATIC      | static      | Line 2, Column 12 
VOID        | void        | Line 2, Column 19 
IDENTIFIER  | main        | Line 2, Column 24 
...
```
