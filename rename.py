import os
import tkinter as tk
from tkinter import filedialog, messagebox

def rename_files(path, options):
    try:
        files = os.listdir(path)
        for file in files:
            old_name, ext = os.path.splitext(file)
            new_name = old_name
            if 'add_prefix' in options:
                new_name = options['add_prefix'] + new_name
            if 'add_suffix' in options:
                new_name += options['add_suffix']
            if 'delete_characters' in options:
                new_name = ''.join(filter(lambda x: x not in options['delete_characters'], new_name))
            if 'delete_numbers' in options:
                new_name = ''.join(filter(lambda x: not x.isdigit(), new_name))
            if 'delete_all_characters' in options:
                new_name = ''.join(filter(lambda x: not x.isalpha() and not x.isdigit(), new_name))
            os.rename(os.path.join(path, file), os.path.join(path, new_name + ext))
        messagebox.showinfo("Success", "Files renamed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def select_folder():
    folder_path = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, folder_path)

def start_rename():
    folder_path = path_entry.get()
    options = {}
    if prefix_var.get():
        options['add_prefix'] = prefix_entry.get()
    if suffix_var.get():
        options['add_suffix'] = suffix_entry.get()
    if del_chars_var.get():
        options['delete_characters'] = del_chars_entry.get()
    if del_nums_var.get():
        options['delete_numbers'] = True
    if del_all_chars_var.get():
        options['delete_all_characters'] = True

    if not os.path.isdir(folder_path):
        messagebox.showerror("Error", "Please select a valid folder path.")
        return

    if not any(options.values()):
        messagebox.showerror("Error", "Please select at least one option.")
        return

    rename_files(folder_path, options)

# Create main window
window = tk.Tk()
window.title("File Renamer")
window.geometry("400x300")

# Add background color
window.configure(bg='#FF5733')

# Frame for folder selection
folder_frame = tk.Frame(window, bg='#85C1E9')
folder_frame.pack(pady=10)

# Folder path entry
path_entry = tk.Entry(folder_frame, width=40)
path_entry.grid(row=0, column=0, padx=5, pady=5)

# Select folder button
select_button = tk.Button(folder_frame, text="Select Folder", command=select_folder)
select_button.grid(row=0, column=1, padx=5, pady=5)

# Options Frame
options_frame = tk.Frame(window, bg='#85C1E9')
options_frame.pack(pady=10)

# Add Prefix
prefix_var = tk.BooleanVar()
prefix_checkbox = tk.Checkbutton(options_frame, text="Add Prefix", variable=prefix_var, bg='#85C1E9')
prefix_checkbox.grid(row=0, column=0, padx=5, pady=5)
prefix_entry = tk.Entry(options_frame, width=20)
prefix_entry.grid(row=0, column=1, padx=5, pady=5)

# Add Suffix
suffix_var = tk.BooleanVar()
suffix_checkbox = tk.Checkbutton(options_frame, text="Add Suffix", variable=suffix_var, bg='#85C1E9')
suffix_checkbox.grid(row=1, column=0, padx=5, pady=5)
suffix_entry = tk.Entry(options_frame, width=20)
suffix_entry.grid(row=1, column=1, padx=5, pady=5)

# Delete Characters
del_chars_var = tk.BooleanVar()
del_chars_checkbox = tk.Checkbutton(options_frame, text="Delete Characters", variable=del_chars_var, bg='#85C1E9')
del_chars_checkbox.grid(row=2, column=0, padx=5, pady=5)
del_chars_entry = tk.Entry(options_frame, width=20)
del_chars_entry.grid(row=2, column=1, padx=5, pady=5)

# Delete Numbers
del_nums_var = tk.BooleanVar()
del_nums_checkbox = tk.Checkbutton(options_frame, text="Delete Numbers", variable=del_nums_var, bg='#85C1E9')
del_nums_checkbox.grid(row=3, column=0, padx=5, pady=5)

# Delete All Characters
del_all_chars_var = tk.BooleanVar()
del_all_chars_checkbox = tk.Checkbutton(options_frame, text="Delete All Characters", variable=del_all_chars_var, bg='#85C1E9')
del_all_chars_checkbox.grid(row=4, column=0, padx=5, pady=5)

# Start button
start_button = tk.Button(window, text="Start", command=start_rename, bg='#58D68D', relief=tk.RAISED, borderwidth=3)
start_button.pack(pady=10)

window.mainloop()
