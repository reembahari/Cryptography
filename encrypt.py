import streamlit as st
from cryptography.fernet import Fernet

# Set the page config
st.set_page_config(page_title="Encryption App", layout="wide")

# Function to generate a new key
def generate_key():
    return Fernet.generate_key()

# Function to encrypt a message
def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    return encrypted

# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_message).decode()
    return decrypted

# Add background color using HTML
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: black;
    }
    .title {
        color: white;
        font-size: 30px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.markdown('<h1 class="title">Text Encryption and Decryption App</h1>', unsafe_allow_html=True)

# Generate a new key
if st.button("Generate New Key"):
    key = generate_key()
    st.session_state.key = key.decode()  # Save the key in the session
    st.success("New key has been generated!")

# Display the current key
if 'key' in st.session_state:
    st.write("Current Key:", st.session_state.key)

# Input for the text to encrypt
user_input = st.text_area("Enter text to encrypt:")

# Button for encryption
if st.button("Encrypt Text"):
    if 'key' not in st.session_state:
        st.error("Please generate a key first!")
    else:
        encrypted_message = encrypt_message(user_input, st.session_state.key.encode())
        st.write("Encrypted Text:", encrypted_message.decode())

# Input for the encrypted text to decrypt
encrypted_input = st.text_area("Enter encrypted text to decrypt:")

# Button for decryption
if st.button("Decrypt Text"):
    if 'key' not in st.session_state:
        st.error("Please generate a key first!")
    else:
        try:
            decrypted_message = decrypt_message(encrypted_input.encode(), st.session_state.key.encode())
            st.write("Decrypted Text:", decrypted_message)
        except Exception as e:
            st.error("Decryption failed. Please ensure the input is correct.")