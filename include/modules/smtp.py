import smtplib, ssl
import config
from secrets import secrets

from email.mime.text import MIMEText

class SMTP(object):

    def __init__(self):
        # From email
        self.femail = secrets.FEMAIL
        self.password = secrets.PASSWORD
        # To email
        self.temail = secrets.TEMAIL
        self.host = config.HOST
        self.port = config.PORT
        self.server = smtplib.SMTP()
        self.msg = "default spenders message"

    def open_connection(self):
        self.server.connect(self.host, self.port)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login(self.femail, self.password)

    def close_connection(self):
        self.server.quit()

    def send_email(self):
        self.server.sendmail(self.femail, self.temail, self.msg)

    # Hard coded message
    def create_msg(self):
        _msg = MIMEText("Message created with create_msg")
        _msg["Subject"] = "Spenders automatic email"
        self.msg = _msg.as_string()
