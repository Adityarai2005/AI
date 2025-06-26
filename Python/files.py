def read_text(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        return f.read()
def write_txt(file_path,text):
    with open(file_path,'a') as f:
        f.write(text)
result=""
print(result)
write_txt(r"C:\Users\ar252\.vscode\Python\sample.txt","I am Hardworking person who only do hardwork when it is too late")
result+=read_text(r"file path hidden for security purposes")
print(result)
# similary specific modules are made to read pdf ,doc files
