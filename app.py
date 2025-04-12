from flask import Flask, render_template, request, session, redirect
import random

app = Flask("Forca")
app.secret_key = "segredo"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/comecar", methods = ["POST"])
def comecar():
        jogador = request.form["jogador"]
        session["jogador"] = jogador 
        session["palavra"] = sortear_palavra()
        session["numero_tentativas"] = 6
        session["letras_corretas"] = []
        session["letras_erradas"] = []
        return redirect("/jogo")

@app.route("/jogo", methods = ["GET", "POST"])
def jogo():
        palavra = session["palavra"]
        palavra_oculta = ""

        if request.method == "POST":
            letra = request.form["letra"].upper()
            
            if letra in palavra:
                session["letras_corretas"].append(letra)
       
        for letra in palavra: 
            if letra in session["letras_corretas"]:
               palavra_oculta += letra 
            else: 
                palavra_oculta += "_ "

        return render_template ("jogo.html", palavra_oculta = palavra_oculta)











def sortear_palavra():
    with open("palavras.txt", "r") as file:
       palavras = file.read().splitlines()
    return random.choice(palavras).upper()
       
















app.run(debug=True)