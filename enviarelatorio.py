#!/usr/bin/env python


import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

try:
    fromaddr = 
    toaddr = 
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 

    body = "\nbla bla bla"

    msg.attach(MIMEText(body, 'plain'))

    filename = 'nomes.csv'

    attachment = open('nomes.csv','rb')


    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    attachment.close()

    server = smtplib.SMTP('smtp-relay.sendinblue.com', 587)
    server.starttls()
    server.login(fromaddr, "<TOKEN>")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print('\nEmail enviado com sucesso!')
except:
    print("\nErro ao enviar email")
