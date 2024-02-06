from flask import Flask, request, json
from db import Database
from validations import PayloadValidations

app = Flask(__name__)

token = 'TOKEN123'

@app.route("/")
def main():
    return "<p>Main Page</p>"

@app.route('/login', methods=['POST'])
def login():
    print('req',request.json)
    obj = request.json
    has_email = 'email' in obj.keys()
    has_password = 'password' in obj.keys()
    print('has_email', has_email, obj)
    print('has_password', has_password, obj)
    if('email' in obj.keys() and 'password' in obj.keys()):
        if (obj['email'] == 'email@email.com' and obj['password'] == '111111'):
                return { 'token': token }, 200
        else:
            return { 'message': 'wrong creds' }, 400
    else:
        return { 'message': 'send correct payload' }, 400
    

@app.route('/products', methods=['GET', 'POST'])
def products():
    # check if user has token
    token_sent = request.headers.get('Authorization')
    if(token_sent != token):
        return { 'message': 'Wrong Token' }
    else:
        d = Database()
        v = PayloadValidations()
        if request.method == 'GET':
            return d.get_products(), 200
        elif request.method == 'POST':
            valid_payload = v.validate_product(request.json)
            if valid_payload:
                items = d.add_product(request.json)
                return { 'data': items }, 200
            else:
                return { 'message': 'Wrong Payload' }, 400
        else:
            return { 'message': 'Method not supported' }, 404
        

# CRUD Operations Create, read, Update, Delete
        
@app.route('/products/<product_id>', methods=['GET', 'DELETE', 'PUT'])
def get_product(product_id):
    token_sent = request.headers.get('Authorization')
    if(token_sent != token):
        return { 'message': 'Wrong Token' }
    else:
        try:
            p_id = int(product_id)
            d = Database()
            v = PayloadValidations()
            if (request.method == 'GET'):
                return d.get_product_by_id(p_id), 200
            elif (request.method == 'PUT'):
                if(v.validate_product(request.json)):
                    return d.update_product(p_id, request.json), 200
                else: 
                    return { 'message': 'Payload Not Valid '}, 400
            elif (request.method == 'DELETE'):
                d.delete_product(p_id)
                return { 'message': 'Product Deleted' }, 200
            else:
                return { 'message': 'Method not allowed'}, 400
        except:
            return { 'message': 'Id is not a Number '}, 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)