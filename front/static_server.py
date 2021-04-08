import http.server
import socketserver
import os

HOST = os.environ.get('HOST', '0.0.0.0')
PORT = int(os.environ.get('PORT', 7000))

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((HOST, PORT), handler) as httpd:
    print(f"Server started at {HOST}:{str(PORT)}")
    httpd.serve_forever()
