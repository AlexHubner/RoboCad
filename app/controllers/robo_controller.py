"""Controller: orquestra planilha -> formulário -> pop-up."""
from app import config
from app.models.estado_model import EstadoModel
from app.models.formulario_model import FormularioModel
from app.models.planilha_model import PlanilhaModel
from app.views.popup_view import PopupView


class RoboController:
    def __init__(self, planilha: PlanilhaModel, formulario: FormularioModel,
                 estado: EstadoModel, view: PopupView):
        self._planilha = planilha
        self._formulario = formulario
        self._estado = estado
        self._view = view

    def executar(self) -> bool:
        try:
            candidatos = self._planilha.carregar()
            indice = self._estado.proximo_indice(len(candidatos))
            candidato = candidatos[indice]
            self._view.log(f"Linha {candidato.numero_linha}: {candidato.nome}")

            self._formulario.enviar(candidato, config.COLUNAS_TEXTO, config.COLUNAS_ESCOLHA)

            self._estado.avancar(indice, len(candidatos))
            self._view.log("Formulário enviado com sucesso.")
            self._view.sucesso("O robô cadastrou os dados.")
            return True
        except Exception as exc:  # noqa: BLE001
            self._view.log(f"Falha: {exc}")
            self._view.erro(f"Ocorreu um erro ao cadastrar os dados:\n{exc}")
            return False
