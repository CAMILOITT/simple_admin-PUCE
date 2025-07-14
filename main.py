import tkinter as tk

from src.gui import IniciarSession


class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Demo App")
    self.geometry("400x300")
    self.ver_pagina_login()

  def ver_pagina_login(self):
    IniciarSession(self)


app = App()
app.mainloop()
# columnas = ("Nombre", "Edad", "Ciudad")


# tabla = ttk.Treeview(ventana, columns=columnas, show="headings")


# def pagina_registro(ventana):
#   ttk.Label(ventana, text="ingresa el nombre de usuario").pack()
#   ttk.Entry(
#     ventana,
#   ).pack()
#   ttk.Label(ventana, text="ingresa la contraseña").pack()
#   ttk.Entry(ventana, show="*").pack()
#   ttk.Button(ventana, text="Iniciar sesion").pack()


# pagina_registro(ventana)


# for col in columnas:
#   tabla.heading(col, text=col)
#   tabla.column(col, width=100)

# datos = [
#   ("Juan", 25, "Madrid"),
#   ("Ana", 30, "Barcelona"),
#   ("Luis", 22, "Valencia"),
# ]

# for fila in datos:
#   tabla.insert("", tk.END, values=fila)

# tabla.pack(fill=tk.BOTH, expand=True)


# def main():
#   exam1 = []
#   exam2 = []
#   sex = []
#   nombres = []
#   examrecu = []
#   sumaHombresExames = []
#   sumaMujeresExames = []

#   countHombresapro = 0
#   countMujeresapro = 0
#   apromujersuple = 0
#   repromujer = 0
#   aprohombresuple = 0
#   reprohombre = 0

#   n = int(input("Ingrese el número de estudiantes: "))

#   for i in range(n):
#     nombre = input(f"\nIngrese el nombre del estudiante {i + 1}: ")
#     nombres.append(nombre)

#     nota = int(input(f"Ingrese la nota del examen 1 para {nombre} (0-20): "))
#     while nota < 0 or nota > 20:
#       nota = int(input("Nota inválida. Ingrese nuevamente (0-20): "))
#     exam1.append(nota)

#     nota = int(input(f"Ingrese la nota del examen 2 para {nombre} (0-20): "))
#     while nota < 0 or nota > 20:
#       nota = int(input("Nota inválida. Ingrese nuevamente (0-20): "))
#     exam2.append(nota)

#     sexo = input(f"Ingrese el sexo de {nombre} (H/M): ").upper()
#     while sexo not in ["H", "M"]:
#       sexo = input("Sexo inválido. Ingrese nuevamente (H/M): ").upper()
#     sex.append(sexo)

#     suma = exam1[i] + exam2[i]

#     if sexo == "H":
#       sumaHombresExames.append(suma)
#       if suma >= 28:
#         print(f"\n{nombre}: APROBADO")
#         countHombresapro += 1
#       elif suma >= 18:
#         nota = int(input(f"Ingrese la nota del examen de recuperación para {nombre} (0-40): "))
#         while nota < 0 or nota > 40:
#           nota = int(input("Nota inválida. Ingrese nuevamente (0-40): "))
#         examrecu.append(nota)
#         if (nota + (suma / 2)) >= 24:
#           print(f"{nombre} APRUEBA EN SUPLETORIOS")
#           aprohombresuple += 1
#         else:
#           print(f"{nombre} REPROBADO")
#           reprohombre += 1
#     else:
#       sumaMujeresExames.append(suma)
#       if suma >= 28:
#         print(f"{nombre}: APROBADA")
#         countMujeresapro += 1
#       elif suma >= 18:
#         nota = int(input(f"Ingrese la nota del examen de recuperación para {nombre} (0-40): "))
#         while nota < 0 or nota > 40:
#           nota = int(input("Nota inválida. Ingrese nuevamente (0-40): "))
#         examrecu.append(nota)
#         if (nota + (suma / 2)) >= 24:
#           print(f"{nombre} APRUEBA EN SUPLETORIOS")
#           apromujersuple += 1
#         else:
#           print(f"{nombre} REPROBADA")
#           repromujer += 1

#   repro = reprohombre + repromujer
#   print(f"\nHombres aprobados: {countHombresapro}")
#   print(f"Hombres aprobados en suple: {aprohombresuple}")
#   print(f"Hombres reprobados: {reprohombre}")
#   print(f"Mujeres aprobadas: {countMujeresapro}")
#   print(f"Mujeres aprobadas en suple: {apromujersuple}")
#   print(f"Mujeres reprobadas: {repromujer}")
#   print(f"Estudiantes reprobados: {repro}")


# ventana.mainloop()


# import tkinter as tk

# root = tk.Tk()
# root.title("gestor de notas")

# root.mainloop()
