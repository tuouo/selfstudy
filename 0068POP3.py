#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import poplib

# email = input("Email: ")
# password = input("Password: ")
# pop_sever = input("POP3 server: ")
email = '@163.com'
password = ''
pop_sever = 'pop.163.com'

server = poplib.POP3(pop_sever)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

server.user(email)
server.pass_(password)

print("All Messages number: %s. Size: %s" % server.stat())
resp, mails, octets = server.list()
print(mails)

index = len(mails)
resp, lines, octets = server.retr(index)

msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(msg_content)
server.quit()