from flask import Flask ,render_template,request,redirect,url_for
import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from ics import Calendar, Event
from datetime import timedelta

def read_creds():
    user = passw = ""
    with open("credentials.txt", "r") as f:
        file = f.readlines()
        user = file[0].strip()
        passw = file[1].strip()

    return user, passw


email_user ,email_password = read_creds()

app = Flask(__name__)


config = {
        'user': 'root',
        'password': 'root',
        'host': 'localhost',
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
    duree = [15,105,60,60,60,60,60,60,60,60]


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


    for event in events:

        i = titre.index(event)
        if i < 4 :
            day = "2020-12-07"
        else:
            day = "2020-12-08"


        start = day+debut[i]
        duration = duree[i]

        c = Calendar()
        e = Event(location="Sonatel",duration=timedelta(0,0,0,0,duration))
        e.name = event
        e.begin = start
        c.events.add(e)
        c.events
        # [<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
        with open('my.ics', 'w') as my_file:
            my_file.writelines(c)
        # and it's done !

        if mail is not None:
            email_send = mail
            try:

                subject = event

                msg = MIMEMultipart()
                msg['From'] = email_user
                msg['To'] = email_send
                msg['Subject'] = subject

                body = 'Merci de votre participation a Days4Innovation !'
                msg.attach(MIMEText(body,'plain'))

                icspart = MIMEBase('text', 'calendar', **{'method' : 'REQUEST', 'name' : 'meeting.ics'})
                icspart.set_payload( open("my.ics","rb").read() )
                icspart.add_header('Content-Transfer-Encoding', '8bit')
                icspart.add_header('Content-class', 'urn:content-classes:calendarmessage')
                msg.attach(icspart)

                text = msg.as_string()
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(email_user,email_password)


                server.sendmail(email_user,email_send,text)
                server.quit()

            except:
                print('An error occured!')

    if request.method == 'POST':
        return redirect(url_for('thx'))



    return render_template("registration.html")


@app.route("/thx", methods=['GET'])
def thx():
    return render_template("thx.html")




if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)