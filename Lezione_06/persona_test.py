
'''from persona import Persona

Matteo: Persona = Persona("Matteo", "Fabbri", 23)
print(Matteo)
Matteo.displayData()'''

from persona2 import Persona

mf: Persona = Persona()
#mf.displayData()
mf.setName("Matteo")
mf.setLastname("Fabbri")
mf.setAge(23)
mf.displayData()
print(mf.getName())
print(mf.getLastname())
print(mf.getAge())
