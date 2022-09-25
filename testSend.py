import smtplib
from cred import email
from cred import password
from cred import to
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login(email, password)
 
# message to be sent
message = "Message_you_need_to_send"
 
# sending the mail
s.sendmail(email, to, message)
 
# terminating the session
s.quit()