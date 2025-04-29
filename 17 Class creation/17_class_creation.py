
#### Class Cration ####

# Para creaor una clase se empieza con Class y se establece un constructor (def __init__ (self)
# self hace referencia a si mismo y los demas van a ser atributos de la clase
class User:
  def __init__ (self, user_id, user_name):
    self.user_id = user_id
    self.name = user_name
    self.followers = 0   # Puedo establecer un parametro por fuera de lso que estan en el constructor.
    self.following = 0

  def follow (self,user):    # Al poner self entre parentesis en la funcion, modifico los atributos de la clase
      user.followers += 1
      self.following += 1

# Al crear un objeto tengo que completar los parametros de los atributos
# user_1 = User (1, "Leo")
user_1 = User("001", "Leo")
user_2 = User("002", "Lau")

print (user_1.user_id)  # 001
print(user_1.name) # Leo
print(user_1.followers) # 0

user_1.follow(user_2)    # al seguir user_1 a u_2 se modificaron los atributos de los dos
print (user_1.followers)
print (user_1.following)
print (user_2.followers)
print (user_2.following)