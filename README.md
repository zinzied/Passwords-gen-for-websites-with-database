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
    git clone https://github.com/yourusername/password-manager.git
    cd password-manager
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
