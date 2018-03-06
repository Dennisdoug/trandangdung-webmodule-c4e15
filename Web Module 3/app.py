from flask import *

from models.service import Service

import mlab
mlab.connect()

app = Flask(__name__)



# service = Service(name="Hera",
#                     yob=1998,
#                     gender=0,
#                     height=160,
#                     phone="0969696969",
#                     address="Ha Noi",
#                     status=True)
# service.save()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:gender>')
def search(gender):
    services = Service.objects(gender=gender)
    return render_template('search.html', all_services=services)

@app.route('/admin')
def admin():
    services = Service.objects()
    return render_template('admin.html', services= services)

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects().with_id(service_id)
    if service_to_delete is None:
        return "Not found"

    service_to_delete.delete()
    return redirect(url_for("admin"))

@app.route('/new-service', methods=['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template('new-service.html')
    elif request.method == "POST":
        form = request.form

        name = form['name']
        yob = form['yob']
        phone = form['phone']

        new_service = Service(name=name,
                              yob=yob,
                              phone=phone,
                              gender=1,
                              height=170,
                              address='Ha Noi',
                              status=True
                              )
        new_service.save()

        return "Saved"

        return "{0} {1} {2} posted".format(name, yob, phone)

@app.route("/detail/<service_id>")
def detail(service_id):
    service_detail = Service.objects().with_id(service_id)
    return render_template("service_detail.html", detail=service_detail)



if __name__ == '__main__':
  app.run(debug=True)
