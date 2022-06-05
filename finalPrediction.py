# #以下为预测
import warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report#用来算准确率
from sklearn.metrics import accuracy_score

from sklearn.naive_bayes import GaussianNB #朴素贝叶斯
from sklearn.neighbors import KNeighborsClassifier #K最邻近算法
from sklearn.tree import DecisionTreeClassifier #决策树算法
from sklearn.ensemble import RandomForestClassifier #随机森林算法
from sklearn.linear_model import SGDClassifier #随机梯度下降算法


def report(np_data,np_target,gnb):
    trainX,testX,trainY,testY = train_test_split(np_data,np_target,test_size=0.8,random_state=45)
    gnb  = gnb
    gnb.fit(trainX,trainY)

    # print(np_data)
    # print("--------")
    # print(trainX)
    # print("--------")
    # print(testX)

    # 模型测试

    y_pred = gnb.predict(testX)
    # print(testY)#正确答案
    # print(y_pred)#为预测结果 共有30个结果
    score = accuracy_score(testY,y_pred)
    report = classification_report(testY,y_pred) #原为accuracy 是准确率的意思
    print(score)