import matplotlib.pyplot as plt
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
#画图部分
#单个画布
def draw(np_data,np_day,figWidth,figHeight,oneCanvas):

    plt.figure(figsize=(figWidth,figHeight),facecolor="gray")
    
    if oneCanvas:
        plt.subplot(311)#分成2x2的矩阵区域 占用编号为1的区域 即1行1区

    plt.plot(np_day[:,0],np_data[:,0],marker='o',c='g',label="治愈人数")#创建一个治愈人数的线图
    plt.legend()
    # for x,y in zip(np_day[:,0],np_data[:,0]):
    #     plt.text(x,y,'%.0f' % y,fontdict={'fontsize':10})
    # plt.title("治愈人数线图")
    plt.xticks(rotation=45)
    plt.savefig('cure.jpg')
    if oneCanvas:
        plt.subplot(312)#分成2x2的矩阵区域 占用编号为2的区域 即1行2区
    else:
        plt.figure(figsize=(figWidth,figHeight),facecolor="gray")
    

    plt.plot(np_day[:,0],np_data[:,1],marker='o',c='r',label="确诊人数")#创建一个确诊人数的线图
    plt.legend()
    # for x,y in zip(np_day[:,0],np_data[:,1]):
    #     plt.text(x,y,'%.0f' % y,fontdict={'fontsize':10})
    # plt.title("确诊人数线图")
    plt.xticks(rotation=45)
    plt.savefig('sure.jpg')
    if oneCanvas:
        plt.subplot(313)#分成2x1的矩阵区域 占用编号为2的区域 第2行
    else:
        plt.figure(figsize=(figWidth,figHeight),facecolor="gray")
    plt.plot(np_day[:,0],np_data[:,2],marker='o',c='k',label="死亡人数")#创建一个死亡人数的线图
    
    plt.legend()
    # for x,y in zip(np_day[:,0],np_data[:,2]):
    #     plt.text(x,y,'%.0f' % y,fontdict={'fontsize':10})
    # plt.title("死亡人数线图")
    plt.xticks(rotation=45)
    
    plt.savefig('die.jpg')
    plt.show()