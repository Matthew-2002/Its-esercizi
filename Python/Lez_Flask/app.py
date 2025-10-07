from flask import Flask, url_for

app: Flask = Flask(__name__)

@app.route('/')
def home() -> str:
    return 'HelloWorld!'




#Creare un percorso /user/<nome> che restituisca “Benvenuto, <nome>!”.
#
#    Testare con nomi diversi nell’URL.


@app.route('/user/<string:username>')
def show_user_profile(username: str):
    return f"Benvenuto {username}"

#Definire /square/<int:n> che ritorni il quadrato di n.

@app.route('/square/<int:n>')
def square(n: int) -> int:
    return f'{n**2}'

#Creare /sum/<int:a>/<int:b> che restituisca la somma dei due numeri.

@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int) -> int:
    return f'{a + b}'


#Generazione link interni
#    Usare url_for per creare automaticamente i link alle route definite, ed esporli in una pagina principale (homepage con link a /about, /user/..., ecc.).

#Navigazione dinamica
#    Creare una pagina con elenco utenti fittizi e i relativi link ai loro profili generati con url_for.

#Mini blog
#    Definire route /post/<int:id> che restituisca un articolo fittizio.
#    Creare una pagine /posts con un elenco di post e i relativi link agli articoli generati tramite url_for.


