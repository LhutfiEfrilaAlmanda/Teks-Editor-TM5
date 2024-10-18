import tkinter as tk
from tkinter import filedialog

class EncryptedNotepad:
    def __init__(self, master):
        self.master = master
        self.master.title("Notepad Enkripsi")
        self.master.geometry("600x400")

        self.text_area = tk.Text(self.master, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill='both')

        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Simpan", command=self.save_file)
        file_menu.add_command(label="Buka", command=self.open_file)
        file_menu.add_command(label="Bersihkan", command=self.clear_text)
        file_menu.add_separator()
        file_menu.add_command(label="Keluar", command=self.master.quit)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            content = self.text_area.get(1.0, tk.END)
            encrypted_content = self.encrypt(content)
            with open(file_path, "w") as file:
                file.write(encrypted_content)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                encrypted_content = file.read()
            decrypted_content = self.decrypt(encrypted_content)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, decrypted_content)

    def clear_text(self):
        self.text_area.delete(1.0, tk.END)

    def encrypt(self, text):
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                encrypted_char = chr((ord(char) - ascii_offset + 3) % 26 + ascii_offset)
                result += encrypted_char
            elif char.isdigit():
                result += str((int(char) + 3) % 10)
            else:
                result += char
        return result

    def decrypt(self, encrypted_text):
        try:
            result = ""
            for char in encrypted_text:
                if char.isalpha():
                    ascii_offset = 65 if char.isupper() else 97
                    decrypted_char = chr((ord(char) - ascii_offset - 3) % 26 + ascii_offset)
                    result += decrypted_char
                elif char.isdigit():
                    result += str((int(char) - 3) % 10)
                else:
                    result += char
            return result
        except:
            return "Gagal mendekripsi file. Pastikan file yang dibuka adalah file yang dienkripsi oleh aplikasi ini."

if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptedNotepad(root)
    root.mainloop()