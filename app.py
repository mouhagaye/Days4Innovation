from flask import Flask ,render_template,request,redirect,url_for
import mysql.connector



app = Flask(__name__)

config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'Days4Innovation'
    }


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/presentationDays4innovation")
def presentationDays4innovation():
    return render_template("presentationDays4innovation.html")

@app.route("/registration" , methods=['GET','POST'])
def registration():
    day1 = ['D4I2020', 'Oz innovation Stories', 'Orange Fab Stories', 'Intrapreneur Factory', 'koori- Design thinking']
    day2 = ['Open innovation en Afrique', 'AI and Data innovation pour telcos', 'Innovation et Formation', 'Présentation des linebreakers', 'Visite Orange Digital Center']
    debut = [' 11:00',' 10:15',' 12:00',' 14:30',' 15:30',' 09:00',' 11:00',' 10:00',' 14:30',' 15:30']
    duree = [15,105,60,60,60,75,75,60,60,60]

    titre = day1 + day2


    name = request.form.get("names")
    mail = request.form.get("mail")
    remarque = request.form.get("message")
    events = request.form.getlist('evenement')
    evenements = ",".join(events)

    if mail is not None:
        connection = mysql.connector.connect(**config)
        cur = connection.cursor(buffered = True)
        cur.execute("INSERT INTO participant(nom,mail,remarque,evenements) VALUES (%s, %s, %s,%s)",(name,mail,remarque,evenements))
        cur.execute("SELECT* FROM participant")
        connection.commit()
        connection.close()


    if request.method == 'POST':
        return redirect(url_for('thx'))



    return render_template("registration.html")

@app.route("/thx")
def thx():
    return render_template("thx.html")



if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)