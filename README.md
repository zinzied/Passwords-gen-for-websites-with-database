## Project Description

This project is a Password Manager application built using Python and PyQt5. The application allows users to generate and save passwords of varying strengths (strong, medium, and hard) for different websites. The passwords are stored securely in an SQLite database.

### Features

- **Password Generation**: The application can generate strong, medium, and hard passwords using predefined criteria.
- **User Interface**: A graphical user interface (GUI) built with PyQt5 allows users to interact with the application easily.
- **Password Storage**: Generated passwords can be saved to an SQLite database, which includes the website associated with each password.
- **Password Management**: Users can update existing passwords for a website or add new ones.

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/Passwords-gen-for-websites-with-database.git
    cd Passwords-gen-for-websites-with-database
    ```

2. **Install the required dependencies**:
    ```sh
    pip install PyQt5
    ```

3. **Ensure you have SQLite installed** (SQLite is usually included with Python).

### Usage

1. **Run the application**:
    ```sh
    python main.py
    ```

2. **Generate Passwords**:
    - Enter the website name in the provided input field.
    - Click on "Generate Strong Password", "Generate Medium Password", or "Generate Hard Password" to generate a password of the desired strength.
    - The generated password will be displayed in the application.

3. **Save Passwords**:
    - After generating a password, click on "Save Password" to store it in the SQLite database.
    - If the website already exists in the database, the password will be updated.
    - After make passwords you can shows them by open :
    ```sh
    python db.py
    ```

4. **User Interface (UI) Setup:**
   - The main window is set up with a title "Password Manager" and a specific size.
   - The UI includes a label, a list box to display saved passwords, a search entry field, and buttons for searching and showing all passwords.

5. **Password Display:**
   - The `show_passwords` method prompts the user to enter a predefined PIN. If the PIN is correct, it connects to an SQLite database (`passwords.db`), fetches all saved passwords, and displays them in the list box.
   - If the PIN is incorrect, a warning message is shown.

4. **Password Search:**
   - The `search_passwords` method allows the user to search for passwords by website. It connects to the SQLite database, fetches rows that match the search term, and displays the results in the list box.

5. **Context Menu for Copying Passwords:**
   - The list box supports a context menu that appears on right-click. This menu includes an option to copy the selected password to the clipboard.
   - The `copy_password` method extracts the password from the selected list item and copies it to the system clipboard.

8. **Database Interaction:**
   - The application interacts with an SQLite database named `passwords.db`. It assumes the database has a table named `passwords` with columns for website and different types of passwords (strong, medium, hard).

9. **Security:**
   - A predefined PIN is used to restrict access to the full list of passwords.

Here is a high-level summary of the main components:

- **Imports:** Necessary modules from PyQt5 and sqlite3.
- **Constants:** A predefined PIN for verification.
- **PasswordManager Class:** The main class that sets up the UI and handles interactions.
- **Main Execution Block:** Initializes the application, applies the dark theme, and starts the event loop.

This code provides a basic but functional password manager with a graphical interface, search functionality, and clipboard integration for copying passwords.
### Modules

- **strong.py**: Contains the function `generate_strong_password` to generate strong passwords.
- **medium.py**: Contains the function `generate_medium_password` to generate medium-strength passwords.
- **hard.py**: Contains the function `generate_hard_password` to generate hard passwords.

### Database Schema

The SQLite database (`passwords.db`) contains a table named `passwords` with the following columns:
- `website`: The name of the website.
- `strong_password`: The strong password associated with the website.
- `medium_password`: The medium password associated with the website.
- `hard_password`: The hard password associated with the website.

### Example

```python
password = generate_strong_password(12)
print(password)  # Outputs a random 12-character strong password
```

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

### License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---
