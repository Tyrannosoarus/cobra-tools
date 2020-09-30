class Root0:
	zero_0: int
	zero_1: int
	collection_count: int
	zero_4: int

	def __init__(self, arg=None, template=None):
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.zero_0 = 0
		self.zero_1 = 0
		self.collection_count = 0
		self.zero_4 = 0

	def read(self, stream):

		io_start = stream.tell()
		self.zero_0 = stream.read_uint()
		self.zero_1 = stream.read_uint()
		self.collection_count = stream.read_uint()
		self.zero_4 = stream.read_uint()

		self.io_size = stream.tell() - io_start

	def write(self, stream):

		io_start = stream.tell()
		stream.write_uint(self.zero_0)
		stream.write_uint(self.zero_1)
		stream.write_uint(self.collection_count)
		stream.write_uint(self.zero_4)

		self.io_size = stream.tell() - io_start

	def __repr__(self):
		s = 'Root0 [Size: '+str(self.io_size)+']'
		s += '\n	* zero_0 = ' + self.zero_0.__repr__()
		s += '\n	* zero_1 = ' + self.zero_1.__repr__()
		s += '\n	* collection_count = ' + self.collection_count.__repr__()
		s += '\n	* zero_4 = ' + self.zero_4.__repr__()
		s += '\n'
		return s
