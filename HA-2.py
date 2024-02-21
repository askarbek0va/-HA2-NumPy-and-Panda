# 1 - Question
'''A Series is a one-dimensional array of data. 
It can hold data of any type: string, integer, float, dictionaries, lists, booleans, and more.
'''
# 2 - Question
import pandas as pd 
a = [1, 2, 3,4,5,6,7,8,9,10,11,12]
months = pd.Series(a, index =['January','February','March','April','May','June','July','August','September','October','November','December'])
print('Months')
print(months)

# 3 - Question
groups={'MatMIE': 28,'Mat DAIS':29, 'COMIE': 31,'COMEC':34}
students = pd.Series(groups)
print('Groups')
print(students)


# 4 - Question
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
data=pd.DataFrame (exam_data, index=labels)
print (data )

# 5- Question
print('Number of attempts in the examination which are greater than 2:')
attempts2= data[data['attempts']>2]
print(attempts2)