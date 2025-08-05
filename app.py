from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.json['expression']
    try:
        # Only allow safe characters
        allowed = "0123456789+-*/(). "
        if all(char in allowed for char in expression):
            result = eval(expression)
            return jsonify({'result': result})
        else:
            return jsonify({'result': 'Invalid Input'})
    except:
        return jsonify({'result': 'Error'})

if __name__ == '__main__':
    app.run(debug=True)
