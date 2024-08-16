import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from strong import generate_strong_password
from medium import generate_medium_password
from hard import generate_hard_password  # Assuming you have a module named 'hard' for generating hard passwords

class PasswordManager(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Manager')
        self.setGeometry(200, 200, 600, 400)
        self.setStyleSheet("font-size: 18px;") 

        self.layout = QVBoxLayout()

        self.website_label = QLabel('Website:')
        self.layout.addWidget(self.website_label)

        self.website_input = QLineEdit(self)
        self.layout.addWidget(self.website_input)

        self.generate_strong_button = QPushButton('Generate Strong Password', self)
        self.generate_strong_button.clicked.connect(self.generate_strong_password)
        self.layout.addWidget(self.generate_strong_button)

        self.generate_medium_button = QPushButton('Generate Medium Password', self)
        self.generate_medium_button.clicked.connect(self.generate_medium_password)
        self.layout.addWidget(self.generate_medium_button)

        self.generate_hard_button = QPushButton('Generate Hard Password', self)
        self.generate_hard_button.clicked.connect(self.generate_hard_password)
        self.layout.addWidget(self.generate_hard_button)

        self.password_label = QLabel('Generated Password:')
        self.layout.addWidget(self.password_label)

        self.password_display = QLabel('')
        self.layout.addWidget(self.password_display)

        self.save_button = QPushButton('Save Password', self)
        self.save_button.clicked.connect(self.save_password)
        self.layout.addWidget(self.save_button)

        self.setLayout(self.layout)

    def generate_hard_password(self):
        password = generate_hard_password()
        self.password_display.setText(password)     

    def generate_strong_password(self):
        password = generate_strong_password()
        self.password_display.setText(password)

    def generate_medium_password(self):
        password = generate_medium_password()
        self.password_display.setText(password)

    def save_password(self):
        website = self.website_input.text().strip()
        password = self.password_display.text().strip()

        if not website or not password:
            QMessageBox.warning(self, 'Error', 'Please generate a password and enter a website.')
            return

        # Connect to the SQLite database
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()

        # Create table with an additional column for the website
        c.execute('''CREATE TABLE IF NOT EXISTS passwords
                     (website text, strong_password text, medium_password text, hard_password text)''')

        # Determine if the password is strong, medium, or hard
        strong_password = password if len(password) == 12 else None
        medium_password = password if len(password) == 8 else None
        hard_password = password if len(password) == 16 else None  # Assuming hard passwords are 16 characters long

        # Check if the website already exists
        c.execute("SELECT * FROM passwords WHERE website = ?", (website,))
        row = c.fetchone()

        if row:
            # Update the existing password
            c.execute("UPDATE passwords SET strong_password = ?, medium_password = ?, hard_password = ? WHERE website = ?",
                      (strong_password, medium_password, hard_password, website))
            QMessageBox.information(self, 'Success', 'Password updated successfully.')
        else:
            # Insert a new row of data
            c.execute("INSERT INTO passwords VALUES (?, ?, ?, ?)", (website, strong_password, medium_password, hard_password))
            QMessageBox.information(self, 'Success', 'Password saved successfully.')

        # Save (commit) the changes
        conn.commit()

        # Close the connection
        conn.close()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = PasswordManager()
    ex.show()
    sys.exit(app.exec_())