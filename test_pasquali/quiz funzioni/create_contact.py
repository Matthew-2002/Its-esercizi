def create_contact(
        nome: str, 
        email: str=None, 
        telefono: int=None
        )-> dict[str:any]:
    contatto: dict[str:any] = {}
    contatto["profile"] = nome
    if email != None:
        contatto["email"] = email
    else:
        contatto["email"] = None
    if telefono != None:
        contatto["telefono"] = telefono
    else:
        contatto["telefono"] = None
    return contatto

def update_contact(
        contact, 
        agg_nome: str=None, 
        **kwargs
        )-> dict[str:any]:
    if agg_nome != None:
        contact["profile"] = agg_nome
    if "email" in kwargs:
        contact["email"] = kwargs["email"]
    if "telefono" in kwargs:
        contact["telefono"] = kwargs["telefono"]
    return contact


contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))
