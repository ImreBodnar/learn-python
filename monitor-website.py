# Website monitoring module with email notification.

import requests
import smtplib
import os

EMAIL_ADDRESS = os.environ.get('PYTHON_EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('PYTHON_EMAIL_PASSWORD')

def send_notification(message):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        msg = f"Subject: SITE DOWN!\n{message}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)

try:
    response = requests.get('http://ec2-13-61-9-81.eu-north-1.compute.amazonaws.com:3000/')

    if response.status_code == 200:
        print('App is RUNNING!')
    else:
        print('App is DOWN!')
        send_notification(f'Returned statuscode is {response.status_code}. Fix the issue and restart the container!')
except Exception as ex:
    print(f'Connection Error! Details: {ex}')
    send_notification('App is not accessible at all!')