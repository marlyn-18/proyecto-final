from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    expression = ""
    if request.method == "POST":
        btn = request.form.get("btn")
        expression = request.form.get("expression", "")

        if btn == "C":
            expression = ""
        elif btn == "=":
            try:
                allowed_chars = "0123456789+-*/.() "
                if all(char in allowed_chars for char in expression):
                    result = str(eval(expression))
                    expression = result
                else:
                    expression = "Error"
            except Exception:
                expression = "Error"
        else:
            expression += btn

    return render_template("index.html", expression=expression)

if __name__ == "__main__":
    app.run(debug=True)
