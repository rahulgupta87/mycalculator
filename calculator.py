from flask import Flask, request
app = Flask(__name__)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    operator = data.get("operator")
    operand1 = data.get("operand1")
    operand2 = data.get("operand2")
    if operator == "add":
        result = operand1 + operand2
    elif operator == "subtract":
        result = operand1 - operand2
    elif operator == "multiply":
        result = operand1 * operand2
    elif operator == "divide":
        result = operand1 / operand2
    return {"result": result}

if __name__ == '__main__':
    app.run(debug=True)
