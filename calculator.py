from flask import Flask , request , render_template , jsonify 

app = Flask(__name__) 

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/operation" , methods = ['POST'])
def ops():
    if (request.method == 'POST'):
        operator = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        if(operator == 'add'):
            res = num1 + num2
            result = f"the sum of {num1} and {num2} is {res} "
        if(operator == 'subtract'):
            res = num1 - num2
            result = f"the subtraction of {num1} and {num2} is {res} "
        if(operator == 'multiply'):
            res = num1 * num2
            result = f"the multiplication of {num1} and {num2} is {res} "
        if(operator == 'divide'):
            res = num1 / num2
            result = f"the sum of {num1} and {num2} is {res} "
        if(operator == 'log'):
            import math
            res = math.log(num1,num2)
            result = f"the sum of {num1} and {num2} is {res} "

        return render_template('results.html' , result = result)


@app.route("/operation_postman" , methods = ['POST'])
def ops1():
    if (request.method == 'POST'):
        operator = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        if(operator == 'add'):
            res = num1 + num2
            result = f"the sum of {num1} and {num2} is {res} "
        if(operator == 'subtract'):
            res = num1 - num2
            result = f"the subtraction of {num1} and {num2} is {res} "
        if(operator == 'multiply'):
            res = num1 * num2
            result = f"the multiplication of {num1} and {num2} is {res} "
        if(operator == 'divide'):
            res = num1 / num2
            result = f"the sum of {num1} and {num2} is {res} "
        if(operator == 'log'):
            import math
            res = math.log(num1,num2)
            result = f"the sum of {num1} and {num2} is {res} "

        return jsonify(result)

if __name__ == "__main__":
    app.run(host= "0.0.0.0")