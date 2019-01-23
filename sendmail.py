import smtplib
import config

def send_email(subject, msg):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(config.EMAIL_ADDRESS,config.PASSWORD)
    message : "Subject :{}\n\n{}".format(subject,msg)
    server.sendmail(config.EMAIL_ADDRESS,config.EMAIL_ADDRESS , message)
    server.quit()
    print('EMAIL SENT')

Subject = "Test email"
msg = "my first email"

send_email(Subject,msg)





#Config is nothing but a python file containing the email id and password
