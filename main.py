import jsonProcess
import drawing
import finalPrediction
import numpy as np

data = jsonProcess.data_json

incTrend = data['incTrend']
data_list = []
day_list = []
target_list = [0]

def jsonToNumpy(test_data):
    for i in range(len(test_data)):
        temp_data = test_data[i]
        data_list.append([temp_data['cure_cnt'],temp_data['sure_cnt'],temp_data['die_cnt']])
        day_list.append([temp_data['day']])
        if i != 0:
            if temp_data['sure_cnt']-test_data[i-1]['sure_cnt'] >0:
                target_list.append(1)
            elif temp_data['sure_cnt']-test_data[i-1]['sure_cnt'] <0:
                target_list.append(-1)
            else:
                target_list.append(0)
jsonToNumpy(incTrend[0:])


np_data = np.array(data_list)
np_day = np.array(day_list)
np_target = np.array(target_list)


# drawing.draw(np_data,np_day,12,8,False)

from sklearn.naive_bayes import GaussianNB #朴素贝叶斯
from sklearn.neighbors import KNeighborsClassifier #K最邻近算法
from sklearn.tree import DecisionTreeClassifier #决策树算法
from sklearn.ensemble import RandomForestClassifier #随机森林算法
from sklearn.linear_model import SGDClassifier #随机梯度下降算法

# print('GaussianNB朴素贝叶斯\n')
# finalPrediction.report(np_data,np_target,GaussianNB())
# print('KNeighborsClassifierK最邻近算法\n')
# finalPrediction.report(np_data,np_target,KNeighborsClassifier())
# print('DecisionTreeClassifier决策树算法\n')
# finalPrediction.report(np_data,np_target,DecisionTreeClassifier())
# print('RandomForestClassifier随机森林算法\n')
# finalPrediction.report(np_data,np_target,RandomForestClassifier())
# print('SGDClassifier随机梯度下降算法\n')
# finalPrediction.report(np_data,np_target,SGDClassifier())
