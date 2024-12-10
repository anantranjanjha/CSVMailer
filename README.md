# Mass Email Sender with CSV Input

This Python script sends personalized emails in bulk using a CSV file for input. Each email includes custom HTML content and optional file attachments.

---

## Features

- Send **mass emails** with unique content based on CSV data.
- Use **HTML email templates** for professional-looking emails.
- Personalize emails with recipient-specific details (e.g., Name, Amount).
- Leverages **Gmail App Password** for secure authentication.

---

## Prerequisites

1. Python 3.7 or later.
2. Gmail account with [App Passwords](https://support.google.com/accounts/answer/185833?hl=en).
3. CSV file with the following columns:
   - `Name`: Recipient's name.
   - `Email`: Recipient's email address.
   - `Amount`: Custom value for each email (e.g., a payment amount).
   - `Subject`: Subject line for the email.
   - `URL`: Optional URL to include in the email.

---

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/anantranjanjha/CSVMailer.git
cd CSVMailer

export sender="your-email@gmail.com"
export emailpass="your-app-password"
