class Matrix33:

	"""
	A 3x3 rotation matrix; M^T M=identity, det(M)=1.    Stored in OpenGL column-major format.
	"""

	# Member 1,1 (top left)
	m_11: float = 1.0

	# Member 2,1
	m_21: float = 0.0

	# Member 3,1 (bottom left)
	m_31: float = 0.0

	# Member 1,2
	m_12: float = 0.0

	# Member 2,2
	m_22: float = 1.0

	# Member 3,2
	m_32: float = 0.0

	# Member 1,3 (top right)
	m_13: float = 0.0

	# Member 2,3
	m_23: float = 0.0

	# Member 3,3 (bottom left)
	m_33: float = 1.0

	def __init__(self, arg=None, template=None):
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.m_11 = 1.0
		self.m_21 = 0.0
		self.m_31 = 0.0
		self.m_12 = 0.0
		self.m_22 = 1.0
		self.m_32 = 0.0
		self.m_13 = 0.0
		self.m_23 = 0.0
		self.m_33 = 1.0

	def read(self, stream):

		self.io_start = stream.tell()
		self.m_11 = stream.read_float()
		self.m_21 = stream.read_float()
		self.m_31 = stream.read_float()
		self.m_12 = stream.read_float()
		self.m_22 = stream.read_float()
		self.m_32 = stream.read_float()
		self.m_13 = stream.read_float()
		self.m_23 = stream.read_float()
		self.m_33 = stream.read_float()

		self.io_size = stream.tell() - self.io_start

	def write(self, stream):

		self.io_start = stream.tell()
		stream.write_float(self.m_11)
		stream.write_float(self.m_21)
		stream.write_float(self.m_31)
		stream.write_float(self.m_12)
		stream.write_float(self.m_22)
		stream.write_float(self.m_32)
		stream.write_float(self.m_13)
		stream.write_float(self.m_23)
		stream.write_float(self.m_33)

		self.io_size = stream.tell() - self.io_start

	def __repr__(self):
		s = 'Matrix33 [Size: '+str(self.io_size)+', Address:'+str(self.io_start)+']'
		s += '\n	* m_11 = ' + self.m_11.__repr__()
		s += '\n	* m_21 = ' + self.m_21.__repr__()
		s += '\n	* m_31 = ' + self.m_31.__repr__()
		s += '\n	* m_12 = ' + self.m_12.__repr__()
		s += '\n	* m_22 = ' + self.m_22.__repr__()
		s += '\n	* m_32 = ' + self.m_32.__repr__()
		s += '\n	* m_13 = ' + self.m_13.__repr__()
		s += '\n	* m_23 = ' + self.m_23.__repr__()
		s += '\n	* m_33 = ' + self.m_33.__repr__()
		s += '\n'
		return s
