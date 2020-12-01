import win32com.client
outlook = win32com.client.Dispatch("Outlook.Application")

def sendMeeting(mail):    
    appt = outlook.CreateItem(1) # AppointmentItem
    appt.Start = "2018-10-28 10:10" # yyyy-MM-dd hh:mm
    appt.Subject = "Subject of the meeting"
    appt.Duration = 60 # In minutes (60 Minutes)
    appt.Location = "Location Name"
    appt.MeetingStatus = 1 # 1 - olMeeting; Changing the appointment to meeting. Only after changing the meeting status recipients can be added

    appt.Recipients.Add(mail) # Don't end ; as delimiter

    appt.Save()
    appt.Send()

if __name__=="__main__":
    sendMeeting()