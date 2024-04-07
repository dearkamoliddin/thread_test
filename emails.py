import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading


from_email = "dearkamoliddin@gmail.com"


def send_email(to_email):
    email_message = MIMEMultipart()
    email_message['From'] = from_email
    email_message['To'] = to_email
    email_message['Subject'] = "Salom!"
    email_message.attach(MIMEText("Nima gap", "plain"))

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    server.login(from_email, "xnwl oxpa dlca iuhs")
    try:
        server.sendmail(from_email, to_email, email_message.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error occurred: {str(e)}")


users = [
    "dearkamoliddin@gmail.com",
    "sanjarbeksocial@gmail.com",
    "shukurullonosirov@gmail.com",
    "uzalisherov@gmail.com",
    "maftuna200412@gmail.com",
    "shohpad@gmail.com",
    "muhammadrahimiminjonov@gmail.com",
    "khondamiras@gmail.com",
    "boxodirazimov683@gmail.com",
    "xikmatullayevogabek@gmail.com",
    "ogashbek20@gmail.com",
    "inoyatovfayzullo878@gmail.com"
]


def send_email_users():
    for user in users:
        send_email(user)


t1 = threading.Thread(target=send_email_users)
t1.start()