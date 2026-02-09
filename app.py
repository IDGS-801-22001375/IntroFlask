from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect
import forms
import math

app = Flask(__name__)

app.secret_key = "6hK2p4;_L#(*CCckH))*26uVm6N(H+"
csrf = CSRFProtect()


## RUTA DISTANCIA ENTRE DOS PUNTOS
@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    distancia = 0
    if request.method == "POST":
        x1 = float(request.form.get("x1"))
        y1 = float(request.form.get("y1"))
        x2 = float(request.form.get("x2"))
        y2 = float(request.form.get("y2"))
        distancia = round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

    return render_template("distancia_puntos/distancia_puntos.html", distancia=distancia)

## RUTA TICKET CINEPOLIS
@app.route("/ticket_cinepolis", methods=["GET", "POST"])
def ticket_cinepolis():
    form = forms.TicketCinepolis(request.form)
    ticket_cinepolis = ""
    if request.method == "POST" and form.validate():

        cantidad_boletos = form.cantidad_boletos.data
        cantidad_compradores = form.cantidad_compradores.data
        usa_tarjeta = form.es_con_tarjeta_cineco.data

        if cantidad_boletos > cantidad_compradores * 7:
            ticket_cinepolis = "No se pueden comprar más de 7 boletos por persona."
        else:
            precio_boleto = 12
            subtotal = cantidad_boletos * precio_boleto

            if cantidad_boletos > 5:
                descuento = 0.15
            elif 3 <= cantidad_boletos <= 5:
                descuento = 0.10
            else:
                descuento = 0

            total = subtotal * (1 - descuento)

            if usa_tarjeta == 'si':
                total *= 0.90

            ticket_cinepolis = f"$ {total:.2f}"

    return render_template("cinepolis/cinepolis.html", form=form, precio_ticket_cinepolis=ticket_cinepolis)

@app.route("/")
def index():
    titulo = "Flask IDGS-801"
    lista = ["Juan", "Mario", "Pedro", "Dario"]
    return render_template("index.html", titulo = titulo, lista = lista)

@app.route("/operasBas", methods=["GET", "POST"])
def operasBas():
    n1=0
    n2=0
    rest=0
    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        rest = float(n1) + float(n2)
    return render_template("operasBas.html", n1=n1, n2=n2, rest=rest)

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    n1 = request.form.get("n1")
    n2 = request.form.get("n2")
    tem = float(n1) + float(n2)
    return f"La suma es: {tem}"

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

@app.route("/usuarios", methods=["GET", "POST"])
def usuarios():
    mat=0
    nom=""
    apa=""
    ama=""
    correo=""
    usuarios_class=forms.UserForm(request.form)
    if request.method == "POST" and usuarios_class.validate():
        mat = usuarios_class.matricula.data
        nom = usuarios_class.nombre.data
        apa = usuarios_class.apePaterno.data
        ama = usuarios_class.apeMaterno.data
        correo = usuarios_class.correo.data
        mensaje='Bienvenido {}'.format(nom)
        flash(mensaje)
    return render_template("usuarios.html",  form=usuarios_class, mat=mat, nom=nom, apa=apa, ama=ama, correo=correo)

@app.route("/hola")
def hola():
    return "¡Hola mundo!"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola, {user}"

@app.route("/numero/<int:n>")
def numero(n):
    return f"<h1>El número es: {n}</h1>"

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"<h1>¡Hola, {username}! Tu ID es: {id}</h1>"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"<h1>La suma es: {n1 + n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:param>")
def func(param = "Juan"):
    return f"<h1>¡Hola, {param}!</h1>"

@app.route("/operas")
def operas():
    return '''
        <form>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            </br>
            <label for="name">apepaterno:</label>
            <input type="text" id"name" name="name" required>
        </form>
        '''

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)
