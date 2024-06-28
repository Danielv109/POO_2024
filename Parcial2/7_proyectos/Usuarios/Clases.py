class Usuarios:
    def __init__(self,nombre,direccion,tel):
        self.nombre = nombre
        self.direccion = direccion
        self.tel = tel

    def setNombre(self,nombre):
        self.nombre = nombre
    
    def getNombre(self):
        return self.nombre
    
    def setDireccion(self,direccion):
        self.nombre = direccion
    
    def getDireccion(self):
        return self.direccion
    
    def setTel(self,tel):
        self.nombre = tel
    
    def getTel(self):
        return self.tel
    
    def info_usuario(self):
        print(f"Nombre {self.getNombre()}  con la direccion {self.getDireccion()} y el telefono {self.getTel()}")

class Clientes(Usuarios):
    def __init__(self,nombre,direccion,tel,num_cliente):
        super().__init__(nombre,direccion,tel)
        self.__num_cliente = num_cliente

    def setNum_cliente(self,num_cliente):
        self.__num_cliente = num_cliente

    def getNum_cliente(self):
        return self.__num_cliente
    
    def info_usuario(self):
        return super().info_usuario(f"Nombre {self.getNombre()}  con la direccion {self.getDireccion()} y el telefono {self.getTel()} con el numero de cliente {self.getNum_cliente()}")
    
class Empleados(Usuarios):
    def __init__(self,nombre,direccion,tel,salario,num_empleado,tipo):
        super().__init__(nombre,direccion,tel)
        self._salario = salario
        self._num_empleado = num_empleado
        self._tipo = tipo

    def setSalario(self,salario):
        self._salario = salario
    
    def getSalario(self):
        return self._salario
    
    def setNum_empleado(self,num_empleado):
        self._num_empleado = num_empleado
    
    def getNum_empleado(self):
        return self._num_empleado
    
    def setTipo(self,tipo):
        self._tipo = tipo
    
    def getTipo(self):
        return self._tipo
    
    def info_usuario(self):
        return super().info_usuario(f"Nombre {self.getNombre()}  con la direccion {self.getDireccion()} y el telefono {self.getTel()} con el salario de {self.getSalario()} y su numero de empleado es {self.getNum_empleado()} y con un tipo {self.getTipo()}")
    

    
    
    
