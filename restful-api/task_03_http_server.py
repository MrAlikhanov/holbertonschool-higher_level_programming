#!/usr/bin/env python3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
              if self.path == "/":
            self._send_text_response(200, "Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_json_response(200, data)
        elif self.path == "/status":
            self._send_text_response(200, "OK")
        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            self._send_json_response(200, info)
        else:
            self._send_text_response(404, "Endpoint not found")


    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)
        try:
            received = json.loads(body)
            response = {"status": "received", "data": received}
            self._send_json_response(200, response)
        except json.JSONDecodeError:
            self._send_json_response(400, {"error": "Invalid JSON body"})
    def _send_text_response(self, status_code: int, message: str):

      
        encoded = message.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)


    def _send_json_response(self, status_code: int, data: dict):
        encoded = json.dumps(data, indent=2).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)
    def log_message(self, fmt, *args):
        print(f"[{self.log_date_time_string()}] {fmt % args}")
      
def run(host: str = "localhost", port: int = 8000):
    server_address = (host, port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server running at http://{host}:{port}")
    print("Available endpoints:")
    print(f"  GET  http://{host}:{port}/        → greeting message")
    print(f"  GET  http://{host}:{port}/data    → sample JSON dataset")
    print(f"  GET  http://{host}:{port}/status  → API status")
    print(f"  GET  http://{host}:{port}/info    → API metadata")
    print(f"  POST http://{host}:{port}/        → echo JSON body")
    print("Press Ctrl+C to stop.\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()
if __name__ == "__main__":
    run()
