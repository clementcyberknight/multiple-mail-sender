import os
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(sender_email, sender_password, recipient_emails, subject, body_text):
    try:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["Subject"] = subject

        # Attach the body text
        message.attach(MIMEText(body_text, "plain"))

        # Add recipients to BCC field to make them hidden
        message["Bcc"] = ", ".join(recipient_emails)

        # Connect to the SMTP server and send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_emails, message.as_string())
            print("Successfully sent email to recipients")

    except smtplib.SMTPAuthenticationError as auth_error:
        print("SMTP Authentication Error. Please check your email and password.")
    except Exception as e:
        print("An error occurred while sending the email:", e)


def read_recipient_emails_from_csv(csv_file):
    recipient_emails = []
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            recipient_emails.extend(row)
    return recipient_emails


if __name__ == "__main__":
    sender_email = "Email Address"
    sender_password = "Enter Google App Password for the gmail account"

    subject = "Enter Subject"
    body_text = """
    Enter Body
    """

    csv_file = "email_add.csv"  # Update this with your CSV file path
    recipient_emails = read_recipient_emails_from_csv(csv_file)
    send_email(sender_email, sender_password, recipient_emails, subject, body_text)
