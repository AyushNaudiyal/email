# Basic usage
sender = EmailSender(
    smtp_server='smtp.gmail.com',
    smtp_port=587,
    username='your.email@gmail.com',
    password='your-password'
)

# Send simple email
sender.send_email(
    to_email='recipient@example.com',
    subject='Test Email',
    body='This is a test email'
)

# Send HTML email with attachments
sender.send_email(
    to_email='recipient@example.com',
    subject='HTML Test',
    body='<h1>Hello</h1><p>This is HTML content</p>',
    is_html=True,
    attachments=['document.pdf', 'image.jpg']
)