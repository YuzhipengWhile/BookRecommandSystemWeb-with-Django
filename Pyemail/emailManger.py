import smtplib
from email.mime.text import MIMEText

mail_host = 'smtp.exmail.qq.com'
mail_user = '保密'
mail_pass = '保密'
sender = '保密'

# 用于发送HTML邮件
def sendEmail(content,title,receivers = ('保密',)):
    message = MIMEText(content,'html','utf-8')

    message['From'] = 'sjm'
    message['To'] = ','.join(receivers)
    message['Subject'] = title
    smtpObj = smtplib.SMTP_SSL(mail_host,465)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.send_message(from_addr=sender,to_addrs=receivers,msg=message)


if __name__ == "__main__":
    # a = b'\xc7\xeb\xca\xb9\xd3\xc3\xca\xda\xc8\xa8\xc2\xeb\xb5\xc7\xc2\xbc\xa1\xa3\xcf\xea\xc7\xe9\xc7\xeb\xbf\xb4'
    # print(a.decode('gbk'))
    content = '''
        <h1>来自SMTP的邮件</h1>
        <p>这只是一次邮件<strong>测试</strong></p>
        <ul>
            <li>列表1</li>
            <li>列表2</li>
        </ul>
    '''
    sendEmail(content=content,title='Python')