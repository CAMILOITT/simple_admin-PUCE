import tkinter as tk

from src.gui import IniciarSession, PaginaInicio
from src.logica import Profesor


class App(tk.Tk):
  profesor = Profesor({})

  def __init__(self):
    super().__init__()
    self.title("Demo App")
    self.geometry("900x500")
    self.frames = {}
    paginas = [IniciarSession, PaginaInicio]

    for F in paginas:
      frame = F(self)
      self.frames[F] = frame
      frame.grid(row=0, column=0, sticky="nsew")

    self.ver_pagina(IniciarSession)

  def ver_pagina(self, pagina):
    frame = self.frames[pagina]
    frame.tkraise()
    if hasattr(frame, "cargar_datos"):
      frame.cargar_datos()


app = App()
app.mainloop()
