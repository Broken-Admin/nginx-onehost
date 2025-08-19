from http.server import BaseHTTPRequestHandler, HTTPServer

class HTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, world!\r\n")

def run(server_class=HTTPServer, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, HTTPHandler)
    print(f'Serving on port {port}...')
    try:
        httpd.serve_forever()
    except :
        pass
    httpd.server_close()

if __name__ == '__main__':
    run()
