import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()

# Authentication
s.login("mailID", "password")

# message to be sent   
SUBJECT = "Book ASAP"   
TEXT = "THIS UPDATE IS FOR 45+ ONLY \nCenter Available: "

message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

# sending the mail
s.sendmail("SenderID", "Reciever ID", message)

# terminating the session
s.quit()
