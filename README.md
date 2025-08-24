# Streamlit Password Manager

A simple and interactive web application built with Streamlit to generate, hash, and store strong passwords. The app also allows users to view previously generated passwords in a structured format.

## Features

- **Generate Strong Passwords:**  
  Generate secure passwords using uppercase, lowercase, numbers, and symbols.
  
- **Password Security Tips:**  
  Provides tips for creating strong passwords, such as using at least 12 characters and avoiding personal information.
  
- **Password Storage:**  
  Passwords are securely stored in an SQLite database after being hashed using `werkzeug.security`.
  
- **View Stored Passwords:**  
  View all previously generated passwords along with their creation timestamp in a tabular format.

- **Interactive UI:**  
  Built with Streamlit for a responsive and user-friendly interface.

## How It Works

1. Users can navigate between pages using the sidebar:
   - Home: Learn about password security and tips.
   - Generate Password: Create a strong password of chosen length and save it securely.
   - View Stored Passwords: See all previously generated passwords stored in the database.

2. When a password is generated, it is hashed using SHA256 for security before being stored in the SQLite database.

3. Stored passwords can be viewed in a DataFrame for easy tracking.

## Tech Stack

- Python
- Streamlit
- SQLite
- Pandas
- Werkzeug Security

## Project Structure

```
├── password_gen_streamlit.py # Main Streamlit application
├── mydatabase.db # SQLite database for stored passwords
└── README.md # Project description
```
