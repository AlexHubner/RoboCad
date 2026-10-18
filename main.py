"""Ponto de entrada do robô."""
import sys

from app import config
from app.controllers.robo_controller import RoboController
from app.models.estado_model import EstadoModel
from app.models.formulario_model import FormularioModel
from app.models.planilha_model import PlanilhaModel
from app.views.popup_view import PopupView


def main() -> int:
    controller = RoboController(
        planilha=PlanilhaModel(config.SHEET_CSV_URL),
        formulario=FormularioModel(
            config.FORM_URL,
            headless=config.HEADLESS,
            timeout_ms=config.TIMEOUT_MS,
            slow_mo_ms=config.SLOW_MO_MS,
            pausa_final_ms=config.PAUSA_FINAL_MS,
        ),
        estado=EstadoModel(config.STATE_FILE),
        view=PopupView(),
    )
    return 0 if controller.executar() else 1


if __name__ == "__main__":
    sys.exit(main())
