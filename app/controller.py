from flask import jsonify, request
from app import app
from service import Service

service = Service()

@app.route('/patient', methods = ['POST'])
def add_patient() :
    payload = request.json
    try:
        service.add_patient(payload)
        return jsonify("Added successfully")
    except ValueError as e:
        return jsonify("Error: {}".format(str(e))), 400
    

@app.route('/all_patient', methods = ['GET'])
def get_all_patient() : 
    response = service.get_all_patient()
    return response
    

@app.route('/patient/<id>', methods = ['GET'])
def get_patient(id) :
    response = service.get_patient(id)
    return response

@app.route('/remove_patient/<id>',methods = ['DELETE'])
def remove_patient(id) : 
    response = service.remove_patient(id)   
    return jsonify(response)

@app.route('/update_patient/<id>',methods = ['PUT'])
def update_patient(id) : 
    payload = request.get_json()
    response = service.update_patient(id,payload) 
    return jsonify(response)

if __name__ == '__main__':
    app.run()