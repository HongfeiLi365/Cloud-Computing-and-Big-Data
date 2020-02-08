from flask import Flask, escape, request

app = Flask(__name__)

seed=0

@app.route('/', methods=['POST', 'GET'])
def hello():
    global seed
    if request.method =='POST':
        req_data = request.get_json(force=True)
        seed = req_data['num']
        return 'Received:'+ str(seed)
        
    if request.method =='GET':
        return str(seed)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)