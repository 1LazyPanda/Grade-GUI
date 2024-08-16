from logic import *


def main():
    """
    This function initializes the application and displays the main window.

    It creates a QApplication object and a Logic object. The Logic object
    represents the main window of the application. Finally, it shows the main
    window and starts the application event loop.
    """
    # Create a QApplication object
    application = QApplication([])

    # Create a Logic object which represents the main window
    window = Logic()

    # Show the main window
    window.show()

    # Start the application event loop
    application.exec()

if __name__ == "__main__":
    main()