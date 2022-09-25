import imaplib

from pydantic import EmailError
from cred import email
from cred import password
from cred import to

imap_ssl_host = 'imap.gmail.com'
imap_ssl_port = 993
username = email
password = password
server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
#    status, data = imap.fetch(num, '(BODY[HEADER.FIELDS (SUBJECT DATE FROM TO)])')
server.login(username, password)
server.select('Inbox')
status,data = server.search(None,"ALL")
total_num = 0
for num in data[0].split():
    total_num = num

status,data = server.fetch(total_num,'(BODY[HEADER.FIELDS (FROM)])')
start = 0
end = 0
meta, fromEmail = data[0]
fromEmail = fromEmail.decode('utf-8')
print(fromEmail)
for i in range(0,len(fromEmail),1):
    if fromEmail[i] == '<':
        start = i
    if fromEmail[i] == '>':
        end = i
fromEmail = fromEmail[start+1:end]


status,data = server.fetch(total_num,'(BODY[TEXT] BODY[HEADER.FIELDS (SUBJECT)])')
print(data)
"""
for num in data[0].split():
      status, data = server.fetch(num, '(BODY[HEADER.FIELDS (FROM)])')
      email_msg = data[0][1]
      print(email_msg)

print(data)
"""