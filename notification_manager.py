from datetime import datetime
import smtplib
import os

GMAIL = os.environ["GMAIL"]
GMAIL_PW = os.environ["PYTHON_FLIGHT_FINDER_APP_PW"]
Y_MAIL = os.environ["YMAIL"]
SMTP = "smtp.gmail.com"
PORT = 587

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send_mail(self, flight):
        # print("Sending mail...")
        with smtplib.SMTP(SMTP, PORT) as conn:
            conn.starttls()
            conn.login(user=GMAIL, password=GMAIL_PW)
            conn.sendmail(
                from_addr=GMAIL,
                to_addrs=Y_MAIL,
                msg=f"Subject: Lower price alert!\n\nOnly PHP {flight.price} to fly from {flight.fly_from_city}-{flight.fly_from_code} to {flight.fly_to_city}-{flight.fly_to_code}, from {datetime.fromtimestamp(flight.flight_date_from).strftime("%Y-%m-%d")} to {datetime.fromtimestamp(flight.flight_date_to).strftime("%Y-%m-%d")}"
            )
        # print("Mail sent!")