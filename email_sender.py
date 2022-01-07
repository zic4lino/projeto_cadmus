import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
def envio_email(email_remetente,email_destinatario,
                senha_remetente,anexo):
    try:
        mensagem = MIMEMultipart()
        mensagem['From'] = email_remetente 
        mensagem['To'] = email_destinatario
        mensagem['Subject'] = "Compilado de vagas"
        corpo_email = "Segue compilado de vagas em anexo"
        mensagem.attach(MIMEText(corpo_email, 'plain'))
        arquivo_anexo = anexo
        anexo = open('compilado_vagas.xlsx','rb')

        email_base = MIMEBase('application', 'octet-stream')
        email_base.set_payload((anexo).read())
        encoders.encode_base64(email_base)
        email_base.add_header('Content-Disposition', "attachment; filename= %s" % arquivo_anexo)
        mensagem.attach(email_base)
        anexo.close()
        email_inteiro = text = mensagem.as_string()
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.login(email_remetente,senha_remetente)
        s.sendmail(email_remetente,email_destinatario, email_inteiro)
        print("Email enviado!!!!")
    except Exception as emailError:
        print("Erro ao enviar email."+str(emailError))
    finally:
        s.quit()
