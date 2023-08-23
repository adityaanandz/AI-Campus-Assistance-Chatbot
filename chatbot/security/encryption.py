from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(data.encode())
    return encrypted_text

def decrypt_data(encrypted_data, key):
    cipher_suite = Fernet(key)
    decrypted_text = cipher_suite.decrypt(encrypted_data)
    return decrypted_text.decode()
