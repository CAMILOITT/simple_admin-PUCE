from tkinter import StringVar, ttk


def formulario_session(ventana, command_button):
  nombre_profesor = StringVar()
  contrasena = StringVar()
  ttk.Label(ventana, text="username del profesor").pack()
  ttk.Entry(ventana, textvariable=nombre_profesor).pack()
  ttk.Entry(ventana, textvariable=contrasena, show="*").pack()
  ttk.Button(
    ventana, text="iniciar session", command=lambda self: command_button(self, nombre_profesor.get(), contrasena.get())
  ).pack()
