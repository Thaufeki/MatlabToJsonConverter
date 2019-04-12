import json
import sys
import numpy
from loadMatFile import loadmat


class MyEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, numpy.integer):
			return int(obj)
		elif isinstance(obj, numpy.floating):
			return float(obj)
		elif isinstance(obj, numpy.ndarray):
			return obj.tolist()
		elif isinstance(obj, bytes):
			#return jwt.encode(obj, 'abracadabra', algorithm='HS256')
			return obj.decode('utf-8')
		else:
			return super(MyEncoder, self).default(obj)
			
def main():
	
	ofile=sys.argv[2]
	data = loadmat(sys.argv[1])
	with open(ofile, 'w') as outfile:
		json.dump(data, outfile, cls=MyEncoder)

if __name__ == "__main__":
	main()