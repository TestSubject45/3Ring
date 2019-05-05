print("Loading source files...")
from gui_main import *
from funcs import *
print("Finished loading source files.\n")
from config import *

if __name__== '__main__':
	print("Creating App...")
	app = QApplication(sys.argv)
	print("done.")


	print("Creating window...")
	mainWindow = MainWindow()
	print("done.")

	print("Starting Loop...")
	sys.exit(app.exec_())
	writeToFile("data/pagesList","csv",pagesList)
	print("Exiting...")