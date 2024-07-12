class Personas:
    def __init__(self,nombre,edad,tel):
        self.nombre =nombre
        self.edad = edad
        self.tel = tel

    def setNombre(self,nombre):
        self.nombre = nombre
    
    def getNombre(self):
        return self.nombre
    
    def setEdad(self,edad):
        self.edad = edad
    
    def getEdad(self):
        return self.edad
    
    def setTel(self,tel):
        self.tel = tel
    
    def getTel(self):
        return self.tel
    
    def Info_persona(self):
        print(f"Informacion de la persona {self.getNombre(), self.getEdad(), self.getTel()}")
    
class Estudiantes(Personas):
    def __init__(self,nombre,edad,tel,carrera,matricula):
        super().__init__(nombre,edad,tel)
        self.__carrera = carrera
        self.__matricula = matricula

    def setCarrera(self,carrera):
        self.__carrera = carrera
    
    def getCarrera(self):
        return self.__carrera
    
    def setMatricula(self,matricula):
        self.__matricula = matricula
    
    def getMatricula(self):
        return self.__matricula

    def Informar_carrera(self):
        print(f"Carrera {self.getCarrera()}")

    def Info_persona(self):
        print(f"Informacion de la persona {self.getNombre(), self.getEdad(), self.getTel(), self.getCarrera(), self.getMatricula()}")
    

class Docentes(Personas):
    def __init__(self,nombre,edad,tel,modalidad,num_empleado):
        super().__init__(nombre,edad,tel)
        self._modalidad = modalidad
        self._num_empleado = num_empleado
    
    def setModalidad(self,modalidad):
        self._modalidad = modalidad
    
    def getModalidad(self):
        return self._modalidad
    
    def setNum_empleado(self,num_empleado):
        self._num_empleado = num_empleado

    def getNum_empleado(self):
        return self._num_empleado
    
    def Informar_modalidad(self):
        print(f"Su modalidad es: {self.getModalidad()}")

    def Info_persona(self):
        print(f"Informacion de la persona {self.getNombre(), self.getEdad(), self.getTel(), self.getModalidad(), self.getNum_empleado()}")
    
    