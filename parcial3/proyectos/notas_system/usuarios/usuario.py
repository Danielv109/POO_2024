
import funciones
import hashlib

# class usuario:
#     def__init__(self,nombre,apellidos,email,password):
#         self.nombre=nombre
#         self.apellidos=apellidos
#         self.email=email
#         self.password=password
    

    


# para encriptar la contraseña
def hash_password(self,contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()


def iniciar_sesion(self):
    contrasena=hashlib.sha256(self.contrasena.encode()).hexdigest()
    try:
        cursor.execute(
            "select * from usuarios where email=%s and password=%s"
            (self.email,contrasena)
        )
        # print(f"email: {self.email}")
        # print(f"contraseña: {contrasena}")
        usuario=cursor.fetchone()
        # print(f"Valor del registro: {usuario}")
        # funciones.esperarTecla()
        if usuario:
            return usuario
        else:
            return[]
    except:
        print(f"Entre a la excepcion")
        funciones.esperarTecla()
        # return[]

    # @staticmethod
