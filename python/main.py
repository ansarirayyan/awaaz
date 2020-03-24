import pyperclip
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from pynput import mouse
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from actions import v_number, play_music


keyboard = KeyboardController()
mouse = MouseController()


# variables for mouse corrdinates

joinCallX = -1072
joinCallY = 539

sendMsgX = -1456
sendMsgY = 987


#while True:
#    time.sleep(4) # Delay for 1 minute (60 seconds).
#    print("This prints once a minute.")
#    keyboard.press(Key.ctrl_l)
#    keyboard.press('a')
#    keyboard.release('a')
#    keyboard.release(Key.ctrl_l)
#
#    keyboard.press(Key.ctrl_l)
#    keyboard.press('c')
#    keyboard.release('c')
#    keyboard.release(Key.ctrl_l)
#
#    keyboard.press(Key.alt)
#    keyboard.press(Key.tab)
#    time.sleep(4)
#    keyboard.release(Key.tab)
#    keyboard.release(Key.alt)
#
#
#    print(pyperclip.paste())


def oprintniftree(latestMsg):
    print(latestMsg)
    # if prevMsg != latestMsg:
    if latestMsg == 'awaaz -v':
        v_number()
    if "awaaz play " in latestMsg:
            audio = latestMsg.replace('awaaz play ', '')
            pyperclip.copy("Your request is being processed...")
            keyboard.press(Key.ctrl_l)
            keyboard.press('v')
            keyboard.release('v')
            keyboard.release(Key.ctrl_l)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            play_music(audio)


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
		# prevMsg = latestMsg
if __name__ == '__main__':
	httpd = HTTPServer(("localhost", 42069), Handler)
	try:
		print("Starting http server on http://localhost:42069/")
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
