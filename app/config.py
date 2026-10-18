"""Configurações centrais do robô."""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

FORM_URL = (
    "https://docs.google.com/forms/d/e/"
    "1FAIpQLSeexx7UIdINMacDmxDHcXwXm2A5fwK6Gv_-CGK6tGcmnrh9Tw/viewform"
)

SHEET_ID = "1ndhcjPmjm3UGcgOm2vOfU5PQbQWKL51k6gxVhkmcIyw"
SHEET_CSV_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"

# Arquivo que guarda qual a próxima linha da planilha a ser processada
STATE_FILE = BASE_DIR / "estado.json"

# --- Modo demonstração ---
HEADLESS = False          # navegador visível
SLOW_MO_MS = 400          # atraso entre ações para acompanhar o robô
PAUSA_FINAL_MS = 3_000    # tempo exibindo a tela de confirmação antes de fechar
TIMEOUT_MS = 30_000

# Mapeamento: coluna da planilha -> título da pergunta no formulário
COLUNAS_TEXTO = {
    "Nome Completo": "Nome Completo",
    "E-mail": "E-mail",
    "Telefone / WhatsApp": "Telefone / WhatsApp",
    "Cidade / Estado": "Cidade / Estado",
    "LinkedIn / Portfólio": "Link do LinkedIn / Portfolio",
    "Curso / Área de Estudo": "Curso / Area de Estudo",
    "Instituição de Ensino": "Instituicao de Ensino",
    "Ano de Conclusão / Previsão": "Ano de Conclusao / Previsao",
    "Cargo Mais Recente": "Cargo Mais Recente",
    "Empresa": "Empresa",
    "Período de Atuação": "Periodo de Atuacoes",
    "Descrição das Principais Atividades": "Descricao das Principais Atividades",
    "Principais Habilidades / Tecnologias": "Principais Habilidades / Tecnologias",
}

COLUNAS_ESCOLHA = {
    "Nível de Escolaridade": "Nivel de Escolaridade",
}
