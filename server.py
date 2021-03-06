__author__ = 'chexiaoyu'

import socket
import spider_class
import convert_json
import MySQLdb
import json
import operation
HOST, PORT = '',8880

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request

    sp = spider_class.Spider()
    sp.start()
    stories = sp.stories

    for item in stories:
        sql = "insert into Cnblogs(recomment, title, author, date, comment, reading) values(％s,%s,%s,%s,%s)"
        conn.execute(sql,item)
    conn.commit()



    js = convert_json.Con_json()
    str_json = js.convert(sp)



    http_response = """
    HTTP/1.1 200 OK

    Hello World!
    """

    client_connection.sendall(http_response)

    client_connection.close()
