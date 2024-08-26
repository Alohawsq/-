import sys

"""
python3 base_learn/02-比对两个文件不同.py test/test1.txt test/test2.txt
"""

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

            differences.append((i + 1, line_diffs, line1.strip(), line2.strip()))

    return differences
    

if __name__ == "__main__":
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    
    differences = compare_files(file1, file2)

    print(f"Total differences: {len(differences)}")
    for diff in differences:
        line_num, col_nums, line1, line2 = diff
        col_str = ', '.join(map(str, col_nums))
        print(f"Line {line_num}, Columns: {col_str}\n - File1: {line1}\n - File2: {line2}\n")