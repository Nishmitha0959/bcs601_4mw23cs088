from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    factorial = None
    number = None

    if request.method == 'POST':
        number = int(request.form['number'])
        factorial = 1

        for i in range(1, number + 1):
            factorial *= i

    return render_template('index.html', factorial=factorial, number=number)

if __name__ == '__main__':
    app.run(debug=True)
