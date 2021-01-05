# Gerardo I. Armenta
# Assignment 1
# Last edit 7-18-20
# Purpose: Python script made to send emails through terminal

from socket import *

mailserver = ('smtp.utep.edu', 25)
helo = 'helo utep.edu\r\n'
m_from = 'mail from: g@utep.edu\r\n'.encode()  # Enter email address
to_intro = 'rcpt to: g@utep.edu\r\n'.encode()  # Enter email address
m_data = 'data\r\n'.encode()
m_subject = 'Subject: Email from my email client\r\n\r\n'.encode()
m_text = 'This is a test email from my own email client. Hope it finds you well.\r\n'.encode()
m_sign = 'Armenta, Gerardo\r\n'.encode()
end = '.\r\n'.encode()
quit = 'QUIT\r\n'.encode()

# Promt to enter your UTEP's email address
entered_from = input('Enter your UTEP email address and press enter:\n')
print('Email entered!\n')

# Prompt to enter recipients email address
addressee = input('Enter recipient\'s email address and press enter:\n')
print('Email address entered!')

# Promts to enter the emails information
subject = input('Enter email subject and press enter:\n')
print('Subject entered!')
body = input('Type your message and press enter\n')
print('Message entered!')
print('\nsending...\n')
new_from = 'mail from: ' + entered_from + '\r\n'
new_to = 'rcpt to: ' + addressee + '\r\n'
new_subject = 'Subject: ' + subject + '\r\n\r\n'
new_body = body + '\r\n'

# Creating socket to use TCP connection to connect with the mail server
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(mailserver)

recv = client_socket.recv(1024)

# sending helo command for utep.edu
client_socket.send(helo.encode())
recv1 = client_socket.recv(1024)

# mail info
client_socket.send(new_from.encode())
recv2 = client_socket.recv(1024)
client_socket.send(new_to.encode())
recv3 = client_socket.recv(1024)
client_socket.send(m_data)
recv4 = client_socket.recv(1024)
client_socket.send(new_subject.encode())
client_socket.send(new_body.encode())
# client_socket.send(m_sign)
client_socket.send(end)
recv_msg = client_socket.recv(1024)

# Closing socket
print('Message has been sent!\n')
client_socket.send(quit)
message = client_socket.recv(1024)
print(message)
client_socket.close()
