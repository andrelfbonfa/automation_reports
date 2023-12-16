import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


def enviaemail(assunto, corpo, anexo):
    
    fromaddr = "team_IT@email.com"
    toaddr = "team@email.com"
   
   # instance of MIMEMultipart 
    msg = MIMEMultipart() 
      
    # storing the senders email address   
    msg['From'] = fromaddr 
      
    # storing the receivers email address  
    msg['To'] = toaddr 

    ##msg['Cc'] = accaddr
      
    # storing the subject  
    msg['Subject'] = assunto
    ##rrvv = str(assunto)
    ##print = (rrvv) 
      
    # string to store the body of the mail 
    body = corpo
      
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
      
    # open the file to be sent  
    filename = anexo
    ##print (filename)
    attachment = open(""+filename, "rb") 
      
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
      
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
      
    # encode into base64 
    encoders.encode_base64(p) 
       
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
      
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
      
    # creates SMTP session 
    s = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com:587') 
      
    # start TLS for security 
    s.starttls() 
      
    # Authentication 
    userenv01    = 'pass'
    senha = 'pass'
    s.login(userenv01,senha)
      
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
      
    # sending the mail 
    s.sendmail(fromaddr, toaddr.split(','), text) 
      
    # terminating the session 
    s.quit() 
    valorretorno = "OK"
    return valorretorno
