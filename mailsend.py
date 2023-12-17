import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#anexo
from email.mime.base import MIMEBase
from email import encoders

#start
host="smtp.meuservidor.com"
port="587"
login="meuemail@lol.com.br"
senha="minhasenha"

server= smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.login(login,senha)

#email Mime

#body
body='''
    <div>
        <h1>Você é o melhor que nós temos</h1>
        <p>Estamos contente por você</p>
    </div>

'''

email_msg = MIMEMultipart()
email_msg['From'] = login
email_msg['To'] = 'destinatario@gmail.com'
email_msg['Subject']='Python mail send, yahh'
email_msg.attach(MIMEText(body,'html'))

anexo='E:/PDF/arquivo.pdf'

parte_apos_pdf = anexo.split('E:/PDF/', 1)[1]


attachment = open(anexo,'rb')
att = MIMEBase('application','octet-stream')
att.set_payload(attachment.read())
encoders.encode_base64(att)

att.add_header('Content-Disposition',f'attachment; filename={parte_apos_pdf}')
attachment.close()
email_msg.attach(att)


#Send type smtp
server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())
server.quit()

