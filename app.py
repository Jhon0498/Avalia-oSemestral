from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para armazenar os professores cadastrados
professores = []

# Rota principal
@app.route("/")
def index():
    return render_template("index.html")

# Rota para exibir avaliação semestral com nome e prontuário
@app.route("/avaliacao_semestral")
def avaliacao_semestral():
    nome = "Jhonatan Mendes Morão"
    prontuario = "PTO3026931"
    return render_template("avaliacao_semestral.html", nome=nome, prontuario=prontuario)

# Rota para Cadastro de Professores
@app.route("/professores", methods=["GET", "POST"])
def professores_route():
    global professores
    if request.method == "POST":
        nome = request.form["nome"]
        disciplina = request.form["disciplina"]
        # Adiciona o novo professor à lista
        professores.append({"nome": nome, "disciplina": disciplina})
        return redirect(url_for("professores_route"))  # Redireciona para a lista de professores

    # Exibe o formulário de cadastro e a lista de professores cadastrados
    return render_template("professores.html", professores=professores)

# Rota para módulos não disponíveis
@app.route("/<path:rota_nao_existente>")
def nao_disponivel(rota_nao_existente):
    return render_template("nao_disponivel.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
