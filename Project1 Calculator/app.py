from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/math", methods=["POST"])
def operation():
    try:
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
    except:
        r = "Please Enter Input"
    else:
        if operation == 'add':
            r = "Sum of " + str(num1) + " and " + str(num2) + " is: " + str(num1 + num2)
        elif operation == 'subt':
            r = "Difference between " + str(num1) + " and " + str(num2) + " is: " + str(num1 - num2)
        elif operation == 'multiply':
            r = "Product of " + str(num1) + " and " + str(num2) + " is: " + str(num1 * num2)
        elif operation == 'divide':
            if num2 == 0:
                if num1 == 0:
                    r = "Division of " + str(num1) + " and " + str(num2) + " is: Not Defined"
                else:
                    r = "Division of " + str(num1) + " and " + str(num2) + " is: Infinity"
            else:
                r = "Division of " + str(num1) + " and " + str(num2) + " is: " + str(num1 / num2)
    return render_template("results.html",result=r)

if __name__=="__main__":
    app.run(debug=True)