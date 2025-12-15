#!/usr/bin/env python3
import re
import os

SOURCE_BIB = 'Clean_Academic_CV/ref.bib'
TARGET_BIB = '_bibliography/publications.bib'

def clean_bibtex(content):
    # 源文件已经做过一次大的清理，这里主要处理特殊符号映射
    
    # 1. 移除 \textbf{...} -> ...
    content = re.sub(r'\\textbf\{([^}]+)\}', r'\1', content)
    
    # 2. 移除 \ul{...} -> ...
    content = re.sub(r'\\ul\{([^}]+)\}', r'\1', content)
    
    # 3. 移除 \textit{...} -> ...
    content = re.sub(r'\\textit\{([^}]+)\}', r'\1', content)

    # 4. 处理 dagger (各种变体)
    # $^\dagger$ -> †
    content = content.replace(r'$^{\dagger}$', '†')
    content = content.replace(r'^{\dagger}', '†')
    content = content.replace(r'^\dagger', '†')
    content = content.replace(r'{\dagger}', '†')
    content = content.replace(r'\dagger', '†')
    
    # 5. 移除所有 $
    content = content.replace('$', '')
    
    # 6. 清理可能残留的 ^
    content = content.replace('^', '')

    # 7. 移除 addendum 字段
    content = re.sub(r'addendum\s*=\s*\{[^}]+\},?', '', content, flags=re.IGNORECASE)

    # 8. 修复 Human mobility 条目中可能的语法问题 (这行之前被注释了，但现在恢复，因为它处理了 Fu†, Xiaokang and ...)
    content = content.replace('Fu†, Xiaokang and', 'Fu†, Xiaokang,')
    
    return content

def update_bib():
    if not os.path.exists(SOURCE_BIB):
        print(f"Error: {SOURCE_BIB} not found")
        return

    # 确保目标目录存在
    os.makedirs(os.path.dirname(TARGET_BIB), exist_ok=True)

    with open(SOURCE_BIB, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cleaned_content = clean_bibtex(content)
    
    with open(TARGET_BIB, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
        
    print(f"Successfully updated {TARGET_BIB}")

if __name__ == "__main__":
    update_bib()
