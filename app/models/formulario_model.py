"""Model que automatiza o Google Forms com Playwright."""
import re
import unicodedata

from playwright.sync_api import Page, sync_playwright

from app.models.candidato import Candidato


def normalizar(texto: str) -> str:
    """Remove acentos, espaços extras e caixa para comparações robustas."""
    sem_acento = unicodedata.normalize("NFKD", texto or "").encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", sem_acento).strip().lower()


class FormularioModel:
    def __init__(self, url: str, headless: bool = False, timeout_ms: int = 30_000,
                 slow_mo_ms: int = 0, pausa_final_ms: int = 0):
        self._url = url
        self._headless = headless
        self._timeout = timeout_ms
        self._slow_mo = slow_mo_ms
        self._pausa_final = pausa_final_ms

    def enviar(self, candidato: Candidato, campos_texto: dict, campos_escolha: dict) -> None:
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=self._headless,
                slow_mo=self._slow_mo,
                args=["--start-maximized"],
            )
            try:
                page = browser.new_page(no_viewport=True)
                page.bring_to_front()
                page.set_default_timeout(self._timeout)
                page.goto(self._url, wait_until="domcontentloaded")
                page.get_by_role("listitem").first.wait_for()

                for coluna, pergunta in campos_texto.items():
                    self._preencher_texto(page, pergunta, candidato.valor(coluna))

                for coluna, pergunta in campos_escolha.items():
                    self._selecionar_opcao(page, pergunta, candidato.valor(coluna))

                self._submeter(page)
                if self._pausa_final:
                    page.wait_for_timeout(self._pausa_final)
            finally:
                browser.close()

    # ---------- helpers ----------
    def _questao(self, page: Page, titulo: str):
        alvo = normalizar(titulo)
        itens = page.get_by_role("listitem")
        for i in range(itens.count()):
            item = itens.nth(i)
            heading = item.get_by_role("heading").first
            if heading.count() and normalizar(heading.inner_text()).rstrip(" *") == alvo:
                return item
        raise LookupError(f"Pergunta não encontrada no formulário: '{titulo}'")

    def _preencher_texto(self, page: Page, titulo: str, valor: str) -> None:
        if not valor:
            return
        campo = self._questao(page, titulo).locator("input[type='text'], input[type='email'], textarea").first
        campo.fill(valor)

    def _selecionar_opcao(self, page: Page, titulo: str, valor: str) -> None:
        if not valor:
            return
        radios = self._questao(page, titulo).get_by_role("radio")
        alvo = normalizar(valor)
        for i in range(radios.count()):
            radio = radios.nth(i)
            rotulo = radio.get_attribute("data-value") or radio.get_attribute("aria-label") or ""
            if normalizar(rotulo) == alvo:
                radio.click()
                return
        raise LookupError(f"Opção '{valor}' não encontrada na pergunta '{titulo}'")

    def _submeter(self, page: Page) -> None:
        page.get_by_role("button", name=re.compile(r"^(Enviar|Submit)$", re.I)).click()
        page.wait_for_url(re.compile(r"formResponse"))
