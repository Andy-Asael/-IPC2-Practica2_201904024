import graphviz as gv
class cliente:
  def __init__(self, nombre, apellido, notelefono):
    self.nombre = nombre
    self.apellido = apellido
    self.notelefono = notelefono

class node:
  def __init__(self, cliente=None, next=None):
    self.cliente = cliente
    self.next = next

class node_de:
  def __init__(self, cliente=None, next=None, previous=None):
    self.cliente = cliente
    self.previous = previous
    self.next = next

class linked_list_de:

  def __init__(self, head=None):
    self.head = head
    self.last = head
    self.size = 0

  def insertar(self, cliente):
    if self.size == 0:
      self.head = node_de(cliente=cliente)
      self.last = self.head
    else:
      new_node = node_de(cliente=cliente, next=self.head)
      self.head.previous = new_node
      self.head = new_node
    self.size += 1

  def imprimir(self):
    if self.head is None:
      return
    node = self.head
    print(node.cliente.nombre, node.cliente.apellido, node.cliente.notelefono, end = "\n")
    while node.next:
      node = node.next
      print(node.cliente.nombre, node.cliente.nombre, node.cliente.apellido, node.cliente.notelefono, end = "\n")

  def buscar(self, notele):
    node = self.head
    if node.cliente.notelefono == notele:
        print("Nombre: ", node.cliente.nombre,"\nApellido: ", node.cliente.apellido,"\nNumero de Telefono: ", node.cliente.notelefono)
    else:
        print("Numero no existente")

  def recorrer(self):
        node = self.head
        while node.next != self.head:
            print(node.cliente)
            node = node.next
        print(node.cliente)

lista_de = linked_list_de()

while True:
    print("Bienvenido")
    print("1. Ingresar Nuevo contacto")
    print("2. Buscar Contacto")
    print("3. Visualizar Agenda")
    print("4. Salir")
    menu=int(input('Ingrese el número que desee: '))
    if menu==1:
        print("#################")
        nombrem = input("Ingrese nombre: ")
        apellidom = input("Ingrese Apellido: ")
        notelm = int(input("Ingrese no. de Teléfono: "))
        d1 = cliente(nombrem, apellidom, notelm)     
        lista_de.insertar(d1)
        print("El contacto se ha agregado exitosamente")
        lista_de.imprimir()
        print("\n")
    elif menu==2:
        print("##################")    
        numero= int(input("Ingrese el número a buscar: "))
        if lista_de.buscar(numero) == True:
            lista_de.recorrer()
            lista_de.imprimir()
    elif menu ==3:
        lista_de.imprimir()
        g1 = gv.Graph(format='jpg')
        g1.node("Agenda")
        imprimir = lista_de.imprimir()
        g1.node(imprimir)
        filename = g1.render(filename='img/g1',directory="C:/Users/andy/Desktop/", view=True) 

            
