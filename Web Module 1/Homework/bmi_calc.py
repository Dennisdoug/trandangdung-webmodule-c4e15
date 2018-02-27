from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:x>/<int:y>')
def bmi(x,y):
    n = x * 10000 / y ** 2
    if n < 16:
        result = "Severly Underweight"
    elif n < 18.5:
        result = "Underweight"
    elif n < 25:
        result = "Normal"
    elif n < 30:
        result = "Overweight"
    else:
        result = "Obese"
    return ("Your BMI result is: " + str(n) + "- You're " + result)

@app.route('/bmicalc/<int:x>/<int:y>')
def bmicalc(x,y):
    bmi = x * 10000 / y ** 2
    if bmi < 16:
        result = "Severly Underweight"
    elif bmi < 18.5:
        result = "Underweight"
    elif bmi < 25:
        result = "Normal"
    elif bmi < 30:
        result = "Overweight"
    else:
        result = "Obese"
    return render_template('bmi_calc.html', result = result, bmicalc = str(bmi))






if __name__ == "__main__":
    app.run(debug=True)
