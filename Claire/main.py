import sys
import os
import appinfo
from App import App
app = App(os.path.dirname(os.path.realpath(__file__)))
def main(args=sys.argv):
	print(app.get_name())
main()