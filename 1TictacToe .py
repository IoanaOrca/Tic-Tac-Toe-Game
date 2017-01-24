
# coding: utf-8

# In[2]:

from IPython.display import clear_output
def imprima(board):
    clear_output()
    print '\n'
    print board[0]+" | "+board[1]+" | "+board[2]
    print "---------"
    print board[3]+" | "+board[4]+" | "+board[5]
    print "---------"
    print board[6]+" | "+board[7]+" | "+board[8]
    print '\n'


# In[3]:

def locatiiplayer(l,mark):
    print('What position are you putting your : {} ?'.format(mark))
    position = input(':')
    #print l
    while l[position-1]=='x' or l[position-1]=='0':
        print('Thant positon is already taken, please give another position for your : {} ?'.format(mark))
        position = input(':')
        #print l
    return position


# In[4]:

def anywinner(board,mark):
    loc=[]
    boo=False
    for i in range(len(board)):
        if board[i]==mark:
            loc.append(i+1)
    #print loc
    win=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(7,5,3)]    
    for i in win :
        if set(i)<=set(loc):
            print 'THE WINNER IS ',mark
            boo=True
    return boo 
#miu=['_','0','0','_','_','0','_','0','0']
#anywinner(miu,'0')


# In[5]:

def istie(board):
    if (casute(board)==9):
        print 'THE GAME IS A TIE!'
        return True
    else:
        return False
#miu=['0','x','x','0','x','x','0','x','x']
#istie(miu)


# In[6]:

def gofirst():
    print 'Who wants to go first ?'
    mark=raw_input('x or 0 :').lower()
    while mark<>'x' and mark <> '0':
        print ('Please select x or 0')
        mark=raw_input()
    return mark
#sic=gofirst()
#print sic


# In[7]:

def casute(l):
    count=0
    for i in l:
        if i=='x'or i=='0':
            count+=1
    return count

#l=['_','x','_','_','0','_','x','_','_']
#casute(l)


# In[ ]:




# In[8]:

def playgame(l):
    setu=gofirst()
    
    imprima(l)
    l[locatiiplayer(l,setu)-1]=setu
    imprima(l)
    while not ( anywinner(l,setu) or istie(l)) :
        if setu=='x':
            setu='0'
        else :
            setu='x'
        l[locatiiplayer(l,setu)-1]=setu
        imprima(l)
    # Ask player for a rematch
    rematch = raw_input('Would you like to play again? y/n')
    if rematch == 'y':
        l=[' ']*9
        playgame(l)
    else:
        print "Thanks for playing!"


# In[9]:

l=[' ']*9
playgame(l)


# In[ ]:



