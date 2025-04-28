'''In questo progetto, dovrai scrivere il codice per un sistema di 
gestione e creazione dei corsi ITS.
Il sistema gestisce aule ed edifici (Parte 1), persone -studenti e 
docenti- in gruppi di studio (parte 2), e corsi (parte 3).
 
### Classe Room:
La classe Room rappresenta un'aula. Ogni aula ha un ID (id), un piano 
(floor), un numero di posti (seats) e un'area (area). L'area è calcolata 
come il doppio dei posti.
- Metodi:
    - get_id(): Restituisce l'ID dell'aula.
    - get_floor(): Restituisce il piano dell'aula.
    - get_seats(): Restituisce il numero di posti dell'aula.
    - get_area(): Restituisce l'area dell'aula.'''

class Room:
    
    def __init__(self, id, floor, seats):
        self.id = id
        self.floor = floor
        self.seats = seats
        self.area = seats*2
    
    def get_id(self):
        return self.id

    def get_floor(self):
        return self.floor

    def get_seats(self):
        return self.seats

    def get_area(self):
        return self.area
    
'''### Classe Building:
La classe Building rappresenta un edificio. Ogni edificio ha un nome 
(name), un indirizzo (address), un intervallo di piani (floors), e una 
lista di aule (rooms).
- Metodi:
    - get_floors(): Restituisce l'intervallo di piani dell'edificio.
    - get_rooms(): Restituisce la lista delle aule nell'edificio.
    - add_room(room): Aggiunge un'aula all'edificio, solo se il piano 
    dell'aula è compreso nell'intervallo di piani dell'edificio.
    - area(): Restituisce l'area totale dell'edificio sommando le aree 
    di tutte le aule.
'''

class Building:
    
    def __init__(self, name, address, floors, rooms=None):
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms = []
    
    def get_floors(self):
        return self.floors

    def get_rooms(self):
        return self.rooms

    def add_room(self, room):
        for room_ in self.rooms:
            if room_.id == room.id:
                return False
        if room.floor >= self.floors[0] and room.floor <= self.floors[1]:
            self.rooms.append(room)
        return self.rooms

    def area(self):
        tot_area: int = 0
        for room in self.rooms:
            tot_area += room.get_area()
        return tot_area
    

'''Classi Person, Student e Lecturer:
La classe Person rappresenta una persona con un codice fiscale (cf), un nome (name), un cognome (surname), un'età (age).
Le classi Student e Lecturer ereditano da Person.
Uno studente è associato ad un gruppo di studio (group). Quindi, la classe Student ha il seguente metodo:
    - set_group(group): Associa un gruppo di studio allo studente'''

class Person:

    def __init__(self, cf, name, surname, age):

        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age

class Student(Person):

    def set_group(group):

        Student.group = group

#class Lecturer(Person):

    #def add_lecturer(self):

class Group:

    def __init__(self, name, limit, students, lecturers):

        self.name = name
        self.limit = limit
        self.students = []
        self.lecturers = []

    def get_name(self):        
        return self.name
    
    def get_limit(self):        
        return self.limit
    
    def get_students(self):        
        return self.students
    
    def get_limit_lecturers(self):
        limit: int = len(self.students) // 10 + 1
        return limit
    
    def add_student(self, student):
        if len(self.students) < self.limit:
            self.students.append(student)

    def add_lecturer(self, lecturer):
        if len(self.lecturers) < self.get_limit_lecturers:
            self.lecturers.append(lecturer)



''' 
Classe Group:
La classe Group rappresenta un gruppo di studio. Ogni gruppo ha un nome (name), un limite di studenti (limit), 
una lista di studenti (students) e una lista di docenti (lecturers).
- Metodi:
    - get_name(): Restituisce il nome del gruppo
    - get_limit(): Restituisce il limite di studenti nel gruppo
    - get_students(): Resituisce la lista di studenti nel gruppo
    - get_limit_lecturers(): Restituisce il limite di docenti nel gruppo. E' consentito 1 docente ogni 10 
    studenti. Il gruppo può avere almeno 1 docente, anche se ci sono meno di 10 studenti.
    - add_student(student): Aggiunge uno studente al gruppo, solo se il limite per gli studenti non è stato 
    raggiunto.
    - add_lecturer(lecturer): Aggiunge un docente al gruppo, solo se il limite per i docenti non è stato raggiunto.'''


'''Classe Course:
La classe Course rappresenta un corso accademico. Ogni corso ha un nome (name) e una lista di gruppi (groups).
- Metodi:
    - register(student): Registra uno studente nel primo gruppo disponibile che non ha ancora raggiunto il 
    limite di studenti.
    - get_groups(): Restituisce la lista dei gruppi nel corso.
    - add_group(group): Aggiunge un gruppo al corso.'''

class Course:

    def __init__(self, name, groups):

        self.name = name
        self.groups = groups

    def get_groups(self):
        return self.groups
    
    def add_group(self, group):
        self.group.append(group)
    
    def register(self, student):
        for group in self.groups:
            if len(group) < group.limit:
                group.append(student)
                pass
