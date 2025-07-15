from tkinter import Frame, StringVar, messagebox, ttk

from src.logica import Profesor, RegistroProfesores


class IniciarSession(Frame):
  registro_profesores = RegistroProfesores()

  def __init__(self, master):
    super().__init__(master)
    nombre_profesor = StringVar()
    contrasena = StringVar()
    ttk.Label(self, text="username del profesor").pack()
    ttk.Entry(self, textvariable=nombre_profesor).pack()
    ttk.Entry(self, textvariable=contrasena, show="*").pack()
    ttk.Button(
      self, text="iniciar session", command=lambda: self.loguearse(nombre_profesor.get(), contrasena.get())
    ).pack()

  def loguearse(self, nombre, contrasena):
    if nombre == "" and contrasena == "":
      messagebox.showwarning("Campos vacíos", "Por favor ingrese el nombre de usuario y la contraseña.")
      return

    existe_profesor = self.registro_profesores.iniciar_session(nombre, contrasena)

    if not existe_profesor:
      messagebox.showinfo(
        "profesor no encontrado", "intente con otro usuario o pongase en contacto con el administrador"
      )
      return

    self.master.profesor = Profesor(existe_profesor)
    self.master.ver_pagina(PaginaInicio)


class PaginaInicio(Frame):
  def __init__(self, master):
    super().__init__(master)

    columnas_informacion = (
      "hombres aprobados",
      "hombres supletorioas",
      "Hombres reprobados",
      "mujeres aprobadas",
      "mujeres en supetorios",
      "mujeres reprobadas",
      "estudiantes repobrados",
    )

    self.tabla_informacion = ttk.Treeview(
      self,
      columns=columnas_informacion,
      show="headings",
    )

    for col in columnas_informacion:
      self.tabla_informacion.heading(col, text=col.capitalize())
      self.tabla_informacion.column(col, width=100)
    self.tabla_informacion.pack()

    columnas_estudiantes = ("nombre", "nota1", "nota2", "recuperacion", "estado")
    self.tabla_estudiantes = ttk.Treeview(self, columns=columnas_estudiantes, show="headings")

    for col in columnas_estudiantes:
      self.tabla_estudiantes.heading(col, text=col.capitalize())
      self.tabla_estudiantes.column(col, width=100)
    self.tabla_estudiantes.pack(fill="both", expand=True)

  def cargar_datos(self):
    if (
      not hasattr(self.master, "profesor")
      or not hasattr(self.master.profesor, "informacion")
      or "lista_estudiantes" not in self.master.profesor.informacion
    ):
      return

    self.estudiantes = self.master.profesor.informacion["lista_estudiantes"]
    self.mostrar_resumen()
    self.mostrar_estudiantes()

  def mostrar_estudiantes(self):
    self.tabla_estudiantes.delete(*self.tabla_estudiantes.get_children())

    for estudiante in self.estudiantes:
      nota1 = estudiante.get("examen1", 0)
      nota2 = estudiante.get("examen2", 0)
      recuperacion = estudiante.get("examen_recuperacion", 0)
      promedio = (nota1 + nota2) / 2
      final = max(promedio, recuperacion)
      estado = "Aprobado" if final >= 3 else "Reprobado"
      row_id = self.tabla_estudiantes.insert(
        "", "end", values=(estudiante.get("nombre", ""), nota1, nota2, recuperacion, estado)
      )
      if estado == "Reprobado":
        self.tabla_estudiantes.tag_configure("reprobado", background="red")
        self.tabla_estudiantes.item(row_id, tags=("reprobado",))

  def mostrar_resumen(self):
    # Inicializar contadores
    hombres_aprobados = 0
    hombres_supletorios = 0
    hombres_reprobados = 0
    mujeres_aprobadas = 0
    mujeres_supletorios = 0
    mujeres_reprobadas = 0
    estudiantes_reprobados = 0

    # for estudiante in getattr(self, "estudiantes", []):
    for estudiante in self.estudiantes:
      sexo = estudiante.get("sexo", "").lower()
      nota1 = estudiante.get("examen1", 0)
      nota2 = estudiante.get("examen2", 0)
      recuperacion = estudiante.get("examen_recuperacion", 0)
      promedio = (nota1 + nota2) / 2
      final = max(promedio, recuperacion)

      if final >= 3:
        if sexo == "m":
          hombres_aprobados += 1
        elif sexo == "f":
          mujeres_aprobadas += 1
        elif recuperacion >= 3:
          if sexo == "m":
            hombres_supletorios += 1
          elif sexo == "f":
            mujeres_supletorios += 1
        else:
          if sexo == "m":
            hombres_reprobados += 1
          elif sexo == "f":
            mujeres_reprobadas += 1
        estudiantes_reprobados += 1

    # Limpiar la tabla antes de insertar
    self.tabla_informacion.delete(*self.tabla_informacion.get_children())
    # Insertar los datos en la tabla de información
    self.tabla_informacion.insert(
      "",
      "end",
      values=(
        hombres_aprobados,
        hombres_supletorios,
        hombres_reprobados,
        mujeres_aprobadas,
        mujeres_supletorios,
        mujeres_reprobadas,
        estudiantes_reprobados,
      ),
    )
