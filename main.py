print("Loading source files...")
from gui_main import *
print("Finished loading source files.")


if __name__== '__main__':
	app = QApplication(sys.argv)
	dashboard = Dashboard()

	sys.exit(app.exec_())