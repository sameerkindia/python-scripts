import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path



html = Template(Path('./index.html').read_text())
email = EmailMessage()

email['from'] = 'Sameer khan'
email['to'] = 'wisamew490@exitbit.com'
email['subject'] = 'Mubarak ho ji'

# email.set_content("aap python seekh rahe hai")
email.set_content(html.substitute(name='sameer'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sameerkhanaa5@gmail.com', 'your_password')
    smtp.send_message(email)
    print("done")