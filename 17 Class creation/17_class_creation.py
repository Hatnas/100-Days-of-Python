
#### Class Cration ####

# Para creaor una clase se empieza con Class y se establece un constructor (def __init__ (self)
# self hace referencia a si mismo y los demas van a ser atributos de la clase
class User:
  def __init__ (self, user_id, user_name):
    self.user_id = user_id
    self.name = user_name
    self.followers = 0   # Puedo establecer un parametro por fuera de lso que estan en el constructor.

# Al crear un objeto tengo que completar los parametros de los atributos
# user_1 = User (1, "Leo")
user_1 = User("001", "Leo")

print (user_1.user_id)  # 001
print(user_1.name) # Leo
print(user_1.followers) # 0

