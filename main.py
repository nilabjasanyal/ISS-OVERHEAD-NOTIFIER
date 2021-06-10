import requests
from datetime import datetime
import smtplib
import time

def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="****.****@gmail.com",password="*****")#USE YOUR OWN ID AND PASSWORD
        connection.sendmail(from_addr="nilabja.2000@gmail.com",to_addrs="nilabja.sanyal@gmail.com",
                            msg="subject:ISS OVERHEAD\n\nHEY LOOK UP!!")
    print("mail sent")

MY_LAT = 23.040561  # Your latitude
MY_LONG = 87.858633  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

hour = time_now.hour


night_time = False

if hour >= 18 or hour <= 5: # USE YOUR OWN SUNRISE SUNSET HOURS
    print("hour ok")
    night_time = True

iss_overhead= False

if (MY_LAT-5 <= iss_latitude <= MY_LAT+5) and ( MY_LONG-5 <= iss_longitude<= MY_LONG+5):
    print("coor ok")
    iss_overhead=True

while night_time and iss_overhead:

    send_mail()
    time.sleep(60)









