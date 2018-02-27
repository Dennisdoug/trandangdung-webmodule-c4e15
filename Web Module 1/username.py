from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def user(username):
    users = {
            "huy":
                {
                    "name": "Nguyen Quang Huy",
                    "age": 29,
                    "work": "Techkids"
                },

            "tuananh":
                {
                    "name": "Huynh Tuan Anh",
                    "age": 22,
                    "work: Techkids"
                

            "dung":
                {
                    "name": "Tran Dang Dung",
                    "age": 22,
                    "work": "Unemployed"
                }
            }

    if username in users:
        return render_template('username.html',
            name = users[username]["name"],
            age = users[username]["age"],
            work = users[username]["work"])
    else:
        return "Not_found"



if __name__ == '__main__':
app.run(debug=True)
