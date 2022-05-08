import os
import smtplib
import imghdr
from email.message import EmailMessage

YOUR_EMAIL_ADDRESS = '27veers@gmail.com'
APP_PASSWORD = 'Veerlaller1!$'
pdfresume = 'Resume.pdf'
with open(pdfresume, 'rb') as doc:
    doc_data = doc.read()
    doc_name = doc.name
emails = ['27veers@gmail.com']
for x in emails:
    msg = EmailMessage()
    msg['Subject'] = 'Testing testing testing'
    msg['From'] = "27veers@gmail.com"
    msg['To'] = str(x)
    msg.set_content("""
    <!DOCTYPE html>
    <html>
        <body>
            <h1>This is the message</h1>
        </body>
    </html>
    """, subtype='html')
    msg.add_attachment(doc_data, maintype='image',subtype='octet-steam',filename=doc_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("27veers@gmail.com", "Veerlaller1!$")
        smtp.send_message(msg)