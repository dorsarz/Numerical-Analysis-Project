import os
import pandas as pd

# پیدا کردن نام دقیق فایل اکسل در پوشه جاری
filename = '3.xlsx'
for f in os.listdir('.'):
    if '3.xlsx' in f:
        filename = f
        break

# خواندن داده‌های فعلی اکسل
df = pd.read_excel(filename)

# تعریف داده جدید به صورت دیکشنری (با توجه به نام ستون‌های فایل شما)
new_data = {
    df.columns[0]: '700KB',
    df.columns[1]: 80,
    df.columns[2]: 320,
    df.columns[3]: 700
}

# اضافه کردن سطر جدید به دیتافریم
df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

# ذخیره مجدد در فایل اکسل
df.to_excel(filename, index=False)
print("داده جدید با موفقیت به فایل اکسل اضافه شد.")