import argparse
from src.utilities import Utilities
def arguments():
	parser=argparse.ArgumentParser()
	parser.add_argument("-s", type=str, help='Search Name Of Station')
	args=parser.parse_args()
	arg = Utilities(args.s)
	arg.searchRadio()
