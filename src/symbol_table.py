from .symbol import Symbol

class SymbolTable:
    def __init__(self):
        self.symbols: dict[str, Symbol] = {}
        self.order_counter: int = 0
    
    def add(self, name: str, line: int, column: int):
        if name in self.symbols:
            self.symbols[name].increment()
        else:
            self.order_counter += 1
            self.symbols[name] = Symbol(name, line, column, self.order_counter)
    
    def get_all(self) -> list[Symbol]:
        return sorted(self.symbols.values(), key=lambda s: s.order)
    
    def __str__(self) -> str:
        if not self.symbols:
            return "Empty symbol table"
        
        result = "=== Symbol Table ===\n\n"
        result += f"{'Order':5} | {'Symbol':18} | {'Qt':5} | First occurency\n"
        result += "-" * 70 + "\n"
        
        for symbol in self.get_all():
            result += str(symbol) + "\n"
        
        result += f"\nUnique symbols: {len(self.symbols)}"
        return result
