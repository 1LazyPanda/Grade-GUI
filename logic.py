from PyQt6.QtWidgets import *
from gui import *
import csv
import os

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        Initialize the Logic class.

        This function initializes the Logic class by calling the constructor of the superclass
        and setting up the user interface. It also connects the submit button and clear button
        to their respective methods.

        :param None: No parameters are accepted.
        :return None: No value is returned.
        """
        # Call the constructor of the superclass
        super().__init__()

        # Set up the user interface
        self.setupUi(self)

        # Connect the submit button to the submit method
        self.SubmitButton.clicked.connect(self.submit)

        # Connect the text changes of the input fields to the respective methods
        self.attempts_input.textChanged.connect(self.score)
        self.name_input.textChanged.connect(self.get_name)
        self.score1_input.textChanged.connect(self.get_score)
        self.score2_input.textChanged.connect(self.get_score)
        self.score3_input.textChanged.connect(self.get_score)
        self.score4_input.textChanged.connect(self.get_score)

    def submit(self) -> None:
        """
        Submit the current score to a CSV file.

        This function retrieves the name and scores from the input fields, calculates the
        final score, and writes the data to the CSV file. If the file does not exist, it
        creates it with a header row.

        Returns:
            None
        """
        try:
            # Get the name from the name input field
            name: str = self.name_input.text()

            # Get the scores from the score input fields
            score1: int = self.get_score(self.score1_input.text())
            score2: int = self.get_score(self.score2_input.text())
            score3: int = self.get_score(self.score3_input.text())
            score4: int = self.get_score(self.score4_input.text())

            # Calculate the final score by averaging the scores
            final_score: int = (score1 + score2 + score3 + score4) // 4

            # Specify the path to the CSV file
            csv_file_path: str = 'data.csv'

            # Check if the file exists
            file_exists: bool = os.path.exists(csv_file_path)

            if file_exists:
                # Check if the file is empty
                file_empty: bool = os.path.getsize(csv_file_path) == 0
            else:
                file_exists = True

            # Open the CSV file in append mode
            with open(csv_file_path, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)

                # If the file is new or empty, write the header row
                if not file_exists or file_empty:
                    writer.writerow(["Name", "Score 1", "Score 2", "Score 3",
                                     "Score 4", "Final Score"])

                # Write the score data to the CSV file
                writer.writerow([name, score1, score2, score3, score4, final_score])

            # Clear the input fields
            self.clear_inputs()

            # Display a success message
            self.suboutput_label.setVisible(True)
            self.suboutput_label.setText("Your score has been submitted!")
            self.suboutput_label.setStyleSheet("color: Gold;")

        except ValueError:
            # Clear the input fields if any input is invalid
            self.clear_inputs()


    def clear_inputs(self) -> None:
        """
        Clear all input fields and reset their visibility.

        This function takes no arguments and returns nothing.
        """
        # Clear the name input field
        self.name_input.clear()  # type: QLineEdit

        # Clear the attempts input field
        self.attempts_input.clear()  # type: QLineEdit

        # Reset the visibility of the score1 label and input field
        self.score1_label.setVisible(False)  # type: QLabel
        self.score1_input.setVisible(False)  # type: QLineEdit
        self.score1_input.clear()  # type: None

        # Reset the visibility of the score2 label and input field
        self.score2_label.setVisible(False)  # type: QLabel
        self.score2_input.setVisible(False)  # type: QLineEdit
        self.score2_input.clear()  # type: None

        # Reset the visibility of the score3 label and input field
        self.score3_label.setVisible(False)  # type: QLabel
        self.score3_input.setVisible(False)  # type: QLineEdit
        self.score3_input.clear()  # type: None

        # Reset the visibility of the score4 label and input field
        self.score4_label.setVisible(False)  # type: QLabel
        self.score4_input.setVisible(False)  # type: QLineEdit
        self.score4_input.clear()  # type: None

        # Reset the visibility of the suboutput label and clear its contents
        self.suboutput_label.setVisible(False)  # type: QLabel
        self.suboutput_label.clear()  # type: None
    
    def clear_score(self) -> None:
        """
        Clear the attempts input field and reset the visibility of the score labels and input fields.

        This function takes no arguments and returns nothing.
        """
        # Clear the attempts input field
        self.attempts_input.clear()  # type: None

        # Reset the visibility of the score labels and input fields
        self._reset_score_visibility()

        # Reset the visibility of the suboutput label and clear its contents
        self.suboutput_label.setVisible(False)  # type: bool
        self.suboutput_label.clear()  # type: None

    def _reset_score_visibility(self) -> None:
        """
        Reset the visibility of the score labels and input fields.

        This function takes no arguments and returns nothing.
        """
        # Reset the visibility of the score1 label and input field
        self.score1_label.setVisible(False)  # type: bool
        self.score1_input.setVisible(False)  # type: bool
        self.score1_input.clear()  # type: None

        # Reset the visibility of the score2 label and input field
        self.score2_label.setVisible(False)  # type: bool
        self.score2_input.setVisible(False)  # type: bool
        self.score2_input.clear()  # type: None

        # Reset the visibility of the score3 label and input field
        self.score3_label.setVisible(False)  # type: bool
        self.score3_input.setVisible(False)  # type: bool
        self.score3_input.clear()  # type: None

        # Reset the visibility of the score4 label and input field
        self.score4_label.setVisible(False)  # type: bool
        self.score4_input.setVisible(False)  # type: bool
        self.score4_input.clear()  # type: None
    
         


    def get_name(self, name_text: str) -> None:
        """
        Get the name of the current player.

        This function takes a string argument representing the text of the name input
        field and returns nothing. It checks if the name is valid (contains only letters)
        and if not, clears the name input field.

        Parameters:
            name_text (str): The text of the name input field.

        Returns:
            None
        """
        # Check if the name is valid
        try:
            name = self.name_input.text().strip()
            if not name.isalpha():
                # The name is not valid, raise a ValueError
                raise ValueError
            
        except ValueError:
            # Clear the name input field
            self.name_input.clear()



    def get_score(self, score_text: str) -> int:
        """
        Get the score of the current player.

        This function takes a string argument representing the text of the score input
        field and returns an integer representing the score. It checks if the score is
        within the valid range, and if not, clears the score input field and displays
        an error message in the suboutput label.

        Parameters:
            score_text (str): The text of the score input field.

        Returns:
            int: The score of the current player.
        """
        try:
            # Strip the score text to remove any leading or trailing whitespace
            # and convert it to an integer
            score = int(score_text.strip())
            
            # Check if the score is within the valid range
            if 0 <= score <= 100:
                # The score is valid, so hide the suboutput label and clear its text
                self.suboutput_label.setVisible(False)
                self.suboutput_label.clear()
                # Return the score
                return score
            
            # If the score is out of the valid range, show the suboutput label
            # and set its text to an error message
            else:
                self.suboutput_label.setVisible(True)
                self.suboutput_label.setText(
                    "Please enter a valid score between 0 and 100."
                )
                self.suboutput_label.setStyleSheet("color: orange;")
                # Return 0 for out-of-range scores
                return 0  # Return 0 for out-of-range scores
            
        except ValueError:
            # If the score text is not a valid integer, show the suboutput label
            # and set its text to an error message
            self.suboutput_label.setVisible(True)
            self.suboutput_label.setText(
                "All scores must be valid integers."
            )
            self.suboutput_label.setStyleSheet("color: red;")
            # Return 0 for invalid scores
            return 0
            

    def score(self) -> None:
        """
        Handle the score input based on the number of attempts.

        This function takes no arguments.

        Returns:
            None
        """
        try:
            # Get the number of attempts from the input field as an integer
            attempts: int = int(self.attempts_input.text())
            
            # Check if the number of attempts is within the valid range
            if attempts < 1 or attempts > 4:
                # If not, raise a ValueError
                raise ValueError
            
            # Show the score1 label and input field if there is at least one attempt
            if attempts >= 1:
                self.score1_label.setVisible(True)
                self.score1_input.setVisible(True)

            # Show the score2 label and input field if there are at least two attempts
            if attempts >= 2:
                self.score2_label.setVisible(True)
                self.score2_input.setVisible(True)
            # If there are less than two attempts, hide the score2 label and input field
            elif attempts < 2:
                self.score2_label.setVisible(False)
                self.score2_input.setVisible(False)
                self.score2_input.clear()

            # Show the score3 label and input field if there are at least three attempts
            if attempts >= 3:
                self.score3_label.setVisible(True)
                self.score3_input.setVisible(True)
            # If there are less than three attempts, hide the score3 label and input field
            elif attempts < 3:
                self.score3_label.setVisible(False)
                self.score3_input.setVisible(False)
                self.score3_input.clear()

            # Show the score4 label and input field if there are exactly four attempts
            if attempts == 4:
                self.score4_label.setVisible(True)
                self.score4_input.setVisible(True)
            # If there are less than four attempts, hide the score4 label and input field
            elif attempts < 4:
                self.score4_label.setVisible(False)
                self.score4_input.setVisible(False)
                self.score4_input.clear()
    
        except ValueError:
            # If the number of attempts is not a valid integer, show the suboutput label
            # and set its text to an error message
            self.suboutput_label.setVisible(True)
            self.suboutput_label.setText(
                "Please enter a valid attempts between 1 and 4."
            )
            self.suboutput_label.setStyleSheet("color: Blue;")
            #self.clear_score()
       
        #try: 
            
            #if attempts < 0 or attempts is None:
                #raise ValueError
            #self.suboutput_label.setVisible(False)
