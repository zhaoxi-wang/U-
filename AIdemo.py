#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#导入库
#from __future__ import unicode_literals
from model.model import ChatBot
import torch,warnings
warnings.filterwarnings("ignore")


#主程序，打印log，同时对话
def seq2chat(inputSeq):
    print('Loading the model...')
    chatBot = ChatBot('modelA.pkl', device=torch.device('cuda'))
    print('Finished...')

    allRandomChoose,showInfo = False, False
    #在控制端显示的词语

    #inputSeq = input("主人: ")#输入应该搞到表单里

    if inputSeq=='_crazy_on_':
        allRandomChoose = True
        print('小可爱: ','成功开启疯狂模式...')
    elif inputSeq=='_crazy_off_':
        allRandomChoose = False
        print('小可爱: ','成功关闭疯狂模式...')
    elif inputSeq=='_showInfo_on_':
        showInfo = True
        print('小可爱: ','成功开启日志打印...')
    elif inputSeq=='_showInfo_off_':
        showInfo = False
        print('小可爱: ','成功关闭日志打印...')
    else:
        outputSeq = chatBot.predictByBeamSearch(inputSeq, isRandomChoose=True, allRandomChoose=allRandomChoose, showInfo=showInfo)
        #print('小可爱: ',outputSeq)
        return outputSeq
    # if (inputSeq == '拜拜'):
    #     break
    print()
seq2chat('你好')