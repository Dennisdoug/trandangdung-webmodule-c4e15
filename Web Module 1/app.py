from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return "Hello C4E15"

@app.route('/sayhi/<name>')
def sayhi(name):
    return "Hello " + name

@app.route('/sum/<int:x>/<int:y>')
def sum(x,y):
    # z = int(x)+int(y)
    return str(x + y)

@app.route('/html')
def heading():
    return "<h1>Motherfucker</hi>"

@app.route('/blog')
def blog():
    article_name = "Thơ CC"
    posts = {
    "content": "abcdxyz",
    "author": "Dung"
    }

    return render_template('blog.html',
                article_title = article_name,
                posts = posts)

@app.route('/user/<user_name>')
def user(user_name):
    article_name = "Secret profiles"
    posts = [
    {
    "name": "Hoang Tu Mua",
    "age": "22",
    "sex": "male",
    "hobbies":"Fuck, Fap"
    }
    ]

    return render_template("fbuser.html", article_title = article_name, posts = posts, user_name = "htm")

if __name__ == "__main__":
    app.run(debug=True)
