# Robô de Cadastro (Python + Playwright, MVC)

A cada execução, o robô lê **uma** linha da planilha Google, preenche o Google Forms e mostra o pop-up **"O robô cadastrou os dados."**

## Estrutura
```
main.py                         # ponto de entrada
app/config.py                   # URLs e mapeamento coluna -> pergunta
app/models/candidato.py         # entidade (linha da planilha)
app/models/planilha_model.py    # lê a planilha (CSV público)
app/models/estado_model.py      # guarda a próxima linha (estado.json)
app/models/formulario_model.py  # automação Playwright
app/views/popup_view.py         # pop-up (Tkinter)
app/controllers/robo_controller.py
```

## Como executar
```bash
pip install -r requirements.txt
python -m playwright install chromium
python main.py
```

A linha usada avança a cada execução bem-sucedida (volta para a primeira ao chegar no fim).
Para recomeçar, apague o `estado.json`.
