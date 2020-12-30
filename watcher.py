import datetime
import requests
import time

from decouple import config
from twilio.rest import Client

TWILIO_SID = config('TWILIO_SID')
AUTH_TOKEN = config('AUTH_TOKEN')
client = Client(TWILIO_SID, AUTH_TOKEN)

print("Watching...")

with open("websites.txt", "r") as file:
    sites = file.readlines()


def write_log(content):
    print(content)
    with open("log.txt", "a") as file:
        file.write(content + "\n")

while True:
    for site in sites:
        site = site.strip()
        timestamp = str(datetime.datetime.now())
        res = requests.get(site)
        content = f"{timestamp}\t\t`{site}`\t\t{res.status_code}"
        if res.status_code != 200:
            message = client.messages.create(
                to=config('TWILIO_TO'),
                from_=config('TWILIO_FROM'),
                body=f"DOWN ALERT: {content}"
            )
        write_log(content)
    time.sleep(60)
