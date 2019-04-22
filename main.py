print("Loading source files...")
from funcs import *
from gui_main import *
print("Finished loading source files.")


if __name__== '__main__':
	print("Creating App...")
	app = QApplication(sys.argv)
	print("done.")


	print("Creating window...")
	mainWindow = MainWindow()
	print("done.")
	

	print("Starting Loop...")
	sys.exit(app.exec_())
	print("Exiting...")