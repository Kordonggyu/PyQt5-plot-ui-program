import pandas as pd
import random

time = []
column_data_A = []
column_data_B = []
column_data_C = []
column_data_D = []
data_file = {}

for i in range(14400):
    time.append(i)
    data = random.randrange(-300, 300)
    column_data_A.append(data)

for i in range(14400):
    data = random.randrange(-300, 300)
    column_data_B.append(data)

for i in range(14400):
    data = random.randrange(-300, 300)
    column_data_C.append(data)

for i in range(14400):
    data = random.randrange(-300, 300)
    column_data_D.append(data)

data_file['time(s)'] = time
data_file['A'] = column_data_A
data_file['B'] = column_data_B
data_file['C'] = column_data_C
data_file['D'] = column_data_D

# timekey = next(iter(data_file))

df = pd.DataFrame(data_file)
df.to_csv("./sampledata.csv", index = False)


