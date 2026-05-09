from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    num1 = 18
    num2 = 12

    a = num1
    b = num2

    while b != 0:
        a, b = b, a % b

    hcf = a
    lcm = (num1 * num2) // hcf

    text = "Fun with Programming"
    reversed_text = text[::-1]

    factorials = {}

    for i in range(4, 9):
        fact = 1
        for j in range(1, i + 1):
            fact *= j
        factorials[i] = fact

    return render_template(
        'index.html',
        hcf=hcf,
        lcm=lcm,
        reversed_text=reversed_text,
        factorials=factorials
    )

if __name__ == '__main__':
    app.run(debug=True)
