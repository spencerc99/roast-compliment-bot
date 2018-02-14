import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
 

def sendMail(address, subject, message):
	msg = MIMEMultipart()
	fromaddr = "roasts4hearts@gmail.com" 
	msg['From'] = fromaddr
	msg['To'] = address
	msg['Subject'] = subject
	msg.attach(MIMEText(message, 'html'))
	 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "GumballChallenge")
	text = msg.as_string()
	server.sendmail(fromaddr, address, text)
	server.quit()