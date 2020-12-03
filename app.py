from flask import Flask ,render_template,request,redirect,url_for
from flask_mysqldb import MySQL
import pythoncom
import win32com.client



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
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO participant(nom,mail,remarque,evenements) VALUES (%s, %s, %s,%s)",(name,mail,remarque,evenements))
        mysql.connection.commit()
        cur.close()


    for event in events:

        i = titre.index(event)
        if i < 4 :
            day = "2020-12-07"
        else:
            day = "2020-12-08"


        start = day+debut[i]
        duration = duree[i]

        if mail is not None:
            try:
                pythoncom.CoInitialize()
                outlook = win32com.client.Dispatch("Outlook.Application")
                appt = outlook.CreateItem(1)
                appt.Start = start # yyyy-MM-dd hh:mm
                appt.Subject = event
                appt.Duration = duration # In minutes (60 Minutes)
                appt.Location = "Sonatel"
                appt.MeetingStatus = 1 # 1 - olMeeting; Changing the appointment to meeting. Only after changing the meeting status recipients can be added

                appt.Recipients.Add(mail) # Don't end ; as delimiter

                appt.Send()
        
                pythoncom.CoInitialize()

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