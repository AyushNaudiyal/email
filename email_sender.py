import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, app_password, receiver_email, subject, body):
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Add body to email
        msg.attach(MIMEText(body, 'plain'))

        # Create SMTP session
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            # Enable security
            server.starttls()
            
            # Login to the server
            server.login(sender_email, app_password)
            
            # Send email
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Your email credentials
    sender_email = input("Enter your Gmail address: ")
    app_password = input("Enter your App Password: ")
    
    # Email details
    receiver_email = input("Enter recipient's email: ")
    subject = input("Enter email subject: ")
    body = input("Enter email body: ")

    # Send the email
    send_email(sender_email, app_password, receiver_email, subject, body)