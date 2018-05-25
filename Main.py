import matplotlib.pyplot as plt
import numpy as np



def define_Mazz(X_size , Y_size):
    Q0 = [] ; R0 = []
    for i in range(X_size):
        Q1 = []  ;   R1 = []
        for j in range(Y_size):
            dic = {}
            dic['Up'] = 0
            dic['Down'] = 0
            dic['Right'] = 0
            dic ['Left'] = 0
            if  j == 20-1 and i == 0 :
                R1.append(1000)
                Q1.append(dic)
            elif i >= 0 and i <= 17 and (j == 9 or j == 10)   :
                R1.append(-99)
                Q1.append(dic)
            else:
                R1.append(-1)
                Q1.append(dic)
        Q0.append(Q1)
        R0.append(R1)
    return Q0,R0
def best_move(x , y):
    cost = -9999999999
    for key,value in Q[x][y].items():
        if value > cost : move = key ; cost = value
    #print('Q['+str(x)+']['+str(y)+']= '+str(Q[x][y])+ '    best ='+str(move)+ '  cost='+str(cost))
    return move , cost
def MapIt():
    for i in range(20):
        result = []
        for j in range(20):
            move , cost = best_move(i , j)
            if move == 'Up' : move = '^'
            if move == 'Down': move = 'v'
            if move == 'Right': move = '>'
            if move == 'Left': move = "<"
            result.append(move)
            #result.append(val)
        print (result)
def Solve(P , x1 , y1 , alpha , gama):
    global Q
    if np.random.random_sample() > P:
        move = np.random.choice(['Up', 'Down', 'Left', 'Right'], 1, p=[0.25, 0.25, 0.25, 0.25])
        move = str(move)[1:-1].replace("'",'')
        current_val =  Q[x1][y1][move]
    else:
        [move , current_val] = best_move(x1 , y1)
    if move == 'Up' and x1 == 0:                    Q[x1][y1]['Up'] += R[x1][y1]
    elif move == 'Up' and x1 != 0:
            x1 -= 1
            next_dir , next_val = best_move(x1 , y1)
            Q[x1+1][y1]['Up'] += alpha * (R[x1][y1] + gama*(next_val) - current_val)
    elif move == 'Down' and x1 == 19:                 Q[x1][y1]['Down'] += R[x1][y1]
    elif move == 'Down' and x1 != 19:
            x1 += 1
            next_dir, next_val = best_move(x1, y1)
            Q[x1-1][y1]['Down'] += alpha * (R[x1][y1] + gama*(next_val) - current_val)
    elif move == 'Left' and y1 == 0:
            Q[x1][y1]['Left'] += R[x1][y1]
    elif move == 'Left' and y1 == 10 and x1 != 18 and x1 != 19:
            Q[x1][y1]['Left'] += R[x1][y1]
    elif move == 'Left' and y1 != 0  and (y1 != 10 or (x1 == 18 or x1 == 19)):
            y1 -= 1 ;
            next_dir, next_val = best_move(x1, y1)
            Q[x1][y1+1]['Left'] += alpha * (R[x1][y1] + gama*(next_val) - current_val)
    elif move == 'Right' and y1 == 19:
            Q[x1][y1]['Right'] += R[x1][y1]
    elif move == 'Right' and y1 == 9 and x1 != 18 and x1 != 19 :
            Q[x1][y1]['Right'] += R[x1][y1]
    elif  move == 'Right' and y1 != 19 and (y1 != 9 or (x1 == 18 or x1 == 19 )):
            y1 += 1
            next_dir, next_val = best_move(x1, y1)
            Q[x1][y1-1]['Right'] += alpha * (R[x1][y1] + gama*(next_val) - current_val)
    else:  print('!!!!!!!!!!!!!!!!! Error : Unknown status !!!!!!!!!!!!!!!!!!!!!!!'); print('x1 = '+str(x1)+ '  y1 = '+str(y1)+ '   move = '+move )
    return x1 , y1

def RL(deadline , P , LerningRate , gama ):
    path = []
    for w in range(deadline):
        x1 = 0
        y1 = 0
        counter = 0
        while True:
            #print counter
            #print(' i am in i='+str(i)+' j='+str(j))
            x1 , y1 = Solve(P , x1 , y1 , LerningRate , gama)
            counter += 1
            if x1 == 0 and y1 == 19:
                break

        #print (w , counter)
        path.append(counter)
    return path

gama_list = [ 0.4 , 0.5 , 0.6 , 0.7 , 0.8 , 0.9 ]
result = ''
rep = []
#for gama in gama_list:
P = 0.85
deadline = 1000
alpha = 0.1
Q,R = define_Mazz(20 , 20)


Q, R = define_Mazz(20, 20)
x = np.arange(1000)

result = RL(deadline , P , alpha , gama_list[0] )
print('======================================= gama   '+str(gama_list[0])+' =======================================')
MapIt() ; rep.append(result)

result =RL(deadline , P , alpha , gama_list[1] )
print('======================================= gama   '+str(gama_list[1])+' =======================================')
MapIt() ; rep.append(result) ;

result =RL(deadline , P , alpha , gama_list[2] )
print('======================================= gama   '+str(gama_list[2])+' =======================================')
MapIt() ; rep.append(result) ;

result =RL(deadline , P , alpha , gama_list[3] )
print('======================================= gama   '+str(gama_list[3])+' =======================================')
MapIt() ; rep.append(result) ;

result =RL(deadline , P , alpha , gama_list[4] )
print('======================================= gama   '+str(gama_list[4])+' =======================================')
MapIt() ; rep.append(result) ;

result =RL(deadline , P , alpha , gama_list[5] )
print('======================================= gama   '+str(gama_list[5])+' =======================================')
MapIt() ; rep.append(result) ;

fig = plt.figure()
ax1 = fig.add_subplot(2,3,1)
ax1.plot(x , rep[0] , 'r')
ax2 = fig.add_subplot(2,3,2)
ax2.plot(x , rep[1] , 'b')
ax3 = fig.add_subplot(2,3,3)
ax3.plot(x , rep[3] , 'g')
ax4 = fig.add_subplot(2,3,4)
ax4.plot(x , rep[3] , 'y')
ax5 = fig.add_subplot(2,3,5)
ax5.plot(x , rep[4] , 'c')
ax6 = fig.add_subplot(2,3,6)
ax6.plot(x , rep[5] , 'k')

plt.show()

fig.tight_layout()

plt.show()