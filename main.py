import smtplib
to = input("Enter the email of recipent: ")

content = input("Enter the content for mail: ")

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("alahyaneosama@gmail.com","1234")
    server.sendmail("alahyaneosama@gmail.com", to, content)
    server.close()
sendEmail(to, content)