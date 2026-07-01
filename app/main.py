from flask import Flask, render_template, request, redirect, flash, url_for, session

app = Flask(__name__)
app.secret_key = "chave_secreta"
filmes = ['Barbie Escola de Princesas', 'Barbie e o Castelo Mágico', 'Barbie e as Sapatilhas Mágicas']
session['filmes'] = filmes

@app.route("/")
def index():
    filmes = session.get("filmes", [])
    return render_template("index.html", filmes=filmes)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    titulo = request.form.get("titulo")
    filmes = session.get("filmes", [])

    if titulo in filmes:
        flash('Esse filme já foi favoritado')
        return redirect(url_for("index"))

    filmes.append(titulo)
    session["filmes"] = filmes

    return redirect(url_for("index"))

@app.route("/remover/<int:indice>")
def remover(indice):
    filmes = session.get("filmes", [])

    if 0 <= indice < len(filmes): #verificando se o indidce tá dentro do tamanho da lista
        filmes.pop(indice)
        session["filmes"] = filmes

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)


@app.route('/sucesso')
def sucesso():
    return flash