from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 8000

print("Servidor ejecutándose en puerto", PORT)

with TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()

