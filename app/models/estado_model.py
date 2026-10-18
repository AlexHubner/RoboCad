"""Model que persiste qual linha deve ser usada na próxima execução."""
import json
from pathlib import Path


class EstadoModel:
    def __init__(self, arquivo: Path):
        self._arquivo = arquivo

    def proximo_indice(self, total: int) -> int:
        indice = 0
        if self._arquivo.exists():
            try:
                indice = int(json.loads(self._arquivo.read_text("utf-8")).get("proximo_indice", 0))
            except (ValueError, json.JSONDecodeError):
                indice = 0
        return indice % total  # recomeça do início ao chegar no fim

    def avancar(self, indice_atual: int, total: int) -> None:
        self._arquivo.write_text(
            json.dumps({"proximo_indice": (indice_atual + 1) % total}), encoding="utf-8"
        )
