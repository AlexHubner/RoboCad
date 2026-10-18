"""Model responsável por ler os dados da planilha Google (CSV público)."""
import csv
import io
import urllib.request

from app.models.candidato import Candidato


class PlanilhaModel:
    def __init__(self, csv_url: str):
        self._csv_url = csv_url

    def carregar(self) -> list[Candidato]:
        with urllib.request.urlopen(self._csv_url, timeout=30) as resp:
            conteudo = resp.read().decode("utf-8-sig")

        leitor = csv.DictReader(io.StringIO(conteudo))
        candidatos = [
            Candidato(numero_linha=i, dados={k.strip(): v for k, v in linha.items() if k})
            for i, linha in enumerate(leitor, start=2)  # linha 1 = cabeçalho
            if any((v or "").strip() for v in linha.values())
        ]
        if not candidatos:
            raise ValueError("A planilha não possui linhas de dados.")
        return candidatos
