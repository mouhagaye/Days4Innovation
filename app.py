from flask import Flask ,render_template,request
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD'] = 'leavemealone'
app.config['MYSQL_DB'] = 'Days4Innovation'

mysql = MySQL(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/presentationDays4innovation")
def presentationDays4innovation():
    return render_template("presentationDays4innovation.html")

@app.route("/registration" , methods=['GET','POST'])
def registration():

    name = request.form.get("names")
    mail = request.form.get("mail")
    remarque = request.form.get("message")
    event = request.form.getlist('evenement')
    evenements = ",".join(event)

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO participant(nom,mail,remarque,evenements) VALUES (%s, %s, %s,%s)",(name,mail,remarque,evenements))
    mysql.connection.commit()
    cur.close

    return render_template("registration.html")


@app.route("/thx")
def thx():
    return render_template("thx.html")



if __name__ == "__main__":

    app.run()