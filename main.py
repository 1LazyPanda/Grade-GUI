from logic import *


def main() -> None:
    """
    Initializes the application and displays the main window.

    This function creates a QApplication object, a Logic object
    which represents the main window, and starts the application event loop.

    Args:
        None

    Returns:
        None
    """
    # Create a QApplication object
    application: QApplication = QApplication([])  # Create a QApplication object

    # Create a Logic object which represents the main window
    window: Logic = Logic()  # Create a Logic object

    # Show the main window
    window.show()  # Show the main window

    # Start the application event loop
    application.exec()  # Start the application event loop

if __name__ == "__main__":
    main()