from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
results = {}

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods =['POST'])
def result():
    global totalSubject
    totalSubject = request.form.get("subjects")

    return render_template('entries.html', fields= range(int(totalSubject)))

@app.route('/marks', methods = ['POST'])
def marks():
    resultss = {}
    name = request.form.get("name")
    for subnum in range(int(totalSubject)):
        subject = request.form.get('subjectName' + str(subnum))
        marks = request.form.get('marks' + str(subnum))
        resultss[subject]=marks 
    return render_template('result.html', name = name, resultss = resultss )

if __name__ == "__main__":
    app.run(debug=True)