from langchain.text_splitter import CharacterTextSplitter

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

import os
from datetime import datetime

import llm

embeddings = HuggingFaceEmbeddings(model_name='Conan-embedding-v1')

def merge_txt_files_and_write(folder_path, output_folder_path):
    # 获取当前日期并格式化为YYYYMMDD格式
    today_date = datetime.now().strftime("%Y%m%d")
    
    # 构造输出文件名
    output_filename = f"{today_date}.txt"
    output_file_path = os.path.join(output_folder_path, output_filename)
    
    # 初始化一个空字符串用于存储所有文本内容
    merged_content = ""
    
    # 遍历文件夹内的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):  # 确保处理的是TXT文件
            file_path = os.path.join(folder_path, filename)
            
            # 打开并读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                merged_content += content + "\n"  # 将当前文件内容添加到合并内容字符串，并添加换行符以分隔不同文件的内容

    # 将合并后的内容写入新的TXT文件
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(merged_content)
    
    return output_file_path

def sortknowledge():
    folder_path = './data/'  # 替换为你的文件夹路径
    output_folder_path = './memory/'  # 替换为输出文件的文件夹路径
    output_file_path = merge_txt_files_and_write(folder_path, output_folder_path)
    #print(output_file_path)
    return output_file_path

def sortknowledge_learn(output_file_path):
    # 使用open函数打开文件
    with open(output_file_path, 'r', encoding='utf-8') as file:
        # 使用read方法读取文件内容
        content = file.read()
    #print(content)
    learntext = llm.chatlearn(content)
    #print(learntext)

    ltmtext = content+"\n"+learntext
    # 将合并后的内容写入新的TXT文件
    with open(output_file_path.split('.txt')[0]+"_learned.txt", 'w', encoding='utf-8') as output_file:
        output_file.write(ltmtext)

    ltmfilepath = output_file_path.split('.txt')[0]+"_learned.txt"
    raw_documents = TextLoader(ltmfilepath,encoding='UTF-8').load()
    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    documents = text_splitter.split_documents(raw_documents)

    vectorstore  = FAISS.from_documents(
        documents,
        embeddings
    )
    if os.path.exists("./memory/ltmdb/"):
        try:
            os.removedirs("./memory/ltmdb")
        except:
            pass
    vectorstore.save_local('./memory/ltmdb')

def ltm_answer(question):
    answer = ""
    
    if os.path.exists("./memory/ltmdb/"):
        vectorstore = FAISS.load_local("./memory/ltmdb/", embeddings,allow_dangerous_deserialization=True)
        found_docs = vectorstore.search(question,"similarity")
        zsk = found_docs[0].page_content
        #print(zsk)
        print("zsk find")
        answer = llm.chatzsk(question,zsk)
    else:
        answer = llm.chat(question)
    
    return answer
    


if __name__ == "__main__":
    #output_file_path = sortknowledge()
    #sortknowledge_learn(output_file_path)

    answer = ltm_answer("什么是心动信号")
    print(answer)
    