from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

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
    app.run(debug=True)
