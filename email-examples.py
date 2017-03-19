#!/usr/bin/env python
'email-examples.py - demo creation of email messages'

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP


# multipart alternative: text and html
def make_map_msg():
    email = MIMEMultipart('alternative')
    text = MIMEText('Hello World!\r\n', 'plain')
    email.attach(text)
    html = MIMEText(
        '<html><body><h4>Hello World!</h4>'
        '</body></html>', 'html')
    email.attach(html)
    return email


# multipart: images
def make_img_msg(fn):
    f = open(fn, 'r')
    data = f.read()
    f.close()
    email = MIMEImage(data, name=fn)
    email.add_header('Content-Disposition',
                     'attachment; filename="%s"' % fn)
    return email


def sendMsg(fr, to, msg):
    s = SMTP('smtp.csu.edu.cn')
    s.login('155011020', '8936270hxj')
    errs = s.sendmail(fr, to, msg)
    s.quit()


if __name__ == '__main__':
    SENDER = '155011020@csu.edu.cn'
    RECIPS = ['8936270@qq.com']
    print 'Sending multipart alternative msg...'
    msg = make_map_msg()
    msg['From'] = SENDER
    msg['To'] = ', '.join(RECIPS)
    msg['Subject'] = 'multipart alternative test'
    sendMsg(SENDER, RECIPS, msg.as_string())

    print 'Sending image msg...'
    msg = make_img_msg('/home/hxj/test.png')
    msg['From'] = SENDER
    msg['To'] = ', '.join(RECIPS)
    msg['Subject'] = 'image file test'
    sendMsg(SENDER, RECIPS, msg.as_string())
