class Writefile():
    def __init__(self,file_name,model):
        print("执行文件")
        self.file = None
        self.file_name = file_name
        self.model = model

    def __enter__(self):
        self.file = open(self.file_name,self.model)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("关闭文件")
        self.file.close()

with Writefile('test.txt','w') as f:
    f.write("番茄炒鸡蛋")

with Writefile('test.txt','r') as f:
    print(f.readlines())