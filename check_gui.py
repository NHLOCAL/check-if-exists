import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def scan_if_exist(file_to_scan, files_list):
    if file_to_scan in files_list:
        return True
    else:
        return False

def main(dir_to_scan, target_dir, index=None):
    index_file = os.path.join(target_dir, "index-files.txt")
    if os.path.isfile(index_file) and index is None:
        with open(index_file, 'r', encoding='utf-8') as f:
            files_list = [str(line.strip()) for line in f]
    else:
        files_list = []
        for root, dirs, files in os.walk(target_dir):
            if files:
                files_list += files

        if index is not False:
            if os.path.isfile(index_file):
                os.system('attrib -s -h ' + index_file)
            with open(index_file, 'w', encoding='utf-8') as f:
                for item in files_list:
                    try:
                        f.write(str(item) + '\n')
                    except:
                        pass
            os.system('attrib +s +h ' + index_file)

    list_dir = os.listdir(dir_to_scan)
    result_text.delete(1.0, tk.END)  # Clear previous results
    for file_to_scan in list_dir:
        answer = scan_if_exist(file_to_scan, files_list)
        if answer:
            result_text.insert(tk.END, f'"{file_to_scan}" קובץ קיים!\n', "right")  # Insert right-aligned text

def browse_dir(label):
    dirname = filedialog.askdirectory()
    label.config(text=dirname)

def start_scan():
    dir_to_scan = dir_to_scan_label.cget("text")
    target_dir = target_dir_label.cget("text")
    index = index_var.get()
    main(dir_to_scan, target_dir, index)

# Create the GUI window
window = tk.Tk()
window.title("סורק תיקיות")
window.geometry("400x400")
window.configure(bg="white")

# Create the labels, radio buttons, and result text widget
dir_to_scan_label = tk.Label(window, text="תיקיית סריקה:", font=("Arial", 12), bg="white", justify=tk.RIGHT, width=20)
dir_to_scan_label.grid(row=0, column=1, pady=10)

dir_to_scan_button = tk.Button(window, text="בחירה", font=("Arial", 10), command=lambda: browse_dir(dir_to_scan_label))
dir_to_scan_button.grid(row=0, column=0)

target_dir_label = tk.Label(window, text="תיקיית יעד:", font=("Arial", 12), bg="white", justify=tk.RIGHT, width=20)
target_dir_label.grid(row=1, column=1, pady=10)

target_dir_button = tk.Button(window, text="בחירה", font=("Arial", 10), command=lambda: browse_dir(target_dir_label))
target_dir_button.grid(row=1, column=0)

index_label = tk.Label(window, text="אינדקס:", font=("Arial", 12), bg="white", justify=tk.RIGHT, width=20)
index_label.grid(row=2, column=1, pady=10)

index_var = tk.StringVar(value="ברירת מחדל")

index_frame = ttk.Frame(window)
index_frame.grid(row=2, column=0)

index_yes_button = ttk.Radiobutton(index_frame, text="כן", variable=index_var, value="כן", style="TRadiobutton",
                                  command=lambda: result_text.focus_set())
index_yes_button.pack(side=tk.RIGHT, padx=5)

index_no_button = ttk.Radiobutton(index_frame, text="לא", variable=index_var, value="לא", style="TRadiobutton",
                                 command=lambda: result_text.focus_set())
index_no_button.pack(side=tk.RIGHT, padx=5)

index_default_button = ttk.Radiobutton(index_frame, text="ברירת מחדל", variable=index_var, value="ברירת מחדל",
                                      style="TRadiobutton", command=lambda: result_text.focus_set())
index_default_button.pack(side=tk.RIGHT, padx=5)

start_button = tk.Button(window, text="התחל סריקה", font=("Arial", 12), command=start_scan)
start_button.grid(row=3, column=0, columnspan=2, pady=20)

result_label = tk.Label(window, text="תוצאות:", font=("Arial", 12), bg="white", justify=tk.RIGHT, width=20)
result_label.grid(row=4, column=1, pady=(20, 10), sticky=tk.W)

result_text = tk.Text(window, width=40, height=10, font=("Arial", 10), bg="light yellow")
result_text.tag_configure("right", justify=tk.RIGHT)
result_text.grid(row=5, column=0, columnspan=2, padx=10, pady=(0, 20), sticky=tk.NSEW)

scrollbar = tk.Scrollbar(result_text)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
result_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=result_text.yview)


# Configure grid weights to make the result text widget expandable
window.grid_rowconfigure(5, weight=1)
window.grid_columnconfigure(0, weight=1)

result_text.tag_add("right", "1.0", tk.END)


# Start the GUI event loop
window.mainloop()
