from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/id/<int:id>', methods = ['GET'])
def GET_API(id):
    if id >= 5000 : return '{\'result\' : true}'
    else : return '{\'result\' : false}'
    
@app.route('/id', methods = ['POST'])
def POST_API():
    params = request.get_json()
    return jsonify(params['name'])
    

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)