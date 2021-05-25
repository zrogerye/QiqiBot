def sendemail(content):
    GMAILPASS = 'qiqiBot3000'
    temp = True
    args = content.split("/")
    receiver = args[1]

    sender = ''

    if len(args) < 5:
        return 'qiqi thinks there are not enough arguments'
        temp = False

    if int(args[4]) == 1:
        sender = 'botqiqi2515@gmail.com'

    if int(args[4]) == 2:
        sender = 'qiqibot2515@gmail.com'

    if temp == True:
        subject = args[2]
        bodySend = args[3]
        msg = MIMEText(bodySend, 'html')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = receiver
        s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
        s.login(user=sender, password=GMAILPASS)
        s.sendmail(sender, receiver, msg.as_string())
        s.quit()
        if temp == True:
            return 'okay! qiqi will deliver the message'
    temp = True
