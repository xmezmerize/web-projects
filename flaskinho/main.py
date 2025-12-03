from flask import Flask, render_template, request
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy

# config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dados.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'someone secret'
db = SQLAlchemy()
db.init_app(app)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False, unique=False)
    email = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"<{self.nome}>"

# routes
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/filtros")
def filtros():
    dados = {'nome' : 'Pedrinho', 'profissão' : 'dev', 'projeto' : 'flaskinho'}
    return render_template('filtros.html', dados=dados, valor=3.14159265)

@app.route("/testes/<nome>")
def teste(nome):
    nome = escape(nome)
    frutas = ['Maçã', 'Banana', 'Pêra']
    return render_template('testes.html', nome="Pedro", idade=19, frutas=frutas)

@app.route("/imagem")
def image():
    return render_template('imagem.html')

@app.route("/formulario", methods=['GET', 'POST'])
def formulario():
    name = None
    email = None
    if request.method == "POST": #manda pro backend
        name = escape(request.form.get('nomeForm'))
        email = escape(request.form.get('emailForm'))
        if name and email: # manda pro banco
            novo_usuario = Usuario(nome=name, email=email)
            db.session.add(novo_usuario)
            db.session.commit()
    return render_template("formulario.html", name=name, email=email)

@app.route("/calculadora", methods=['GET', 'POST'])
def calculadora():
    calculo = None
    if request.method == "POST":
        peso = request.form.get('pesoForm', type=float)
        altura = request.form.get('alturaForm', type=float)
        if peso and altura:
            calculo = round((peso / altura ** 2), 2)
    return render_template("calculadora.html", calculo=calculo)

@app.route("/numeros", methods=["GET", "POST"])
def numeros():
    lista = []
    if request.method == "POST":
        num = request.form.get("numForm", type=str) 
        if num:
            for digito in num:  
                if digito.isdigit():
                    d = int(digito)
                    tipo = "Par" if d % 2 == 0 else "Impar"
                    lista.append((d, tipo))
    return render_template("raspagem_numeros.html", numeros=lista)

# servidor
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)