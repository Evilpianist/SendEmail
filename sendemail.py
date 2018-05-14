import smtplib
from email.mime.multipart import MIMEMultipart

fromaddr = "youremail" # change the content to the email address you use to send email
fromaddrpass = "yourpassword" # change this content to your password
toaddr = "usersemail" # change this content to the email addr you want to send to.

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Testing Python Email" # cusmize your title

body = "This is an automated email" # customize your content

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(fromaddr,fromaddrpass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()