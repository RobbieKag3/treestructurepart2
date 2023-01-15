from flask import Flask,render_template
app=Flask(__name__,template_folder='templates')
@app.route('/oaktree')
def showoaktree():
    return render_template('oak.html')
@app.route('/longleafpine')
def showlongleaftree():
    return render_template('longleafpine.html')
@app.route('/coconut')
def showcoconuttree():
    return render_template('coconut.html')
@app.route('/sugarpine')
def showsugartree():
    return render_template('sugarpine.html')
app.run(debug=True)