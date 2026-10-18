"""Model que representa uma linha da planilha."""
from dataclasses import dataclass, field


@dataclass
class Candidato:
    numero_linha: int
    dados: dict = field(default_factory=dict)

    def valor(self, coluna: str) -> str:
        return (self.dados.get(coluna) or "").strip()

    @property
    def nome(self) -> str:
        return self.valor("Nome Completo")
