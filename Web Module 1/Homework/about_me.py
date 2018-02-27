from flask import Flask, render_template
import os
from flask import Flask, redirect
app = Flask(__name__)

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/school')
def school():
    return redirect("http://techkids.vn", code=302)

if __name__ == "__main__":
    app.run(debug=True)
