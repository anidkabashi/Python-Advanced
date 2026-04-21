import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather_tokyo_data.csv")

df.columns = df.columns.str.strip().str.lower()

df['temperature'] = df['temperature'].astype(str).str.replace(r"[()]", "", regex=True)
df['temperature'] = pd.to_numeric(df['temperature'])

df['date'] = pd.to_datetime(df['year'].astype(str) + "/" + df['day'])

avg_temp = df['temperature'].mean()
print(f"Average Temperature: {avg_temp:.2f}")

df['month'] = df['date'].dt.month
monthly_avg = df.groupby('month')['temperature'].mean()

print("\nMonthly Average:")
print(monthly_avg)

monthly_avg.plot(kind='bar')
plt.title("Monthly Average Temperature")
plt.show()

hottest = df.loc[df['temperature'].idxmax()]
coldest = df.loc[df['temperature'].idxmin()]

print("\n🔥 Hottest Day:")
print(hottest)

print("\n❄️ Coldest Day:")
print(coldest)

plt.plot(df['date'], df['temperature'])
plt.title("Temperature Trend")
plt.xticks(rotation=45)
plt.show()

def get_season(month):
    if month in [12,1,2]:
        return 'Winter'
    elif month in [3,4,5]:
        return 'Spring'
    elif month in [6,7,8]:
        return 'Summer'
    else:
        return 'Autumn'

df['season'] = df['month'].apply(get_season)

seasonal_avg = df.groupby('season')['temperature'].mean()

print("\nSeasonal Average:")
print(seasonal_avg)