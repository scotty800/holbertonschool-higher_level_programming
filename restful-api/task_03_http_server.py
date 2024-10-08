#!/usr/bin/python3

import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class Serv(BaseHTTPRequestHandler):
    def do_Get(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'ok')

        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'Endpoint not found')


def run(server_class=HTTPServer, handler_class=Serv, port=8000):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Serving on port {}...".format(port))
    httpd.serve_forever()


if __name__ == '__main__':
    run()
