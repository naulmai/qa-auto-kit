import sys
import csv
import re
import os

def markdown_to_csv(md_path, csv_path):
    if not os.path.exists(md_path):
        print(f"Error: File '{md_path}' does not exist.")
        return

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    
    # Phân nhóm các dòng thành các bảng riêng biệt (nhóm các dòng liên tiếp bắt đầu bằng |)
    tables = []
    current_table = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('|'):
            current_table.append(stripped)
        else:
            if current_table:
                tables.append(current_table)
                current_table = []
    if current_table:
        tables.append(current_table)

    if not tables:
        print(f"Error: No Markdown table found in '{md_path}'.")
        return

    # Lựa chọn bảng có số lượng cột lớn nhất (thường là bảng test cases với 12 cột, bỏ qua bảng metadata chỉ có 2 cột)
    target_table = None
    max_cols = 0
    for t in tables:
        # Tách cột dòng header đầu tiên để đếm số cột
        first_line = t[0].strip('|')
        cols_count = len([col.strip() for col in first_line.split('|')])
        if cols_count > max_cols:
            max_cols = cols_count
            target_table = t

    # Lọc bỏ dòng gạch ngang (VD: |---|---|)
    table_lines = [line for line in target_table if not re.match(r'^\|[\s\-\|:]+\|$', line)]

    rows = []
    for line in table_lines:
        # Bỏ dấu | ở đầu và cuối dòng
        line = line.strip('|')
        
        # Split các cột bằng dấu |
        columns = [col.strip() for col in line.split('|')]
        
        # Xử lý thẻ <br> thành newline thực tế cho file CSV/Excel
        columns = [col.replace('<br>', '\n').replace('<br/>', '\n') for col in columns]
        
        rows.append(columns)

    # Ghi ra file CSV, sử dụng utf-8-sig để Excel nhận diện đúng tiếng Việt (BOM)
    with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
        
    print(f"Successfully converted markdown table to CSV!")
    print(f"Exported {len(rows)-1} records to: {csv_path}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python md_to_csv.py <input.md> <output.csv>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    markdown_to_csv(input_file, output_file)
