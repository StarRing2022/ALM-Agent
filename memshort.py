import hotnews
import llm

import os
from datetime import datetime

def write_to_file(text_content, folder_path):
    # 获取当前日期并格式化为YYYYMMDD格式
    today_date = datetime.now().strftime("%Y%m%d")
    
    # 构造文件名
    filename = f"{today_date}.txt"
    
    # 构造完整的文件路径
    file_path = os.path.join(folder_path, filename)
    
    # 检查文件夹是否存在，如果不存在则创建
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # 以追加模式打开文件，如果文件不存在，将会创建一个新文件
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(text_content)


def gen_short_memory():
    newstextlst,newstext = hotnews.get_news()
    genknown = llm.chatreasoning(newstext)

    # 调用函数
    folder_path = './data/'  # 替换为你的文件夹路径
    text_content = genknown.replace("\n","").strip()+"\n\n"  # 替换为你想要写入的内容
    write_to_file(text_content, folder_path)


# if __name__ == "__main__":
#     gen_short_memory()   