import socket
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def test_connection():
    try:
        socket.create_connection(('Google.com', 80))
        return True
    except OSError:
        return False
ACT = str(test_connection())

if ACT == 'True':
    A = 'AWAN_NEW is UP'
else:
    A = 'AWAN_NEW is DOWN'

sender = 'karthikeyan@awaninfotech.com'
receivers = 'karthikeyan@awaninfotech.com'
password = '*********'
message = A

s = smtplib.SMTP('smtp.1and1.com', 587)
s.starttls()
s.login(sender, password)
msg = MIMEMultipart()
msg['From']=sender
msg['To']=receivers
msg['Subject']="This is TEST"
msg.attach(MIMEText(message, 'plain'))
s.send_message(msg)
s.quit()