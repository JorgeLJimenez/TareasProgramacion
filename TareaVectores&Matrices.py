import math #importo la librería math

class Vector: #defino la clase Vector

  def __init__(self, x, y, z): #metodos de la forma __funcion__(...) son llamados métodos especiales.
    self.x = x #defino las variables de clase
    self.y = y
    self.z = z
    self.magnitud = (self.x**2 + self.y**2)**0.5
    self.angulo = math.atan2(self.y, self.x)

  def __str__(self):
    respuesta = "( " + str(self.x) + " , " + str(self.y) + " , " + str(self.z) + " )"
    return(respuesta)
    #este __srt__ viene de cadena, y es lo que quiero que saque al imprimir
    #sirve para que al print un vector, salga un vector y no algo raro
    #los dos def primeros son metodos especiales, para hacer cosas interesantes
  def __add__(self,otro):
    x = self.x + otro.x
    y = self.y + otro.y
    z = self.z + otro.z
    return(Vector(x,y,z))

  def __sub__(self, otro):
    return Vector(self.x - otro.x, self.y - otro.y, self.z - otro.z)

  def __mul__(self,otro): # este metodo magico 'mul' reconoce la operacion vec1*2.
    if type(otro)==type(self):
      x = self.x*otro.x
      y = self.y*otro.y
      z = self.z*otro.z
      return(x+y+z)
    else:
      x = otro*self.x
      y = otro*self.y
      z = otro*self.z
      return(Vector(x,y,z))

  def __rmul__(self, otro): # 
    if type(otro)==type(self):
      x = self.x*otro.x
      y = self.y*otro.y
      z = self.z*otro.z
      return(x+y+z)
    else:
      x = otro*self.x
      y = otro*self.y
      z = otro*self.z
      return(Vector(x,y,z))

vec1 = Vector(1,2,3)
vec2 = Vector(6,5,4)

print("vec1 = "+str(vec1))
print("vec2 = "+str(vec2))
print("vec1 + vec2 = "+str(vec1+vec2))
print("vec1 - vec2 = "+str(vec1-vec2))
print("vec1 * vec2 = "+str(vec1*vec2))
escalar1=2
print("vec1 * "+str(escalar1)+" = "+str(vec1*escalar1))
escalar2=-3
print(str(escalar2)+" * vec1 = "+str(escalar2*vec1))

#
#
#MANIPULACIÓN DE MATRICES
#
#

print("\n")

class Matriz2x2:
  def __init__(self, lista):
    self.a11=lista[0][0]
    self.a12=lista[0][1]
    self.a21=lista[1][0]
    self.a22=lista[1][1]

  def __str__(self):
    respuesta = "| "+str(self.a11)+"  "+str(self.a12)+" |\n| "+str(self.a21)+"  "+str(self.a22)+" |"
    return(respuesta)

  def __add__(self,otro):
    a11 = self.a11 + otro.a11
    a12 = self.a12 + otro.a12
    a21 = self.a21 + otro.a21
    a22 = self.a22 + otro.a22
    return(Matriz2x2([[a11,a12],[a21,a22]]))

  def __sub__(self,otro):
    a11 = self.a11 - otro.a11
    a12 = self.a12 - otro.a12
    a21 = self.a21 - otro.a21
    a22 = self.a22 - otro.a22
    return(Matriz2x2([[a11,a12],[a21,a22]]))

  def __mul__(self,otro):
    if type(otro)==type(self):
      return("La multiplicación entre matrices se implementará pronto al programa.")
    else:
      a11 = self.a11*otro
      a12 = self.a12*otro
      a21 = self.a21*otro
      a22 = self.a22*otro
      return(Matriz2x2([[a11,a12],[a21,a22]]))

  def __rmul__(self,otro):
    if type(otro)==type(self):
      return("La multiplicación entre matrices se implementará pronto al programa.")
    else:
      a11 = self.a11*otro
      a12 = self.a12*otro
      a21 = self.a21*otro
      a22 = self.a22*otro
      return(Matriz2x2([[a11,a12],[a21,a22]]))

  def columna_iesima(self,M,i):
    lista=[[M.a11,M.a12],[M.a21,M.a22]]
    return("|"+str(lista[0][i])+"|\n|"+str(lista[1][i])+"|")

L1 = [[1,2],[3,4]]
L2 = [[10,20],[30,40]]

M1 = Matriz2x2(L1)
M2 = Matriz2x2(L2)

print("Matriz M1=")
print(M1)
print("Matriz M2=")
print(M2)
print("M1+M2=")
print(M1+M2)
print("M2-M1=")
print(M2-M1)
c1=2
print("M1*"+str(c1)+"=")
print(M1*c1) #funciona con el mul
c2=-1
print(str(c2)+"*M1=")
print(c2*M1) #funciona con el rmul
i=0 #indice de la columna en programación. En matemáticas sería i+1
print(str(i+1)+"-ésima columna de la matriz M1:")
print(M1.columna_iesima(M1,i))
i=1 #indice de la columna en programación. En matemáticas sería i+1
print(str(i+1)+"-ésima columna de la matriz M1:")
print(M1.columna_iesima(M1,i))