import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_file_via_gmail(to, subject, body, file_path, file_name):
    gmail_user = 'juanandresoro435@gmail.com'
    gmail_password = 'srtqchswynxyliur'

    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body))

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(file_path, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    'attachment', filename=file_name)
    msg.attach(part)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to, msg.as_string())
        server.close()
        print ('Email sent!')
    except Exception as e:
        print ('Something went wrong...', e)

if __name__ == '__main__':
    to = 'juanxxi2015@gmail.com'
    subject = 'Test Email'
    body = 'This is a test email'
    file_path = "C:/Users/juana/Documentos/DBGUI.py"
    file_name = 'DBGUI.py'
    send_file_via_gmail(to, subject, body, file_path, file_name)
