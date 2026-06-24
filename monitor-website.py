# Website monitoring module with email notification.
import boto3
import requests
import smtplib
import os
import paramiko

from aws import ec2_client

EMAIL_ADDRESS = os.environ.get('PYTHON_EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('PYTHON_EMAIL_PASSWORD')


def send_notification(message):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        msg = f"Subject: SITE DOWN!\n{message}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)

def restart_container():
    print('App is RESTARTING!')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='ec2-13-61-9-81.eu-north-1.compute.amazonaws.com', username='ec2-user',
                key_filename='~/.ssh/id_rsa')
    stdin, stdout, stderr = ssh.exec_command('docker start CONTAINER_ID')
    print(stdout.readlines())
    ssh.close()
    print('App is RESTARTED!')


try:
    response = requests.get('http://ec2-13-61-9-81.eu-north-1.compute.amazonaws.com:3000/')

    if response.status_code == 200:
        print('App is RUNNING!')
    else:
        print('App is DOWN!')
        send_notification(f'Returned statuscode is {response.status_code}. Fix the issue and restart the container!')

        # restart application
        restart_container()
except Exception as ex:
    print(f'Connection Error! Details: {ex}')
    send_notification('App is not accessible at all!')

    # restart server

    # restart app
    restart_container()