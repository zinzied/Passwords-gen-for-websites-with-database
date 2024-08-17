import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QListWidget, QInputDialog, QMessageBox, QMenu
from PyQt5.QtGui import QClipboard
from PyQt5.QtCore import Qt

# Predefined PIN for verification
PREDEFINED_PIN = "1234" #here set your pin to can show the passwords saved in database 

class DatabaseManager(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Manager')
        self.setGeometry(200, 200, 700, 600)  # Set the window size
        self.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
                color: #ffffff;
                font-size: 18px;
            }
            QLabel {
                color: #ffffff;
            }
            QLineEdit {
                background-color: #3c3c3c;
                color: #ffffff;
                border: 1px solid #555555;
                padding: 5px;
            }
            QListWidget {
                background-color: #3c3c3c;
                color: #ffffff;
                border: 1px solid #555555;
            }
            QInputDialog, QMessageBox {
                background-color: #3c3c3c;
                color: #ffffff;
                border: 1px solid #555555;
            }
            QPushButton {
                background-color: #555555;
                color: #ffffff;
                border: 1px solid #555555;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #666666;
            }
            QPushButton:pressed {
                background-color: #777777;
            }
        """)

        self.layout = QVBoxLayout()

        self.label = QLabel('Saved Passwords')
        self.layout.addWidget(self.label)

        self.listbox = QListWidget(self)
        self.listbox.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listbox.customContextMenuRequested.connect(self.show_context_menu)
        self.listbox.setMinimumSize(580, 300)  # Set the minimum size of the listbox
        self.layout.addWidget(self.listbox)

        self.search_entry = QLineEdit(self)
        self.search_entry.setPlaceholderText('Search by website')
        self.layout.addWidget(self.search_entry)

        self.search_button = QPushButton('Search', self)
        self.search_button.clicked.connect(self.search_passwords)
        self.layout.addWidget(self.search_button)

        self.show_button = QPushButton('Show All Passwords', self)
        self.show_button.clicked.connect(self.show_passwords)
        self.layout.addWidget(self.show_button)

        self.setLayout(self.layout)

    def show_passwords(self):
        pin, ok = QInputDialog.getText(self, 'Enter PIN', 'Enter PIN:', QLineEdit.Password)
        if ok and pin == PREDEFINED_PIN:
            # Connect to the SQLite database
            conn = sqlite3.connect('passwords.db')
            c = conn.cursor()

            # Fetch all rows from the passwords table
            c.execute("SELECT website, strong_password, medium_password, hard_password FROM passwords")
            rows = c.fetchall()

            # Close the connection
            conn.close()

            # Clear the listbox before inserting new items
            self.listbox.clear()

            # Display the passwords and websites in the GUI
            for row in rows:
                website = row[0]
                password = row[1] or row[2] or row[3]  # Display the first non-null password
                self.listbox.addItem(f"Website: {website}: Password: {password}")
        else:
            QMessageBox.warning(self, 'Error', 'Incorrect PIN')

    def search_passwords(self):
        search_term = self.search_entry.text().strip().lower()

        # Connect to the SQLite database
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()

        # Fetch rows that match the search term
        c.execute("SELECT website, strong_password, medium_password, hard_password FROM passwords WHERE lower(website) LIKE ?", ('%' + search_term + '%',))
        rows = c.fetchall()

        # Close the connection
        conn.close()

        # Clear the listbox before inserting new items
        self.listbox.clear()

        # Display the matching passwords and websites in the GUI
        for row in rows:
            website = row[0]
            password = row[1] or row[2] or row[3]  # Display the first non-null password
            self.listbox.addItem(f"Website: {website}: Password: {password}")

    def show_context_menu(self, position):
        menu = QMenu()
        copy_action = menu.addAction("Copy Password")
        action = menu.exec_(self.listbox.viewport().mapToGlobal(position))
        if action == copy_action:
            self.copy_password()

    def copy_password(self):
        selected_item = self.listbox.currentItem()
        if selected_item:
            text = selected_item.text()
            # Extract the password from the text
            password = text.split("Password: ")[1]
            # Copy the password to the clipboard
            clipboard = QApplication.clipboard()
            clipboard.setText(password)
            QMessageBox.information(self, 'Copied', 'Password copied to clipboard.')

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    # Apply dark theme stylesheet
    dark_stylesheet = """
    QWidget {
        background-color: #2b2b2b;
        color: #ffffff;
    }
    QLineEdit, QListWidget, QInputDialog, QMessageBox {
        background-color: #3c3c3c;
        color: #ffffff;
        border: 1px solid #555555;
    }
    QPushButton {
        background-color: #555555;
        color: #ffffff;
        border: 1px solid #555555;
        padding: 5px;
    }
    QPushButton:hover {
        background-color: #666666;
    }
    QPushButton:pressed {
        background-color: #777777;
    }
    """
    app.setStyleSheet(dark_stylesheet)

    ex = DatabaseManager()
    ex.show()
    sys.exit(app.exec_())
