import datetime
import time
import smtplib
from imap_tools import MailBox, AND

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
        self.imap_ssl_host = 'imap.gmail.com'
        self.imap_ssl_port = 993

        
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
        with MailBox(self.imap_ssl_host).login(self.email,self.password,'INBOX') as mailbox:
            for msg in mailbox.fetch(AND(from_=self.sendTo, seen=False)):
                if msg.subject == "TODO":
                    print()
                    print("TODO!")

        """
        server = imaplib.IMAP4_SSL(self.imap_ssl_host, self.imap_ssl_port)
        server.login(self.email,self.password)
        server.select('Inbox')
        status, data = server.search(None, '(UNSEEN)')
        print(data.decode('utf-8'))
        totalEmails = 0
        for num in data[0].split():
            totalEmails = num
        startEmailNum = int(totalEmails.decode('utf-8'))
        for x in range(startEmailNum,startEmailNum-20,-1):
            status,data = server.fetch(bytes(str(x),'utf-8'),'(BODY[HEADER.FIELDS (FROM)])')
            start = 0
            end = 0 
            meta, fromEmail = data[0]
            fromEmail = fromEmail.decode('utf-8')
            for i in range(0,len(fromEmail),1):
                if fromEmail[i] == '<':
                    start = i+1
                if fromEmail[i] == '>':
                    end = i
            if fromEmail == self.sendTo:
                # TODO
                return
        """

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
x.checkMail()