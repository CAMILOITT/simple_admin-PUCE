from tkinter import StringVar, messagebox, ttk

from .logica import RegistroProfesores


class IniciarSession:
  registro_profesores = RegistroProfesores()

  def __init__(self, ventana):
    self.registro_profesores.existe_cuenta
    self.ventana = ventana
    self.ver()

  def ver(self):
    nombre_profesor = StringVar()
    contrasena = StringVar()
    ttk.Label(self.ventana, text="username del profesor").pack()
    ttk.Entry(self.ventana, textvariable=nombre_profesor).pack()
    ttk.Entry(self.ventana, textvariable=contrasena, show="*").pack()
    ttk.Button(
      self.ventana, text="iniciar session", command=lambda: self.loguearse(nombre_profesor.get(), contrasena.get())
    ).pack()

  def loguearse(self, nombre, contrasena):
    existe_profesor = self.registro_profesores.existe_cuenta(nombre)
    if nombre == "" and contrasena == "":
      messagebox.showwarning("inputs vacios", "Por favor llene todos los inputs")
      return

    if not existe_profesor:
      messagebox.showinfo("profesor no encontrado", "intente con otro usuario o registre la nueva cuenta")
      return

    self.registro_profesores.iniciar_session(nombre, contrasena)
    print("iniciando session")
