import tkinter as tk
from tkinter import filedialog, scrolledtext

def compare_files(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    differences = []
    max_lines = max(len(lines1), len(lines2))

    for i in range(max_lines):
        line1 = lines1[i] if i < len(lines1) else ""
        line2 = lines2[i] if i < len(lines2) else ""

        if line1 != line2:
            line_diffs = []
            max_len = max(len(line1), len(line2))

            for j in range(max_len):
                char1 = line1[j] if j < len(line1) else ""
                char2 = line2[j] if j < len(line2) else ""
                if char1 != char2:
                    line_diffs.append(j + 1)

            differences.append((i + 1, line_diffs, line1, line2))

    return differences

def highlight_differences(text_widget, differences):
    for diff in differences:
        line_num, col_nums, line1, line2 = diff
        for col_num in col_nums:
            start_idx = f"{line_num}.{col_num-1}"
            end_idx = f"{line_num}.{col_num}"
            text_widget.tag_add("highlight", start_idx, end_idx)
    text_widget.tag_config("highlight", background="yellow", foreground="black")

def open_file1():
    filepath = filedialog.askopenfilename()
    if filepath:
        file1_entry.delete(0, tk.END)
        file1_entry.insert(0, filepath)

def open_file2():
    filepath = filedialog.askopenfilename()
    if filepath:
        file2_entry.delete(0, tk.END)
        file2_entry.insert(0, filepath)

def compare_and_display():
    file1 = file1_entry.get()
    file2 = file2_entry.get()

    if not file1 or not file2:
        result_text.insert(tk.END, "Please select both files.\n")
        return

    result_text.delete(1.0, tk.END)

    differences = compare_files(file1, file2)

    if differences:
        result_text.insert(tk.END, f"Total differences: {len(differences)}\n")
        for diff in differences:
            line_num, col_nums, line1, line2 = diff
            col_str = ', '.join(map(str, col_nums))
            result_text.insert(tk.END, f"Line {line_num}, Columns: {col_str}\n - File1: {line1}\n - File2: {line2}\n")
        highlight_differences(result_text, differences)
    else:
        result_text.insert(tk.END, "The files are identical.\n")

# 创建主窗口
root = tk.Tk()
root.title("File Comparator")

# 文件1选择
file1_label = tk.Label(root, text="File 1:")
file1_label.grid(row=0, column=0, padx=10, pady=5)
file1_entry = tk.Entry(root, width=50)
file1_entry.grid(row=0, column=1, padx=10, pady=5)
file1_button = tk.Button(root, text="Browse", command=open_file1)
file1_button.grid(row=0, column=2, padx=10, pady=5)

# 文件2选择
file2_label = tk.Label(root, text="File 2:")
file2_label.grid(row=1, column=0, padx=10, pady=5)
file2_entry = tk.Entry(root, width=50)
file2_entry.grid(row=1, column=1, padx=10, pady=5)
file2_button = tk.Button(root, text="Browse", command=open_file2)
file2_button.grid(row=1, column=2, padx=10, pady=5)

# 比较按钮
compare_button = tk.Button(root, text="Compare", command=compare_and_display)
compare_button.grid(row=2, column=0, columnspan=3, pady=10)

# 结果显示区域
result_text = scrolledtext.ScrolledText(root, width=80, height=20)
result_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# 启动主循环
root.mainloop()
