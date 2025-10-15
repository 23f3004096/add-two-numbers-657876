from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        if num1 and num2:
            result = int(num1) + int(num2)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)