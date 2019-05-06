import time

class Worker:
	def run(self):
		while True:
			try:
				with open(r'D:\temp\whatever.txt', 'a') as handle:
					handle.write('ok\n')
			except Exception as exc:
				pass
			print('ok')
			time.sleep(5)

Worker().run()