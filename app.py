from flask import Flask, render_template, request
from funcoes import analisar_anemia

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    resultado = ""

    if request.method == "POST":
        sexo = request.form["sexo"].lower()

        valores = {
            "RBC": float(request.form["RBC"]),
            "HGB": float(request.form["HGB"]),
            "HT": float(request.form["HT"]),
            "VCM": float(request.form["VCM"]),
            "HCM": float(request.form["HCM"]),
            "CHCM": float(request.form["CHCM"]),
            "RETIC": float(request.form["RETIC"]),
            "FERRO": float(request.form["FERRO"]),
            "B12": float(request.form["B12"]),
            "FOLATO": float(request.form["FOLATO"])
        }

        resultado = analisar_anemia(sexo, valores)

    return render_template("index.html", resultado=resultado)

app.run(debug=True)