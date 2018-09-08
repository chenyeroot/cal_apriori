import apriori as ap  #把apriori.py导入，可使用sys模块
import pandas as pd

df_class = pd.read_excel(".../df_class.xlsx")

print(u'\n转换原始数据至0-1矩阵...')
ct = lambda x : pd.Series(1, index = x[pd.notnull(x)]) #转换0-1矩阵的过渡函数
b = map(ct, df_class.as_matrix()) #用map方式执行
df_class = pd.DataFrame(list(b)).fillna(0) #实现矩阵转换，空值用0填充
print(u'\n转换完毕。')
#del b #删除中间变量b，节省内存

support = 0.01  #最小支持度
confidence = 0.1 #最小置信度
ms = '---' #连接符，默认'--'，用来区分不同元素，如A--B。需要保证原始表格中不含有该字符

result = ap.find_rule(df_class, support, confidence, ms).to_excel('.../result.xlsx')
