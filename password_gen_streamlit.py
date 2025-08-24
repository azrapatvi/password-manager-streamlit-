import streamlit as st
import random
import sqlite3
import pandas as pd
from werkzeug.security import generate_password_hash,check_password_hash
password=""

if "password" not in st.session_state:
    st.session_state.password = ""


st.sidebar.title("🔑 Navigation")
st.sidebar.subheader("🔧 Password Options")

page=st.sidebar.radio("Go to",["Home","Generate Password", "View Stored Passwords"])

if page=="Home":
    st.title("Random Password Generator")
    st.subheader("Generate strong, random, and secure passwords instantly.")
    col1,col2=st.columns(2)

    st.write(" ")
    with col1:
        st.write("""
            Weak passwords are easy to hack.  
            Use this tool to create strong, unique, and secure passwords 
            to protect your online accounts. 🚀
        """)

    with col2:
        st.markdown("""
            **🔒 Tips for Strong Passwords**
            - Use at least 12 characters  
            - Mix uppercase, lowercase, numbers, and symbols  
            - Avoid using personal info  
            - Use different passwords for different accounts  
        """)

elif page=="Generate Password":

    conn=sqlite3.connect("mydatabase.db")
    cursor=conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stored_pass(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP        
            )
    """)

    st.subheader("🔐 Generate a Strong and Secure Password")
    st.write("🔑 Your Security Starts Here")

    with st.container(border=True):
        password_length=st.slider("Select password length",4,32,6)
        
        submitted=st.button("Generate Password")
        if submitted:
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_"

            
            for i in range(1,password_length+1):
                password+=random.choice(chars)

            st.session_state.password=password
            st.write("✅ Your Secure Password is")
            st.code(st.session_state.password,language="")

            hashed_password=generate_password_hash(st.session_state.password)
            cursor.execute("INSERT INTO stored_pass (password)VALUES(?)",(hashed_password,))
            conn.commit()

elif page=="View Stored Passwords":
    st.subheader("📂 Stored Passwords")
    conn=sqlite3.connect("mydatabase.db")
    cursor=conn.cursor()

    cursor.execute("SELECT * FROM stored_pass ")
    rows = cursor.fetchall()

    df = pd.DataFrame(rows, columns=["ID", "Password", "Created At"])
    st.dataframe(df)

    