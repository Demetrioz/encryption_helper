from tkinter import Tk, Label, Text, Button, messagebox
from cryptography.fernet import Fernet

class EncryptionHelper():
  def __init__(self) -> None:
    self.window = Tk()
    self.window.title("Encryption Helper")
    self.window.config(padx=16, pady=16)

    self.title_label = Label(text="Encryption Helper")
    self.title_label.grid(row=0, column=1)

    self.public_key_label = Label(text="Public Key", width=25)
    self.public_key_label.grid(row=1, column=0)
    self.public_key_text = Text(height=5, width=60)
    self.public_key_text.grid(row=1, column=1, columnspan=2, pady=8)

    self.private_key_label = Label(text="Private Key", width=25)
    self.private_key_label.grid(row=2, column=0)
    self.private_key_text = Text(height=5, width=60)
    self.private_key_text.grid(row=2, column=1, columnspan=2, pady=8)

    self.decrypted_text_label = Label(text="Decrypted Text", width=25)
    self.decrypted_text_label.grid(row=3, column=0)
    self.decrypted_text_text = Text(height=5, width=60)
    self.decrypted_text_text.grid(row=3, column=1, columnspan=2, pady=8)

    self.encrypted_text_label = Label(text="Encrypted Text", width=25)
    self.encrypted_text_label.grid(row=4, column=0)
    self.encrypted_text_text = Text(height=5, width=60)
    self.encrypted_text_text.grid(row=4, column=1, columnspan=2, pady=8)

    self.generate_key_button = Button(text="Generate Key", command=self.__generate_key)
    self.generate_key_button.grid(row=5, column=0)

    self.encrypt_button = Button(text="Encrypt", command=self.__try_encrypt)
    self.encrypt_button.grid(row=5, column=1)

    self.decrypt_button = Button(text="Decrypt", command=self.__try_decrypt)
    self.decrypt_button.grid(row=5, column=2)

  def __generate_key(self) -> None:
    key = Fernet.generate_key()
    self.private_key_text.delete(1.0, "end")
    self.private_key_text.insert(1.0, key)

  def __try_encrypt(self) -> None:
    try:
      key = self.private_key_text.get(1.0, "end-1c")
      plain_text = self.decrypted_text_text.get(1.0, "end-1c")
      encoded_text = plain_text.encode("utf-8")

      if key == None or key == "":
        raise Exception("Private Key missing")

      if plain_text == None or plain_text == "":
        raise Exception("No text to encrypt")

      encryptor = Fernet(key)
      encrypted_text = encryptor.encrypt(encoded_text)

      self.encrypted_text_text.delete(1.0, "end")
      self.encrypted_text_text.insert(1.0, encrypted_text)

    except Exception as ex:
      messagebox.showerror("Error", ex)

  def __try_decrypt(self) -> None:
    try:
      key = self.private_key_text.get(1.0, "end-1c")
      encrypted_text = self.encrypted_text_text.get(1.0, "end-1c")
      encoded_text = encrypted_text.encode("utf-8")

      if key == None or key == "":
        raise Exception("Private Key missing")

      if encrypted_text == None or encrypted_text == "":
        raise Exception("No text to decrypt")

      encryptor = Fernet(key)
      decrypted_text = encryptor.decrypt(encoded_text)

      self.decrypted_text_text.delete(1.0, "end")
      self.decrypted_text_text.insert(1.0, decrypted_text)
      
    except Exception as ex:
      messagebox.showerror("Error", ex)

  def run(self) -> None:
    self.window.mainloop()