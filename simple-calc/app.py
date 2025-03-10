from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 == 0:
                    result = "Error: Cannot divide by zero!"
                else:
                    result = num1 / num2
        except ValueError:
            result = "Error: Please enter valid numbers!"

    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)