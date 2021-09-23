#原函数为f=1.5*x1^2+2*x2^2+1.5*x3^2+x1*x3+2*x2*x3-3*x1-x3
def Gaussian_Elimination(g,H):
    """此函数为实现高斯消元的函数"""

    for i in range(2,0,-1):
        n=i
        while n>0:
            temp=float(H[3-n][2-i]/H[2-i][2-i])
            for j in range(0,3):
                H[3-n][j]=H[3-n][j]-temp*H[2-i][j]
            g[3-n]=g[3-n]-temp*g[2-i]
            n=n-1

    for i in range(2,0,-1):
        n=i-1
        while n>=0:
            temp=float(H[n][i]/H[i][i])
            H[n][i]=H[n][i]-temp*H[i][i]
            g[n]=g[n]-temp*g[i]
            n=n-1

    for i in range(0,3):
        g[i]=g[i]/H[i][i]

    return g


def Solve_Grid(x):
    """此函数负责求解梯度"""
    g=[float(3*x[0]+x[2]-3),4*x[1]+2*x[2],x[0]+2*x[1]+3*x[2]-1]
    return g

def Solve_H(x):
    """此函数负责求解黑塞矩阵"""
    H=[[3.0,0,1],[0,4,2],[1,2,3]]
    return H

if __name__=='__main__':

    x=[0.0,0,0]

    # 对于二次型函数牛顿法可以一次迭代达到极值点
    for i in range(0,1):
        d=Gaussian_Elimination(Solve_Grid(x),Solve_H(x))
        for j in range(0,3):
            x[j]=x[j]-d[j]
        print(f"第{i+1}次迭代时，得到的近似解为{x}")
