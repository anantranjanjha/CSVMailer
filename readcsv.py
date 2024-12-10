import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
import os


def emailformate(name,balance,weblink):
  htmllist = """
  <!DOCTYPE html>
  <html>
  <head>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f4f4f4;
        color: #333;
      }
      .email-container {
        max-width: 600px;
        margin: 20px auto;
        background-color: #ffffff;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
      }
      .email-header {
        background-color: #007BFF;
        color: #ffffff;
        padding: 20px;
        text-align: center;
      }
      .email-header h1 {
        margin: 0;
        font-size: 24px;
      }
      .email-body {
        padding: 20px;
      }
      .email-body h2 {
        color: #007BFF;
        font-size: 20px;
      }
      .email-body p {
        line-height: 1.6;
        margin: 15px 0;
      }
      .email-footer {
        background-color: #f4f4f4;
        color: #888;
        text-align: center;
        padding: 10px 20px;
        font-size: 12px;
      }
      .button {
        display: inline-block;
        background-color: #007BFF;
        color: #ffffff;
        text-decoration: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 16px;
        margin-top: 10px;
      }
      .button:hover {
        background-color: #0056b3;
      }
    </style>
  </head>
  <body>
    <div class="email-container">
      <h1>This is a test mail sent to you from bank.</h1>
      <div class="email-header">
        <h1>Welcome to Our Banking Service</h1>
      </div>

      <!-- Body -->
      <div class="email-body">
        <h2>Hello, $name</h2>
        <p>
          Thank you for joining us! We're thrilled to have you onboard. At BPMC Bank, 
          we're committed to providing you with the best experience possible.
        </p>
        <p>
          Here's a quick overview of your account Balance: $balance
        </p>
        <p>
          Ready to get started? Click the button below to access your account and explore all the features waiting for you.
        </p>
        <a href=$weblink class="button">Get Started</a>
      </div>

      <!-- Footer -->
      <div class="email-footer">
        <p>If you have any questions, feel free to <a href="mailto:support@example.com">contact us</a>.</p>
        <p>© 2024 [Your Company Name]. All rights reserved.</p>
      </div>
    </div>
  </body>
  </html>

  """
  data = {
    "name": name,
    "balance": balance,
    "weblink": weblink
  }
  template = Template(htmllist)
  htmlstring = template.substitute(data)
  return htmlstring
# print(dataset)




def sendEmail(receiver,subject,htmlstr):
    sender = os.getenv("sender")
    password = os.getenv("emailpass")
    receiver = receiver
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    
    text = MIMEText(htmlstr,"html")
    msg.attach(text)
    try:
      with smtplib.SMTP("smtp.gmail.com",587) as server:
          server.starttls()
          server.login(sender,password)
          server.sendmail(sender,receiver,msg.as_string())
          server.quit()
          print("Email sent successfully")
    except Exception as e:
      print(f"Error: {e}")
    
dataset = pd.read_csv("emaillist.csv")

try:
  for index,data in dataset.iterrows():
    sendEmail(data['Email'],data['subject'],emailformate(data['Name'],data['Amount'],data['url']))
except:
  print("problem with csv file")