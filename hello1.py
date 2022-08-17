from flask import Flask, jsonify,send_from_directory


app = Flask(__name__,static_folder='static/dist')
from ddb import * 


@app.route('/')
def hello():
	return app.send_static_file('hello.html')

@app.route('/dist/<path:path>')
def static_dist(path):
    # тут пробрасываем статику
    return send_from_directory("static/dist", path)

@app.route('/api/cars')
def cars():
	return jsonify({
        'cars': [
            'price',
            'body',
            'engine',
            'bbr',
           
        ]
    })


if __name__ == '__main__':
    app.run(debug=True)