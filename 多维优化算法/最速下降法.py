#原函数为f=(x1-4)^4+(x2-3)^2+4*(x3+5)^4

def Solve_Grid(x):
    """此函数负责求解梯度"""
    g=[float(4*(x[0]-4)*(x[0]-4)*(x[0]-4)),2*(x[1]-3),16*(x[2]+5)*(x[2]+5)*(x[2]+5)]
    return g

def Solve_H(x):
    """此函数负责求解黑塞矩阵"""
    H=[[12*(x[0]-4)*(x[0]-4),0.0,0],[0.0,2,0],[0.0,0,48*(x[2]+5)*(x[2]+5)]]
    return H

def Solve_α(g,H):
    """此函数负责求解每一步下降的步长α"""
    temp1=0.0
    temp2=[0.0,0,0]
    temp3=0.0

    for i in range(0,3):
        temp1=temp1+g[i]*g[i]

    for i in range(0,3):
        for j in range(0,3):
            temp2[i]=temp2[i]+g[j]*H[j][i]

    for i in range(0,3):
        temp3=temp3+temp2[i]*g[i]

    return temp1/temp3

if __name__=='__main__':

    x=[4.0,2,-1]#起始点
    n=0.1

    for i in range(0,10001):
        if i==10*n:
            print(f"第{i}次迭代后得到的结果为：{x}")
            n=n*10
        g=Solve_Grid(x)
        α=Solve_α(g,Solve_H(x))
        for j in range(0,3):
            x[j]=x[j]-α*g[j]
