# 🔐 Project 02: Password Strength Meter
# 📌 Objective
# Build a Password Strength Meter in Python that evaluates a user's password based on security rule. The program will:

# Analyze passwords based on length, character types, and patterns.
# Assign a strength score (Weak, Moderate, Strong).
# Provide feedback to improve weak passwords.
# Use control flow, type casting, strings, and functions.
# 🔹 Requirements
# 1. Password Strength Criteria
# A strong password should:
# ✅ Be at least 8 characters long
# ✅ Contain uppercase & lowercase letters
# ✅ Include at least one digit (0-9)
# ✅ Have one special character (!@#$%^&*)

# 2. Scoring System
# Weak (Score: 1-2) → Short, missing key elements
# Moderate (Score: 3-4) → Good but missing some security features
# Strong (Score: 5) → Meets all criteria
# 3. Feedback System
# If the password is weak, suggest improvements.
# If the password is strong, display a success message.

import re
import streamlit as st

# Page style
st.set_page_config(page_title=" 🔐 Password Strength Meter made by Ab_Ahad" ,page_icon="🌘",layout="centered")

# custom Css
st.markdown("""
    <style>
        .main {text-align:center;}
        .stTextInput { width 60% !important;margin:auto;}
        .stButton button { width 30%;background-color #4CAF50; color: white; font-size: 18px;}
        .stButton button:hover {background-color: #45a049;}
</style>
""",unsafe_allow_html=True)

#page tile and discription
st.title("🔐 Password Strength Meter")
st.write("Enter your password below to check its security level.🔍")

#function to check password strenght
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9) **.")

        # Special characters
    if re.search(r"[ !@#$%^&*()_+{}\[\]:;\"'<,>.?/\\|`~]", password):
        score += 1 
    else:
        feedback.append("❌ Include **at least one special character ( !@#$%^&*()_+{}\[\]:;\"'<,>.?/\\|`~)**.")

        # Display Password Strength Result
    if score == 4:
        st.success("✅ Your password is **Strong**.")
    elif score >= 3 :
        st.info("⚠️ ** Moderate Password** - Consider improving security by adding more feature.")
    else:
        st.error("❌ **Weak Password** - Please follow the below suggestions to make it strong.")

        # Display feedback
        if feedback:
            with st.expander(" 🔍 **Improvement Suggestions** "):
                for item in feedback:
                    st.write(item)
password = st.text_input("Enter your password", type="password", help="Ensure your password is strong.🔐")

# Button to check password strength
if st.button("Check Strength"):
    if password:
        check_password_strength(password)

    else:
        st.warning("⚠️ Please enter your password to check its strength.")
