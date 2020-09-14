#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from socket import *
import tkinter as tk
import tkinter.scrolledtext as tst
import time
import tkinter.messagebox
import threading
from AIdemo import seq2chat
class Application(tk.Frame):
	def __init__(self,master):
		tk.Frame.__init__(self,master)
		self.grid()
		self.createWidgets()
	def createWidgets(self):
		#显示聊天窗口
		self.textEdit=tst.ScrolledText(self,width=50,height=15)
		self.textEdit.grid(row=0,column=0,rowspan=1,columnspan=4)
		#定义标签，改变字体颜色
		self.textEdit.tag_config('AI',foreground='red')
		self.textEdit.tag_config('大威天龙',foreground='blue')

		#编辑窗口
		self.inputText=tk.Text(self,width=40,height=5)
		self.inputText.grid(row=1,column=0,columnspan=1)
		#定义快捷键，按下回车即可发送消息
		self.inputText.bind("<KeyPress-Return>",self.textSendReturn)
		#发送按钮
		self.btnSend=tk.Button(self,text='发送消息',command=self.textSend)
		self.btnSend.grid(row=1,column=3)


	def textSend(self):
		#获取Text的所有内容
		str=self.inputText.get('1.0','end-1c')
		if str!="" :
			#显示发送时间和发送消息
			timemsg='\n'+'大威天龙'+'  '+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())+'\n'
			self.textEdit.config(state='normal')
			self.textEdit.insert(tk.END,timemsg,'AI')
			self.textEdit.insert(tk.END,str+'\n')
			#将滚动条拉到最后显示最新消息
			self.textEdit.see(tk.END)
			self.textEdit.config(state='disabled')
			self.inputText.delete(0.0,tk.END)	#删除输入框的内容
			#发送数据到服务端
			#发送输入的数据
			sendmsg=seq2chat(str)
		else:
			tk.messagebox.showinfo('警告',"不能发送空白信息！")

		revTime='AI'+'  '+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())+'\n'
		#通过设置state属性设置textEdit可编辑
		self.textEdit.config(state='normal')
		self.textEdit.insert(tk.END,revTime,'大威天龙')
		self.textEdit.insert(tk.END,sendmsg)
		#将滚动条拉到最后显示最新消息
		self.textEdit.see(tk.END)
		# #通过设置state属性设置textEdit不可编辑
		# self.textEdit.config(state='disabled')

	def textSendReturn(self,event):
		if event.keysym=="Return":
			self.textSend()

root=tk.Tk()
root.title('快来跟我聊聊天吧')


app=Application(master=root)
app.mainloop()
