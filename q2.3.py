import os
import pandas as pd

# پیدا کردن نام دقیق فایل اکسل
filename = '3.xlsx'
for f in os.listdir('.'):
    if '3.xlsx' in f:
        filename = f
        break

# خواندن فایل اکسل
df = pd.read_excel(filename)
df.columns = df.columns.str.strip()

# فیلتر کردن داده‌ها برای بازه 100KB تا 600KB بر اساس صورت سوال
# (حتی اگر داده 700KB اضافه شده باشد، این سطرها فیلتر می‌شوند)
df_filtered = df[df.iloc[:, 0].isin(['100KB', '200KB', '300KB', '400KB', '500KB', '600KB'])]

# استخراج ستون مربوط به الگوریتم ۲ و محاسبه میانگین
alg2_times = df_filtered['Alg.2']
mean_alg2 = alg2_times.mean()

print("--- محاسبه میانگین زمان اجرای الگوریتم ۲ ---")
print("زمان‌های اجرا:", list(alg2_times))
print(f"میانگین زمان اجرای الگوریتم ۲ برای داده‌های ۱۰۰ تا ۶۰۰ کیلوبایت: {mean_alg2}")