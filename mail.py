import smtplib
from email.mime.text import MIMEText
_user = "441836637@qq.com"
_pwd = "xhxblklsougqcaej"
_to = "littercap@gmail.com"

msg = MIMEText("Test")
msg["Subject"] = "don't panic"
msg["From"] = _user
msg["To"] = _to

s = smtplib.SMTP_SSL("smtp.qq.com", 465)
s.login(_user, _pwd)
s.sendmail(_user, _to, msg.as_string())
s.quit()
print ("Success!")
