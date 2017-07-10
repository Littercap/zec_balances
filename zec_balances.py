import requests
import time
import sys
import smtplib
from email.mime.text import MIMEText

headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
_user = "441836637@qq.com"
_pwd = "xhxblklsougqcaej"
_to = "littercap@163.com"

msg = MIMEText("At least one worker crashed!")
msg["Subject"] = "Miner Alarm"
msg["From"] = _user
msg["To"] = _to

while(True):
    result = requests.get("http://zcash.flypool.org/api/miner_new/t1bqmB9MzbeUkqVZMJtvur5PY22QozvKyZk",headers=headers)
    PC163 = result.json()["workers"]['littercap@163']
    PCP40 = result.json()["workers"]['littercap@P40']

    PC163time = time.localtime(PC163['workerLastSubmitTime'])
    PCP40time = time.localtime(PCP40['workerLastSubmitTime'])

    print('PC163:'+'\t'+'HashRate:'+PC163['hashrate']+'\t'+'ValidShare:'+str(PC163['validShares'])+'\t'+'LastSubmit:'+time.strftime(" %m-%d %H:%M:%S", PC163time)+'\r')
    print('PCP40:'+'\t'+'HashRate:'+PCP40['hashrate']+'\t'+'ValidShare:'+str(PCP40['validShares'])+'\t'+'LastSubmit:'+time.strftime(" %m-%d %H:%M:%S", PCP40time)+'\r')

    if PC163['validShares'] == 0 or PCP40['validShares'] == 0:
        print("One Worker Sucks!", '\n')
        mail = smtplib.SMTP_SSL("smtp.qq.com", 465)
        mail.login(_user, _pwd)
        mail.sendmail(_user, _to, msg.as_string())
        mail.quit()
        break

    for i in range(600):
        sys.stdout.writelines(time.asctime(time.localtime()) + '\r')
        time.sleep(1)
