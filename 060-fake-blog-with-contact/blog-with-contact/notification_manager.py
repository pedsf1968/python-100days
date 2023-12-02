import smtplib
from os import environ


class Message:
    def __init__(self, data):
        self.name = data["name"],
        self.email = data["email"],
        self.phone = data["phone"],
        self.content = data["message"]

    def display(self):
        print(f"Name: {self.name}\n"
              f"Email: {self.email}\n"
              f"Phone: {self.phone}\n"
              f"Content: {self.content}")

    def get_json(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "content": self.content
        }


class NotificationManager:
    def __init__(self):
        self.smtp_server = environ["DEVOPS_SMTPLIB_SERVER"]
        self.smtp_email = environ["DEVOPS_SMTPLIB_EMAIL"]
        self.smtp_password = environ["DEVOPS_SMTPLIB_PASSWORD"]

    def display(self):
        print(self.smtp_server, self.smtp_email, self.smtp_password)

    def send_email(self, message):
        with smtplib.SMTP(self.smtp_server) as connection:
            email_msg = f"Subject:New Message\n\nName: {message.name}\nEmail: {message.email}\nPhone: {message.phone}\nMessage:{message.content}"
            connection.starttls()
            connection.login(user=self.smtp_email, password=self.smtp_password)
            connection.sendmail(from_addr=message.email,
                                to_addrs=self.smtp_email,
                                msg=email_msg)