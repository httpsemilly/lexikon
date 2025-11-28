class Symbol:
    def __init__(self, name: str, line: int, column: int, order: int):
        self.name: str = name
        self.line: int = line
        self.column: int = column
        self.order: int = order
        self.count: int = 1
    
    def increment(self):
        self.count += 1
    
    def __str__(self) -> str:
        return f"{self.order:5} | {self.name:18} | {self.count:5} | Linha {self.line:3}, Coluna {self.column:3}"
