import smtplib
my_email = 'BigGuy@gmail.com'
password = "BigguysOnly"
connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=my_email,password=password)
