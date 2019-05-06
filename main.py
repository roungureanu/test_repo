import time

class Worker:
	def run(self):
		while True:
			print('ok')
			time.sleep(5)

Worker().run()