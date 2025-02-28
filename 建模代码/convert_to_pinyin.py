from pypinyin import pinyin, lazy_pinyin

def convert_to_pinyin(chinese_text):
    return ''.join(lazy_pinyin(chinese_text)).upper()

if __name__ == "__main__":
    import sys
    text = sys.argv[1]
    print(convert_to_pinyin(text))