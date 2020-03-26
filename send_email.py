import smtplib
# Don't Forget TO Install smtplib Library
# pip install smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

# Remember to allow less Secure apps in senders account.
# Read ReadMe for more info.
senders_mail_address=''   #add senders email address here
senders_password=''		  #add senders password here
recivers_mail_address=''  #add recivers mail
server.login('senders_mail_address', 'senders_password')
subject = 'Mail Subject'
body = str('Message Body ')
msg = 'Subject:' + str(subject+"\n\n"+body)
server.sendmail(
    senders_mail_address,   #sender mail address
    recivers_mail_address, #change your email here in order to get notification to your mail "Reciever mail"
    msg                         #content of mail
)
print("Mail Sent!")
server.quit()
