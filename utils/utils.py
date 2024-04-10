import pycaret
# print(pycaret.__version__)  # 3.3.0
from pycaret.datasets import get_data
from pycaret.regression import *

data = get_data('insurance')
# print(data.head(5))

# 调用setup函数来初始化机器学习任务，指定data为使用的数据集，target='charges'表示模型的目标变量是charges列，即要预测的是保险费用
s = setup(data, target='charges')

best = compare_models()  # 调用compare_models()函数，该函数比较不同的机器学习模型并选择性能最好的模型

# 使用create_api(best, 'insurance_prediction_model')创建一个API，这个API将使用在上一步中选择的最佳模型
create_api(best, 'insurance_prediction_model')  # PyCaret has integration with FastAPI

