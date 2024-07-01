class Queue():
	def __init__(self) -> None:
		self.queue = []
	
	def enqueue(self, elem) -> None:
		self.queue.append(elem)

		return
	
	def dequeue(self):
		if not self.isempty():
			return self.queue.pop(0)
		else:
			return None

	def isempty(self) -> bool:
		return len(self.queue) == 0

