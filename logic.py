from PyQt6.QtWidgets import *
from gui import *
import csv
import os

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """
        Initialize the Logic class.

        This function initializes the Logic class by calling the constructor of the superclass
        and setting up the user interface. It also connects the submit button and clear button
        to their respective methods.

        Parameters:
            None

        Returns:
            None
        """
        # Call the constructor of the superclass
        super().__init__()
        # Set up the user interface
        self.setupUi(self)
        
        # Connect the submit button to the submit method
        self.SubmitButton.clicked.connect(self.submit)
        self.attempts_input.textChanged.connect(self.score)
        self.name_input.textChanged.connect(self.get_name)
        self.score1_input.textChanged.connect(self.get_score)
        self.score2_input.textChanged.connect(self.get_score)
        self.score3_input.textChanged.connect(self.get_score)
        self.score4_input.textChanged.connect(self.get_score)

    def submit(self):
        try: 
            name = self.name_input.text()
            score1 = self.get_score(self.score1_input.text())
            score2 = self.get_score(self.score2_input.text())
            score3 = self.get_score(self.score3_input.text())
            score4 = self.get_score(self.score4_input.text())
            final_score= (score1 + score2 + score3 + score4)//4

            csv_file_path = 'data.csv'
            file_exists = os.path.exists(csv_file_path)
            if file_exists:
                file_empty = os.path.getsize(csv_file_path) == 0
            else:
                file_exists = True

            with open(csv_file_path, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)

                if not file_exists or file_empty:
                    writer.writerow(["Name  ", "  Score 1  ", "  Score 2  ", "  Score 3  ", "  Score 4  ", "  Final Score"])
                
                writer.writerow([name , score1, score2, score3, score4, final_score])

            self.clear_inputs()
            self.suboutput_label.setVisible(True)
            self.suboutput_label.setText("Your score has been submitted!")
            self.suboutput_label.setStyleSheet("color: Gold;")


            

        except ValueError:
            self.clear_inputs()


    def clear_inputs(self):
        self.name_input.clear()
        self.attempts_input.clear()

        self.score1_label.setVisible(False)
        self.score1_input.setVisible(False)
        self.score1_input.clear()

        self.score2_label.setVisible(False)
        self.score2_input.setVisible(False)
        self.score2_input.clear()

        self.score3_label.setVisible(False)
        self.score3_input.setVisible(False)
        self.score3_input.clear()

        self.score4_label.setVisible(False)
        self.score4_input.setVisible(False)
        self.score4_input.clear()

        self.suboutput_label.setVisible(False)
        self.suboutput_label.clear()
    
    def clear_score(self):
        self.attempts_input.clear()

        self.score1_label.setVisible(False)
        self.score1_input.setVisible(False)
        self.score1_input.clear()

        self.score2_label.setVisible(False)
        self.score2_input.setVisible(False)
        self.score2_input.clear()

        self.score3_label.setVisible(False)
        self.score3_input.setVisible(False)
        self.score3_input.clear()

        self.score4_label.setVisible(False)
        self.score4_input.setVisible(False)
        self.score4_input.clear()

        self.suboutput_label.setVisible(False)
        self.suboutput_label.clear()
    
         


    def get_name(self, name_text):
        try:
            name = self.name_input.text().strip()
            if not name.isalpha():
                raise ValueError
            
        except ValueError:
            self.name_input.clear()



    def get_score(self, score_text):
        try:
            score = int(score_text.strip())
            
            if 0 <= score <= 100:  # Valid score range
                self.suboutput_label.setVisible(False)
                self.suboutput_label.clear()
                return score
            
            elif score < 0 or score > 100:  # Score is out of valid range
                self.suboutput_label.setVisible(True)
                self.suboutput_label.setText(
                    "Please enter a valid score between 0 and 100."
                )
                self.suboutput_label.setStyleSheet("color: orange;")
                return 0  # Return 0 for out-of-range scores
            
            else:
                raise ValueError("Invalid score format.")  # Catch any other invalid format
                    
        except ValueError:
            self.suboutput_label.setVisible(True)
            self.suboutput_label.setText(
                "All scores must be valid integers."
            )
            self.suboutput_label.setStyleSheet("color: red;")
            return 0 
            

    def score(self):
        try:
            attempts = int(self.attempts_input.text())
            
            if attempts < 1 or attempts > 4:
                raise ValueError
            
            if attempts >= 1:
                    self.score1_label.setVisible(True)
                    self.score1_input.setVisible(True)

            if attempts >= 2:
                    self.score2_label.setVisible(True)
                    self.score2_input.setVisible(True)
            elif attempts < 2:
                    self.score2_label.setVisible(False)
                    self.score2_input.setVisible(False)
                    self.score2_input.clear()

            if attempts >= 3:
                    self.score3_label.setVisible(True)
                    self.score3_input.setVisible(True)
            elif attempts < 3:
                    self.score3_label.setVisible(False)
                    self.score3_input.setVisible(False)
                    self.score3_input.clear()

            if attempts == 4:
                    self.score4_label.setVisible(True)
                    self.score4_input.setVisible(True)
            elif attempts < 4:
                    self.score4_label.setVisible(False)
                    self.score4_input.setVisible(False)
                    self.score4_input.clear()
    
        except ValueError:
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