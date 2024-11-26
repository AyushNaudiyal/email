# Email Sending Script

A Python script to send emails using the Gmail SMTP server.

---

## Features

- Send emails with a subject and body.
- Uses **Gmail SMTP** for email delivery.
- Secure login with Gmail **App Password**.

---

## Requirements

- Python 3.6 or higher
- Gmail account with **App Password** enabled (2-Step Verification must be turned on).

---

## Setup

1. Enable **2-Step Verification** in your Gmail account.  
2. Generate an **App Password** in Gmail settings:
   - Go to **Google Account > Security > App Passwords**.
   - Choose the app and device, then generate the password.
   - Use the generated password in this script.

---

## Usage

1. Run the script:
   ```bash
   python send_email.py
   ```
2. Enter the following details when prompted:
   - Your Gmail address
   - Your Gmail App Password
   - Recipient's email address
   - Email subject
   - Email body
3. The email will be sent, and you'll receive a success message.

---

## Note

- Ensure that your Gmail account allows SMTP connections.
- Use **App Passwords** for added security instead of your main Gmail password.

---
