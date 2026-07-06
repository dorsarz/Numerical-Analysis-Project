import os
import pandas as pd
import matplotlib.pyplot as plt

# پیدا کردن نام دقیق فایل در پوشه جاری
filename = '3.xlsx'
for f in os.listdir('.'):
    if '3.xlsx' in f:
        filename = f
        break

# خواندن فایل اکسل
df = pd.read_excel(filename)

# تمیز کردن نام ستون‌ها و تبدیل سایزها به عدد
df.columns = df.columns.str.strip()
size_col = df.columns[0]
df[size_col] = df[size_col].astype(str).str.replace('KB', '').astype(int)

sizes = df[size_col]
algorithms = df.columns[1:]

# ۱. نمودار خطی
plt.figure(figsize=(8, 5))
for alg in algorithms:
    plt.plot(sizes, df[alg], marker='o', label=alg)
plt.title('Execution Time (Line Plot)')
plt.xlabel('Data Size (KB)')
plt.ylabel('Time')
plt.legend()
plt.grid(True)
plt.show()

# ۲. نمودار میله‌ای
df.plot(x=size_col, kind='bar', figsize=(8, 5))
plt.title('Execution Time (Bar Chart)')
plt.xlabel('Data Size (KB)')
plt.ylabel('Time')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

# ۳. نمودار جعبه‌ای
plt.figure(figsize=(7, 5))
plt.boxplot([df[alg] for alg in algorithms], labels=algorithms)
plt.title('Execution Time Distribution (Box Plot)')
plt.ylabel('Time')
plt.grid(axis='y')
plt.show()