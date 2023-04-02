
'''创建一个线性拟合并绘制散点图、拟合曲线的函数
该程序通过传入np.array类型的两组数据（x,y），返回拟合曲线的斜率a和截距b，并计算相关系数r、斜率标准差s、标准不确定度u（P=0.683），并绘制散点图、拟合曲线。
可选参数：
example:
import lrqlib as lrq

v = [2.942330326,2.884219201,2.822405558,2.761159687,2.694757472,2.628811777,2.559726962,2.487562189,2.412129566]
t = [0.2549,0.2427,0.2303,0.2173,0.2041,0.1902,0.1758,0.1608,0.1451]

a,b,r,s,u = lrq.linear(t,v)

output:
a= 4.833110377949369 b= 1.7101157908567044
r= 0.9999872505668137
s= 0.009224488269169263
u= 0.0009785735339269013

'''


def linear(xl, yl, font='E:\\网盘文件快传\\MiSans\\MiSans 开发下载字重\\MiSans-Semibold.ttf', xlim=None, ylim=None, title=None, xlabel='x', ylabel='y', size=(8,6), extend=True):
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib
    from scipy import optimize
    from math import sqrt
    # 字体设置
    zhfont1 = matplotlib.font_manager.FontProperties(fname=font)

    x = np.array(xl)
    y = np.array(yl)

    # 线性拟合
    def linear_fit(x, y):
        n = len(x)
        x_avg = np.mean(x)
        y_avg = np.mean(y)
        a = np.sum((x-x_avg)*(y-y_avg))/np.sum((x-x_avg)**2)
        b = y_avg - a*x_avg
        return a, b
    # 拟合

    def residuals(p):
        a, b = p
        return y - (a*x+b)
    a, b = optimize.leastsq(residuals, [1, 1])[0]
    print('a=', a, 'b=', b)
    # 计算相关系数
    r = np.corrcoef(x, y)[0, 1]
    print('r=', r)
    # 计算斜率标准差
    s = a*sqrt((1/r**2-1)/(len(x)-2))
    print('s=', s)
    # 计算不确定度
    u = sqrt(np.sum((y-(a*x+b))**2)/(len(x)-2))
    print('u=', u)
    # 绘图
    plt.figure(figsize=size)
    plt.title(title,fontproperties=zhfont1,fontsize=20,loc='center',color="black")
    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)
    plt.scatter(x, y, color='red', label='实验数据')
    plt.plot(x, a*x+b, color='blue', label='拟合曲线')
    plt.xlabel(xlabel, fontproperties=zhfont1)
    plt.ylabel(ylabel, fontproperties=zhfont1)
    #判断是否绘制拟合曲线延长线
    if extend:
        plt.axline((0,b),(1,a+b),color = 'b', ls = '--')
    plt.legend(prop=zhfont1)
    plt.show()
    return a, b, r, s, u
