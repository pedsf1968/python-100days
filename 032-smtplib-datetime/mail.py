import smtplib

BW_EMAIL = "#########"
BW_PASSWORD = "#####"
BW_SMTP_SERVER = "smtp.gmail.com"

with smtplib.SMTP(BW_SMTP_SERVER) as connection:
    # Secure the connection
    connection.starttls()
    connection.login(user=BW_EMAIL, password=BW_PASSWORD)
    connection.sendmail(
        from_addr=BW_EMAIL,
        to_addrs="toto@gmail.com",
        msg="Subject:Hello3\n\nThis is the body of the email."
    )
