import os
from dotenv import load_dotenv
import pymongo
from flask import Flask, request
app = Flask(__name__)

@app.route("/healthCheck", methods=["GET"])
def healthCheck():
    print('performing health check...')
    return "ok"

#### exposing flask api with path /calculate and method type POST
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

    #### inserting records in mongodb
    ## loading monogdb user and password fron env
    load_dotenv()
    mongoUser = os.getenv("MONGOUSER")
    mongoPwd = os.getenv("MONGOPWD")
    mongoDb = 'test'
    mongoCollection = 'calculator-records'
    
    ## mongodb client to establish connection with the db cluster
    mongoClient = pymongo.MongoClient("mongodb+srv://"+mongoUser+":"+mongoPwd+"@cluster-dev.a8h29.mongodb.net/?retryWrites=true&w=majority")
    db = mongoClient[mongoDb]
    collection = db[mongoCollection]

    image = {}
    image['operand1'] = operand1
    image['operator'] = operator
    image['operand2'] = operand2
    image['result'] = result
    
    collection.insert_one(image)
    
    mongoClient.close()
    print('Data successfully inserted in mongo...')

    return {"result": result}

if __name__ == '__main__':
    app.run(debug=True)

