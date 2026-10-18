"""View: exibe mensagens ao usuário via pop-up (Tkinter)."""
import sys
import tkinter as tk
from tkinter import messagebox


class PopupView:
    TITULO = "Robô de Cadastro"

    def _exibir(self, func, mensagem: str) -> None:
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        func(self.TITULO, mensagem, parent=root)
        root.destroy()

    def sucesso(self, mensagem: str = "O robô cadastrou os dados.") -> None:
        self._exibir(messagebox.showinfo, mensagem)

    def erro(self, mensagem: str) -> None:
        self._exibir(messagebox.showerror, mensagem)

    def log(self, mensagem: str) -> None:
        texto = f"[ROBÔ] {mensagem}"
        enc = sys.stdout.encoding or "utf-8"
        print(texto.encode(enc, errors="replace").decode(enc))
