#IMPORTANT:::THIS CODE HAS BEEN MADE AND TESTED PERFECTLY WITH PYTHON VERSION 2.7 AND GIVING SOME UNPREDICTABLE ERRORS WITH PYTHON VERSIONS BELOW 2.7 WHICH ARE IN WORKSPACE COMPUTERS


from curses import initscr,curs_set,newwin,endwin,KEY_RIGHT,KEY_LEFT,KEY_DOWN,KEY_UP,start_color
from random import randrange
import curses

class introduction:
	initscr()
	curs_set(0)
	def __init__(self):
		self.win = newwin(50,130,0,0)
	
		self.win.keypad(1)
		self.win.nodelay(0)
		self.win.border(' ',' ',' ',' ',' ',' ',' ',' ')
	def an(self):
		f=open("robocop")
		x,y=2,2
		for line in f.readlines():
			self.win.addstr(y,x,line)
			y=y+1
		self.win.refresh()
		curses.napms(1000)
		self.win.clear()
		endwin()

#--------------------------------------------------------------------------------------------------------------------------------------

a9=introduction()
a9.an()			
#---------------------------------------------------------------------------------------------------------------------------------------
class field:
	def __init__(self,y,x,z):
		self.y=y
		self.x=x
		self.win = newwin(y,x,0,0)
		self.win.keypad(1)
		self.win.nodelay(1)
		self.win.border('|','|','~','~','+','+','+','+')
		self.snake=[[28,7],[29,7],[30,7],[31,7],[32,7],[28,8],[29,8],[30,8],[31,8],[32,8],[28,9],[29,9],[30,9],[31,9],[32,9],[28,10],[29,10],[30,10],[31,10],[32,10]]
		self.a=[' ','i',' ','i',' ','[','@',' ','@',']','|','_','_','_','|','d',' ',' ',' ','b']
		self.d=z
		#self.bmb=bmb
	

	def add(self):
		#d=3
		for f in range(self.d):
			c = [n for n in [[randrange(1,self.x-2,1),randrange(1,self.y-2,1)] for x in range(len(self.snake))] if n not in self.snake]
        		self.win.addch(c == [] and 4 or c[f][1],c == [] and 44 or c[f][0],'D')
		c = [n for n in [[randrange(1,self.x-2,1),randrange(1,self.y-2,1)] for x in range(len(self.snake))] if n not in self.snake]
		#for f in range(self.bmb):
		self.win.addch(c == [] and 4 or c[self.d][1],c == [] and 44 or c[self.d][0],'B')

  	def addrob(self):
		for x in range(len(self.snake)):
			self.win.addch(self.snake[x][1],self.snake[x][0],self.a[x])
#----------------------------------------------------------------------------------------------------------------------------------------
class hello():
	initscr()
	curs_set(0)
	def __init__(self):
		self.win=newwin(20,80,0,0)
		self.win.keypad(1)
		self.win.nodelay(0)
		self.win.border()
		self.k=27
		self.win.addstr(2,2,"PRESS ENTER",curses.A_BOLD)
	def screeny(self,y1,y2,y3,x1,x2):
		#self.win.addstr(9,35,"           ")
		for y in range(y1,y2,y3):
			self.k=self.win.getch()
			self.win.timeout(50)
			if self.k==27:break
			self.k=-1
			if self.k==-1:
				self.win.addch(y,x1,'X')
				self.win.addch(y,x2,'X')

	def screenx(self,x1,x2,x3,y1,y2):
		

		for x in range(x1,x2,x3):
			self.k=self.win.getch()
			self.win.timeout(50)
			if self.k==27:break
			self.k=-1
			if self.k==-1:
				self.win.addch(y1,x,'X')
				self.win.addch(y2,x,'X')
				

	def show(self):
		while True:
			
			key=self.win.getch()
			self.win.timeout(1000)
			key=-1
			if key==-1:break

	
		self.win.refresh()
		curses.napms(2000)


#--------------------------------------------------------------------------------------------------------------------------------------
class name():	
	initscr()
	curs_set(0)

	def __init__(self):
		self.win = newwin(20,80,0,0)
	
		self.win.keypad(1)
		self.win.nodelay(0)
		self.win.border()
		self.win.addstr(8,15,"ENTER YOUR NAME ::::",curses.A_BOLD)
		self.nm=self.win.getstr(10,15,15)
			
	def end(self):
		endwin()
	def show(self):
		
		self.win.addstr(9,35,"PRESS ENTER")
		
		while True:
			
			key=self.win.getch()
			self.win.timeout(1800)
			key=-1
			if key==-1:break
#ob=name()		
a1=name()
a1.end()
player=a1.nm
#______________________________________________________________________________________________________________________________________
class rob(field):
	initscr()
	curs_set(0)
	curses.flash()

	def __init__(self,z,sc):
		field.__init__(self,20,80,z)
		self.key=KEY_RIGHT
		self.count=0
		self.level=0
		self.bar=6
		self.sc=sc
		self.gamescore=0
	def addtxt(self):
		self.win.addstr(self.y-1,2,"bomb active!!",curses.A_UNDERLINE)

	def move(self,tmout):
		while self.key!=27:
    			flag=0
			
    			self.win.addstr(0,2,' count: '+str(self.count)+' ',curses.A_BOLD)
			self.win.addstr(0,15,'PLAYER : ' + player +'   ')
			key3=self.key
    			self.win.timeout(tmout)
    			key2=self.key
    			getkey = self.win.getch()
    			self.key = self.key if getkey==-1 else getkey
			if self.key!=ord("p")  and self.key!=27 and self.key!=KEY_UP and self.key!=KEY_DOWN and self.key!=KEY_RIGHT and self.key!=KEY_LEFT:
				self.key=key3
     			if self.key==ord("p"):
    				l="PAUS"
    				self.win.addstr(self.snake[5][1],self.snake[5][0],l,curses.A_BOLD)
    				while True:
					ev=self.win.getch()
					if ev==ord("p"):
						for x in range(len(l)):
							self.win.addch(self.snake[5][1],self.snake[5][0]+x,' ')
						self.key=key2
						break
					if ev==27:
		  				flag=1
		  				break
    			s=self.snake
   

    			for x in  range(len(self.snake)):
	    			self.win.addch(self.snake[x][1],self.snake[x][0],' ')
        
    			if self.key==KEY_RIGHT:
    				for x in range(len(self.snake)):
					self.snake[x][0]=self.snake[x][0]+1
    			if self.key==KEY_LEFT:
				for x in range(len(self.snake)):
					self.snake[x][0]=self.snake[x][0]-1
    			if self.key==KEY_UP:
				for x in range(len(self.snake)):
					self.snake[x][1]=self.snake[x][1]-1
    			if self.key==KEY_DOWN:
				for x in range(len(self.snake)):
					self.snake[x][1]=self.snake[x][1]+1
			if self.count != self.d:
    				for x in range(len(self.snake)):
	    				if self.win.inch(self.snake[x][1],self.snake[x][0]) & 255 != ord(' ') and self.win.inch(self.snake[x][1],self.snake[x][0]) & 255 !=ord('D'):

						y1=self.y-2
						while y1>1:
							if y1%2==1:
								for x in range(1,self.x-1):
									k1=self.win.getch()

									self.win.timeout(3)
									if k1==27:
										flag=1
										break
									k1=-1
									if k1==-1:
										self.win.addch(y1,x,'x')
							if y1%2==0:
								for x in range(self.x-2,1,-1):
									k1=self.win.getch()
									self.win.timeout(3)
									k1=-1
									if k1==-1:
										self.win.addch(y1,x,'x')
							if flag==1:break
							y1=y1-1					
					
		    				win2=newwin(20,80,0,0)
		    				win2.nodelay(1)
		    				win2.keypad(1)
		    				win2.border('#','#','#','#','#','#','#','#')
		    				win2.addstr(9,35,"SORRY....YOU LOST....GAME OVER!!")
						for x in range(4):
							curses.flash()
							win2.refresh()
							curses.napms(500)

		    				while True:
			   
							e=win2.getch()
			    				win2.timeout(1800)
			    				e=win2.getch()
			    				e=-1
			    				if e==-1:break
		    				flag=1
		    				break
    				if flag==1:
					curses.beep()
					break
    
    			for x in range(len(self.snake)):
	   			if self.win.inch(self.snake[x][1],self.snake[x][0]) & 255 == ord('D'):
					self.count=self.count+1
					self.gamescore=self.gamescore+self.sc
			if self.count==self.d:
				self.win.addstr(self.y-1,2,"good!!you collected all codes.Now rush to bomb !!",curses.A_UNDERLINE)
				for x in range(len(self.snake)):
	    				if self.win.inch(self.snake[x][1],self.snake[x][0]) & 255 != ord(' ') and self.win.inch(self.snake[x][1],self.snake[x][0]) & 255 !=ord('B') and self.win.inch(self.snake[x][1],self.snake[x][0]) & 255 !=ord('D'):
						y1=self.y-2
						while y1>1:
							if y1%2==1:
								for x in range(1,self.x-1):
									k1=self.win.getch()

									self.win.timeout(3)
									if k1==27:
										flag=1
										break
									k1=-1
									if k1==-1:
										self.win.addch(y1,x,'x')
							if y1%2==0:
								for x in range(self.x-2,1,-1):
									k1=self.win.getch()
									self.win.timeout(3)
									k1=-1
									if k1==-1:
										self.win.addch(y1,x,'x')
							if flag==1:break
							y1=y1-1					
						win2=newwin(20,80,0,0)
		    				win2.nodelay(1)
		    				win2.keypad(1)
		    				win2.border('#','#','#','#','#','#','#','#')
		    				win2.addstr(9,35,"SORRY....YOU LOST....GAME OVER!!",curses.A_BOLD)
						for x in range(4):
							curses.flash()
							win2.refresh()
							curses.napms(500)
						win2.refresh()
						curses.napms(3000)
		    				flag=1
		    				break
    
					if self.win.inch(self.snake[x][1],self.snake[x][0]) & 255 == ord('B'):
						self.level=1
						a8=hello()
						a8.screeny(5,16,1,5,6)
						a8.screenx(7,12,1,5,6)
						a8.screenx(7,12,1,14,15)
						a8.screeny(15,10,-1,12,13)
						a8.screeny(15,10,-1,19,20)	
						a8.screenx(14,19,1,11,12)			
						a8.screeny(5,16,1,24,25)
						a8.screeny(5,16,1,29,30)
						a8.screenx(25,29,1,14,15)
						a8.screeny(5,16,1,34,35)
						a8.screeny(5,16,1,36,37)
						a8.screenx(37,42,1,5,6)
						a8.screenx(37,42,1,14,15)
						a8.screeny(5,16,1,42,42)
						a8.screenx(44,56,2,14,15)
						a8.show()							
						win3=newwin(20,80,0,0)
		    				win3.nodelay(1)
		    				win3.keypad(1)
		    				win3.border('|','|','~','~','+','+','+','+')
		    				win3.addstr(9,30,"CONGRACTS....YOU DIFFUSED THE BOMB....YOU WON!!",curses.A_BOLD)
						flag=1
						win3.refresh()
						curses.napms(3000)
	            				endwin()
						break
				if flag==1:
					curses.beep()
					break


    			for x in range(len(self.snake)):
	    			self.win.addch(self.snake[x][1],self.snake[x][0],self.a[x])
		endwin()


	def barrier(self):
		for f in range(self.bar):
			c = [n for n in [[randrange(1,self.x-2,1),randrange(1,self.y-2,1)] for x in range(len(self.snake))] if n not in self.snake]
        		self.win.addch(c == [] and 4 or c[f][1],c == [] and 44 or c[f][0],'X')



			


#----------------------------------------------------------------------------------------------------------------------------------------
class level2:
	initscr()
	curs_set(0)
	def __init__(self):
		self.win = newwin(20,80,0,0)
	
		self.win.keypad(1)
		self.win.nodelay(0)
		self.win.border()
		self.win.addstr(8,15,"LEVEL 2 BEGINS",curses.A_BOLD)
		self.win.refresh()
		curses.napms(100)
		self.win.addstr(10,15,"BEWARE OF X.............IT CAN KILL U",curses.A_BOLD)
		self.win.refresh()
		curses.napms(2000)
	

	def show1(self):

		
		while True:
			
			key=self.win.getch()
			self.win.timeout(1000)
			key=-1
			if key==-1:break
#-------------------------------------------------------------------------------------------------------------------------------------
a4=hello()
a4.screeny(5,16,1,5,6)
a4.screenx(7,11,1,10,11)
a4.screeny(5,16,1,11,12)
a4.screeny(5,16,1,16,17)
a4.screenx(17,22,1,14,15)
a4.screenx(17,22,1,10,11)
a4.screenx(17,22,1,5,6)
a4.screeny(5,16,1,25,26)
a4.screenx(27,33,1,14,15)
a4.screeny(5,16,1,34,35)
a4.screenx(36,42,1,14,15)
a4.screeny(5,16,1,45,46)
a4.screeny(5,16,1,52,53)
a4.screenx(47,54,1,5,6)
a4.screenx(47,54,1,14,15)
a4.screenx(58,68,2,14,15)
a4.show()

a2=rob(3,10)
a2.add()
a2.addrob()
a2.addtxt()
a2.move(180)
score1=a2.gamescore
if a2.level==1:
	a6=level2()
	#a6.show1()
	a3=rob(5,10)
	a3.add()
	a3.addrob()
	a3.addtxt()
	a3.barrier()
	a3.move(300)
	score2=a3.gamescore

if a2.level==1:
	final=score1+score2
else:
	final=score1
print '\n  \n  GAME DESIGNED BY SHUBHAM SANGAL \n' + player + ' your score: '+str(final)+'\n'
