import pyperclip
from pynput.keyboard import Key, Controller as KeyboardController
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from actions import v_number, play_music, spam, antifbi, join_call

keyboard = KeyboardController()


def oprintniftree(latestMsg):
    file = open("prevMsg","r+")
    print(latestMsg)
    if latestMsg != file:
        if "awaaz" in latestMsg: # command prefix
            if "-v" in latestMsg:
                v_number()
            if "play " in latestMsg:
                audio = latestMsg.replace('awaaz play ', '')
                pyperclip.copy("Your request is being processed...")
                keyboard.press(Key.ctrl_l)
                keyboard.press('v')
                keyboard.release('v')
                keyboard.release(Key.ctrl_l)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                play_music(audio)
            if "spam" in latestMsg:
                i = 4
                while True:
                    spam()
                    i = i - 1
                    if (i == 0):
                        break;
            if "anti-fbi" in latestMsg:
                antifbi()
            if "join call" in latestMsg:
                pyperclip.copy("Your request is being processed...")
                keyboard.press(Key.ctrl_l)
                keyboard.press('v')
                keyboard.release('v')
                keyboard.release(Key.ctrl_l)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                join_call()
            file.write(latestMsg)
            file.close()


class Handler(BaseHTTPRequestHandler):
	# await instructions from the chrome extension on what to type
	def do_GET(self):
		self.send_response(400)
		self.send_header("Content-Type", "text/html")
		self.send_header("Access-Control-Allow-Origin", "*")
		self.end_headers()
		self.wfile.write(b"<h1 align='center'>Please send a POST request using the chrome extension!</h1>")
	def do_POST(self):
		self.send_response(200)
		self.send_header('Content-Type', 'text/plain')
		self.send_header("Access-Control-Allow-Origin", "*")
		self.end_headers()
		typing_string = self.rfile.read(int(self.headers['Content-Length']))
		oprintniftree(typing_string.decode())
if __name__ == '__main__':
	httpd = HTTPServer(("localhost", 42069), Handler)
	try:
		print("Starting http server on http://localhost:42069/")
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
