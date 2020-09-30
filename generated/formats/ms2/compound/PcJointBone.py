import typing


class PcJointBone:
	floats: typing.List[float]

	def __init__(self, arg=None, template=None):
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.floats = []

	def read(self, stream):

		io_start = stream.tell()
		self.floats = [stream.read_float() for _ in range(12)]

		self.io_size = stream.tell() - io_start

	def write(self, stream):

		io_start = stream.tell()
		for item in self.floats: stream.write_float(item)

		self.io_size = stream.tell() - io_start

	def __repr__(self):
		s = 'PcJointBone [Size: '+str(self.io_size)+']'
		s += '\n	* floats = ' + self.floats.__repr__()
		s += '\n'
		return s
