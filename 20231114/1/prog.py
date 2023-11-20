def objcount(cls):
	class New(cls):
		counter = 0

		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			New.counter += 1

		def __del__(self):
			try:
				super().__del__()
			except:
				pass
			
			New.counter -= 1

	return New


import sys
exec(sys.stdin.read())