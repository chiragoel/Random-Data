import random as r

def fitness(x):
    for i in range(5):
        a = 0
        s = 100*(x[i+1] - x[i]*x[i])*(x[i+1] - x[i]*x[i]) + (x[i] - 1)*(x[i] - 1)
        a = a+s
    return a
    
    
fw = open("rand_data.csv","w+")
fw.write("SN,F1,F2,F3,F4,F5,F6,Value \n")
for i in range(100):
    x=[]
    x.append(round(r.uniform(10,100),2))
    x.append(round(r.uniform(-9,0),2))
    x.append(round(r.uniform(-50,-10),2))
    x.append(round(r.uniform(-20,-10),2))
    x.append(round(r.uniform(0,1),2))
    x.append(round(r.uniform(-5,-1),2))

    b = fitness(x)
    wr = "%d,%f,%f,%f,%f,%f,%f,%f \n"%(i,x[0],x[1],x[2],x[3],x[4],x[5],b)
    fw.write(wr)

   