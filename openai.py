import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator

# Function to translate text
def translate_text():
    src_text = source_text.get("1.0", "end-1c")
    target_lang = language_combo.get()

    if not src_text.strip():
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return

    if not target_lang:
        messagebox.showwarning("Language Error", "Please select a target language.")
        return

    try:
        # Initialize the Translator
        translator = Translator()

        # Perform the translation
        translated = translator.translate(src_text, dest=target_lang.lower())

        # Display the translated text
        target_text.delete("1.0", tk.END)
        target_text.insert(tk.END, translated.text)

    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Create the GUI window
root = tk.Tk()
root.title("Simple Language Converter")

# Source text label and input
source_label = tk.Label(root, text="Enter text to translate:")
source_label.pack()

source_text = tk.Text(root, height=10, width=50)
source_text.pack()

# Language selection dropdown
language_label = tk.Label(root, text="Select target language:")
language_label.pack()

language_options = [
    ('French', 'fr'),
    ('Spanish', 'es'),
    ('German', 'de'),
    ('Italian', 'it'),
    ('Hindi', 'hi'),
    ('Chinese (Simplified)', 'zh-cn')
]

language_combo = ttk.Combobox(root, values=[lang[0] for lang in language_options], state="readonly")
language_combo.pack()

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack()

# Target text label and output
target_label = tk.Label(root, text="Translated text:")
target_label.pack()

target_text = tk.Text(root, height=10, width=50)
target_text.pack()

# Run the application
root.mainloop()
