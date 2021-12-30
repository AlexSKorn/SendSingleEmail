import yagmail
import os
import time

sender = 'akorndev@gmail.com'
receiver = 'nxjmmkmvd@emltmp.com'

subject = "This is the subject"

contents = """
Here is the contents of the email!
Hi!
"""

while True: 
  yag = yagmail.SMTP(user=sender, password=os.getenv('TEST'))
  yag.send(to=receiver, subject=subject, contents=contents)
  print("Email Sent!")
  time.sleep(60)