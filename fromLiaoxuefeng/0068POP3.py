#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

def POP3_do():
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
    #print(mails)

    index = len(mails)
    resp, lines, octets = server.retr(index)

    msg_content = b'\r\n'.join(lines).decode('utf-8')
    msg = Parser().parsestr(msg_content)  	# --> Message
    print_info(msg, 0)
    server.quit()
	
def print_info(msg, indent = 0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' %(name,addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if msg.is_multipart():
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s%s' % ('  ' * indent, '-' * 10))
            print_info(part, indent + 1)
    else :
        content_type = msg.get_content_type()
        if content_type == 'text/pain' or content_type == 'text/html':
            content = msg.get_payload(decode = True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttchment: %s' % ('  ' * indent, content_type))
			
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value
	
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0 :
            charset = content_type[pos + 8:].strip()
    return charset
	
if __name__ == '__main__':
    POP3_do()