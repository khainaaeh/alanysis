import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter


twitch_data = pd.read_csv('../datasets/Twitch_game_data.csv', encoding='latin1')
# monthly_views = twitch_data.groupby(['Year', 'Month'])['Hours_watched'].sum()
yearly_views = twitch_data.groupby('Year').agg({
    'Hours_watched': 'sum',
})
yearly_views['Days_watched'] = yearly_views['Hours_watched'] / 24
pd.options.display.float_format = '{:,.2f}'.format


plt.figure(figsize=(10, 8))
plt.bar(yearly_views.index, yearly_views['Days_watched'], color='skyblue')
plt.xlabel('Год')
plt.xticks(rotation=65)
plt.ylabel('Дни просмотра')
plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
plt.title('Количество дней просмотра по годам')
plt.tight_layout()
# print(yearly_views)
plt.show()


game_watched_hours = twitch_data.groupby('Game').agg({
    'Hours_watched': 'sum',
    'Avg_viewers': 'mean'
}).reset_index()
top10GamesWatched = game_watched_hours.nlargest(10, 'Hours_watched')

plt.figure(figsize=(15, 10))
plt.title('Топ 10 игр по количеству просмотров')
plt.bar(top10GamesWatched['Game'], top10GamesWatched['Hours_watched'], color='skyblue')
plt.xlabel('Игра')
plt.xticks(rotation=65)
plt.ylabel('Часы просмотра')
plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
plt.tight_layout()
plt.show()
# print(top10GamesWatched)




peak_viewers_game = twitch_data.groupby('Game')['Peak_viewers'].max().reset_index()
top10GamesByPeakViewers = peak_viewers_game.nlargest(10, 'Peak_viewers')
# print(top10GamesByPeakViewers)

plt.figure(figsize=(15, 10))
plt.title('Топ категорий с пиковым числом зрителей')
plt.bar(top10GamesByPeakViewers['Game'], top10GamesByPeakViewers['Peak_viewers'], color='red')
plt.xlabel('Категория')
plt.xticks(rotation=65)
plt.ylabel('Пиковое число зрителей')
plt.tight_layout()
plt.show()

top10AvgViewers = game_watched_hours.nlargest(10, 'Avg_viewers')
plt.figure(figsize=(15, 10))
plt.title('Топ категорий по среднему количеству зрителей')
plt.bar(top10AvgViewers['Game'], top10AvgViewers['Avg_viewers'], color='red')
plt.xlabel('Категория')
plt.xticks(rotation=65)
plt.ylabel('Среднее число зрителей')
plt.tight_layout()
plt.show()


filtered_data = twitch_data[twitch_data['Game'].isin(['League of Legends', 'Dota 2'])]
monthly_avg_viewers = filtered_data.groupby(['Year', 'Month', 'Game'])['Avg_viewers'].mean().reset_index()
monthly_avg_viewers['Date'] = monthly_avg_viewers['Year'].astype(str) + '-' + monthly_avg_viewers['Month'].astype(str)
monthly_avg_viewers['Date'] = pd.to_datetime(monthly_avg_viewers['Date'], format='%Y-%m')

lol_data = monthly_avg_viewers[monthly_avg_viewers['Game'] == 'League of Legends']
dota_data = monthly_avg_viewers[monthly_avg_viewers['Game'] == 'Dota 2']

plt.figure(figsize=(15, 10))
plt.bar(lol_data['Date'], lol_data['Avg_viewers'], label='LoL', alpha=0.7, color='blue', width=20)
plt.bar(dota_data['Date'], dota_data['Avg_viewers'], label='Dota2', alpha=0.7, color='red', width=20)

plt.xlabel('Месяцы')
plt.ylabel('Среднее количество зрителей')
plt.title('Среднее количество зрителей по месяцам для игр LoL и Dota2')
plt.xticks(rotation=65)
plt.legend()
plt.tight_layout()
plt.show()



