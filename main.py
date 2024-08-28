import smtplib
from DateTime import checkday
from fileLoad import fileload


today=checkday()
if today==2:
    myquote=fileload()

myemail="randomd878@gmail.com"
mypassword="lvtygsrbsybekfze"
with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
    connection.starttls()#encrypts the mail

    connection.login(user=myemail,password=mypassword)
    connection.sendmail(from_addr=myemail,
                        to_addrs="r.dude@myyahoo.com",
                        msg=f"subject:Weekly Wisdom \n\n{myquote}")

