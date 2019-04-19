import tkinter as tk
from datetime import datetime
import threading

class Window(object):
	
	def __init__(self,root):

		self.thread = None
		self.stopEvent = None
		self.time = None
		self.startOrStop = 0

		self.root = root
		self.root.wm_protocol("WM_DELETE_WINDOW", self.onWindowClose)	#callback to window close function
		self.root.wm_title("Clock")		#Title of window
		self.root.geometry("400x300+200+200")	#Dimension of thee App
		self.root.config(bg="#fff")

		#self.root.wm_attributes("-fullscreen", True)

		self.addWidgets()

	# function that add components or widgets to app
	def addWidgets(self):

		#top frame.. just for show purpose
		self.TopFrame = tk.Frame(self.root, bg="#ff4081", width=400, height=50)
		self.TopFrame.pack(ipadx=10, ipady=10)

		# label to show time
		self.timeLabel = tk.Label(self.root, text="Welcome!", font='Helvetica 18 bold', fg="#333", bg="#fff")
		self.timeLabel.pack(ipadx=10, ipady=20)

		#Button to start or Hide Clock
		self.btn = tk.Button(self.root, text="Start clock", bg="#ff4081", fg="#fff", width=25, height=2, font='Helvetica 10 bold', activebackground="#fff", activeforeground="#ff4081", padx=10, pady=10, command=self.startOrStopClock)
		self.btn.pack()

	def startOrStopClock(self):

		if(self.startOrStop == 0):
			self.startClock()
			self.startOrStop = 1
		else:
			self.stopClock()
			self.startOrStop = 0

	# function to hide Clock
	def stopClock(self):

		self.btn.config(text="Start Clock")
		self.stopEvent.set()


	# function to start the thread and get current time
	def startClock(self):

		self.btn.config(text="Stop Clock")
		self.stopEvent = threading.Event()
		self.thread = threading.Thread(target=self.showTime, args=())
		self.thread.start()


	# display current time continuosly
	def showTime(self):

		try:
			while not self.stopEvent.is_set():
				# getting current time
				self.time = datetime.now().time()

				# setting the time
				self.timeLabel.config(text = "{}:{}:{}".format(self.time.hour, self.time.minute, self.time.second))
 
		except RuntimeError:
			print("RuntimeError")

	# on app close
	def onWindowClose(self):

		self.stopEvent.set()
		self.root.destroy()


app = tk.Tk()
Window = Window(app)
app.mainloop()