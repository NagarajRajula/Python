import threading 

barrier = threading.Barrier(3) 

class thread(threading.Thread): 
	def __init__(self, thread_ID): 
		threading.Thread.__init__(self) 
		self.thread_ID = thread_ID 
	def run(self): 
		print(str(self.thread_ID) + "\n") 
		barrier.wait() 
		
thread1 = thread(100) 
thread2 = thread(101) 

thread1.start() 
barrier.wait() 

thread2.start()


print("Exit\n") 
