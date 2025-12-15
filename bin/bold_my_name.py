#!/usr/bin/env python3
import sys
import re
import os

# 定义要加粗的名字列表
MY_NAMES = [
    "Fu, X.", "Xiaokang Fu", "Fu, Xiaokang", "付小康",
    "Fu†, X.", "Fu†, Xiaokang"
]

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        for name in MY_NAMES:
            # 使用 re.escape 转义特殊字符，并构建正则
            # 使用 g 标志是 JS 的，Python 中直接用 sub 替换所有匹配
            regex = re.compile(re.escape(name))
            content = regex.sub(f"<strong>{name}</strong>", content)
            
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Bolded names in: {filepath}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 bold_my_name.py <file1> <file2> ...")
        sys.exit(1)
        
    for file_path in sys.argv[1:]:
        process_file(file_path)
