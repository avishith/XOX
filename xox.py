from tkinter import *
import random
import tkinter.messagebox as msg
global touch
global btns_
global n
n=8

def reset():
	global n
	global btns_
	btns_=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
	
	for i in btns_:
							i["text"]=''
							touch=1
							n=8
	

def check():
				global touch
				global n
			
				global btns_
				if (b1['text']=='O' and b2['text']=='O' and b3['text']=='O' or b4['text']=='O' and b5['text']=='O' and b6['text']=='O' or b7['text']=='O' and b8['text']=='O' and b9['text']=='O' or b1['text']=='O' and b4['text']=='O' and b7['text']=='O' or b2['text']=='O' and b5['text']=='O' and b8['text']=='O' or b3['text']=='O' and b6['text']=='O' and b9['text']=='O' or b1['text']=='O' and b5['text']=='O' and b9['text']=='O' or b3['text']=='O' and b5['text']=='O' and b7['text']=='O'):
					qus=msg.askquestion( 'XOX','O win Game...! Do U wants to play AGAIN')
				
					if qus=='yes':
							
							btns_=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
							for i in btns_:
								i["text"]=''
							touch=1
							n=8
							
					else:
						root.destroy()
				elif (b1['text']=='X' and b2['text']=='X' and b3['text']=='X' or b4['text']=='X' and b5['text']=='X' and b6['text']=='X' or b7['text']=='X' and b8['text']=='X' and b9['text']=='X' or b1['text']=='X' and b4['text']=='X' and b7['text']=='X' or b2['text']=='X' and b5['text']=='X' and b8['text']=='X' or b3['text']=='X' and b6['text']=='X' and b9['text']=='X' or b1['text']=='X' and b5['text']=='X' and b9['text']=='X' or b3['text']=='X' and b5['text']=='X' and b7['text']=='X'):
					qus=msg.askquestion( 'XOX','X win Game...! Do U wants to play AGAIN')
					win=1
					if qus=='yes':
							
							btns_=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
							for i in btns_:
								i["text"]=''
							touch=1
							n=8
					
					else:
						root.destroy()

def computer(value):
	global touch
	global n
	global btns_
	try:
		if touch==0:
			
			
			play=btns_[random.randint(0,n)]
			
			play['text']='O'
			check()
			btns_.remove(play)
			n=n-1
			touch=1
	
	except ValueError:
			qus=msg.askquestion( 'XOX','Tie 1Game')	
			if qus=='yes':
							
							btns_=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
							for i in btns_:
								i["text"]=''
							touch=1
	
							n=8
			else:
				root.destroy()
def play(button):
		global btns_
		global touch
		global n
		try:
			if button['text']=='' and touch ==1:
		
				button['text'] = 'X'
				n=n-1
				btns_.remove(button)
				check()
				dely=[100,200,550,680]
				dely=dely[random.randint(0,3)]
				root.after(dely,computer,"O")
				touch=0
				
		except ValueError:
			qus=msg.askquestion( 'XOX','Tie 2Game')	
			if qus=='yes':
							
							btns_=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
							for i in btns_:
								i["text"]=''
							touch=1
				
							n=8	
				
			

root=Tk()
ABC1=Frame(root,bg='#1f5629',bd=20,relief=RIDGE)
ABC1.grid()
touch=1
b1=Button(ABC1,height=6,fg='red',width=8,bg='black',text="",bd=4,font=("arial",7,"bold"),command=lambda:play(b1))
b1.grid(row=0,column=0)
	
b2=Button(ABC1,height=6,fg='red',text='',width=8,bg='black',bd=4,font=("arial",7,"bold"),command=lambda:play(b2))
b2.grid(row=0,column=1)
	
b3=Button(ABC1,height=6,bg='black',fg='red',text='',width=8,bd=4,font=("arial",7,"bold"),command=lambda:play(b3))
b3.grid(row=0,column=2)
	
b4=Button(ABC1,height=6,width=8,bg='black',bd=4,fg='red',font=("arial",7,"bold"),command=lambda:play(b4))
b4.grid(row=1,column=0)
	
b5=Button(ABC1,height=6,width=8,bg='black',bd=4,fg='red',font=("arial",7,"bold"),command=lambda:play(b5))
b5.grid(row=1,column=1)
	
b6=Button(ABC1,height=6,width=8,bg='black',bd=4,fg='red',font=("arial",7,"bold"),command=lambda:play(b6))
b6.grid(row=1,column=2)
	
b7=Button(ABC1,height=6,width=8,bg='black',bd=4,fg='red',font=("arial",7,"bold"),command=lambda:play(b7))
b7.grid(row=2,column=0)
	
b8=Button(ABC1,height=6,width=8,bg='black',bd=4,fg='red',font=("arial",7,"bold"),command=lambda:play(b8))
b8.grid(row=2,column=1)
	
b9=Button(ABC1,height=6,bg='black',width=8,bd=4,fg='red',font=("arial",7,),command=lambda:play(b9))
b9.grid(row=2,column=2)
b10=Button(ABC1,text='RESET',height=1,bg='black',width=2,bd=4,fg='red',font=("arial",7,),command=reset)
b10.grid(row=3,column=0)

b11=Button(ABC1,text='RESET',height=1,bg='black',width=2,bd=4,fg='red',font=("arial",7,),command=reset)
b11.grid(row=3,column=2)
btns_=[b1,b2,b3,b4,b5,b6,b7,b8,b9]	

	
root.mainloop()



