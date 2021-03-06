import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

template = """
<table align="center" border="0" cellpadding="0" cellspacing="0" width="600" style="border: 1px solid #cccccc;">
  <tr>
    <td bgcolor="#ee4c50" style="padding: 40px 10px 30px 10px;" align="center">
      <!-- <img width="200" height="300" src="https://orig00.deviantart.net/cc79/f/2014/043/a/8/a_cute_valentines_day_by_pedro_nekoi_by_matsurixbear-d7683c8.jpg" /> -->
      <p style="font-family: cursive; font-size: 40px"><b>Happy Valentines!</b></p>
    </td>
    <td>
      <table border="0" cellpadding="0" cellspacing="0">
        <tr>
          <td bgcolor="#ffffff" style="padding: 40px 30px 40px 30px">
            <table border="0" cellpadding="0" cellspacing="0" width="100%">
              <tr>
                <td>
                  <p style="font-family: cursive">Dear {},</p>
                  <p style="font-family: cursive" id="message">{}</p>
                  <p style="font-family: cursive">Love,</p>
                  <p style="font-family: cursive">{} & Roast4Hearts</p>
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td bgcolor="#fcd2d8" style="padding: 20px">
            <p style="font-family: Helvetica Neue, serif; font-size: 14px">Your beautiful friendship and your friend's generosity contributed to ending heart disease! Send a roast or a compliment like this to a friend for just $1. Venmo @Roasts4Hearts. More info <a href="https://www.facebook.com/events/1229340043867148/">here</a></p>
            <p style="font-family: Helvetica Neue, serif; font-size: 12px">All proceeds going to <a href="http://www.heart.org">American Heart Association</a></p>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
"""


def sendMail(address, subject, message, sender_name, recipient_name):
	msg = MIMEMultipart()
	fromaddr = "roasts4hearts@gmail.com"
	msg['From'] = fromaddr
	msg['To'] = address
	msg['Subject'] = subject

	msg.attach(MIMEText(template.format(recipient_name, message, sender_name), 'html'))

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "GumballChallenge")
	text = msg.as_string()
	server.sendmail(fromaddr, address, text)
	server.quit()
