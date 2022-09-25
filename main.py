import datetime
import time
import smtplib
from cred import email
from cred import password
from cred import to
# Step one, figure out how to send an email
class main():
    def __init__(self):
        # Setup vars, sending email, recieveing email
        self.time = datetime.datetime.now()
        self.dailySent = False
        self.sendServer = smtplib.SMTP('smtp.gmail.com', 587)
        self.email = email
        self.password = password
        self.sendTo = to
        
    def loop(self):
        while True:
            time.sleep(1)
            self.time = datetime.datetime.now()
            if self.time.hour == 24 and self.time.minute == 0 and self.time.minute == 0 and self.dailySent == False:
                self.sendDaily()
                self.dailySent = True   
            if self.time.hour == 1 and self.dailySent == True:
                self.dailySent == False

    
    
    def checkMail(self):
        return
    def sendDaily(self):
        
        SUBJECT = str(self.time.day)+"/"+str(self.time.month)+"/"+str(self.time.year)
        TEXT = "Message\nHiii\n\n\nhiiii"
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        self.sendServer.starttls()
        self.sendServer.login(self.email, self.password)
        self.sendServer.sendmail(email, self.sendTo, message)
        self.sendServer.quit()

        return
x = main()
x.sendDaily()