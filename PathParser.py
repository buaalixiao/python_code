import codecs
def fileParser(filename):
    'Replace CSS,JS,IMG path in html files.'
    import re 
    f = open(filename,'r',encoding ='utf-8')
    lines = f.readlines()
    f.close()
    for index, line in enumerate(lines):
        #替换JS文件路径
        pattern = '<script src="js/'
        repl = '<script src="/static/js/'
        line = re.sub(pattern,repl,line)
        #替换CSS文件路径
        pattern = 'rel="stylesheet" href="'
        repl = 'rel="stylesheet" href="/static/'
        line = re.sub(pattern,repl,line)
        #替换图片文件路径
        pattern = '<img src="'
        repl = '<img src="/static/'
        line = re.sub(pattern,repl,line)
        #替换图标文件路径
        pattern = 'rel="shortcut icon" href="'
        repl = 'rel="shortcut icon" href="/static/'
        line = re.sub(pattern,repl,line)
        # #测试
        # pattern = 'script'
        # repl = 'script123'
        # line = re.sub(pattern,repl,line)
        # #增加单独文件目录
        # pattern = '/static/'
        # repl = '/static/filename'
        # line = re.sub(pattern,repl,line)
        lines[index] = line
    f = open(filename,'w',encoding ='utf-8')
    f.writelines(lines)
    f.close()
    return


import os
def dirParser(dirname):
    for root,dirs,files in os.walk(dirname):
        for file in files:
            fileParser(os.path.join(root,file))
            #print(os.path.join(root,file))
        for dir in dirs:
            dirParser(dir)

if __name__ == '__main__':
    path = r'G:\test_file\template'
    dirParser(path)