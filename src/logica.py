class RegistroProfesores:
  # "username":
  #      "nombre:" "nombre apellido"
  # "materia":
  # lista de estudiantes
  # contraseña
  cuentas = {
    "camiloitt": {
      "nombre": "Camilo Torres",
      "materia": "Matematicas",
      "lista_estudiantes": [{"nombre": "Camilo Torres", "examen1": 5, "examen2": 3, "examen_recuperacion": 6}],
      "contrasena": "12345",
    }
  }

  def __init__(self):
    pass

  def existe_cuenta(self, user: str):
    # pass
    lista_profesores = list(self.cuentas.keys())
    index_profesor = lista_profesores.index(user)
    return False if index_profesor < 0 else True

  def agregar_cuenta(self, user: str, materia: str, contrasena: str):
    existe_cuenta = self.existe_cuenta(user)
    if not existe_cuenta:
      return

    self.cuentas[user]["nombre"] = user
    self.cuentas[user]["materia"] = materia
    self.cuentas[user]["lista_estudiantes"] = []
    self.cuentas[user]["contrasena"] = contrasena

  def crear_username(self, user: str):
    lista_profesores = self.cuentas.keys()
    username = user[0] + user[5:]
    nombres_similares = filter(
      lambda username_existentes: username == username_existentes,
      lista_profesores,
    )

    if len(nombres_similares) > 0:
      return nombres_similares + len(nombres_similares)
    return username

  def iniciar_session(self, user, contrasena):
    if user in self.cuentas and self.cuentas[user]["contrasena"] == contrasena:
      return self.cuentas[user]
    return None


class Profesor:
  informacion = {}

  def __init__(self, datos):
    self.informacion = datos

  def obtener_lista_alumnos(self):
    return self.informacion["materia"]
