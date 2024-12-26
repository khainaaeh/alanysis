from heapq import nlargest
import matplotlib.pyplot as plt
import pandas as pd
from fontTools.merge.util import first

game_metrics = pd.read_csv('../datasets/Video Game Sales/vgchartz-2024.csv')

# ТОП 10 ПРОДАЖ
groupedArray = game_metrics.groupby('title').agg({
    'total_sales': 'sum',
    'release_date': 'first'
})
top10sales = groupedArray.nlargest(10, 'total_sales')
print(f'Топ 10 игр по продажам за всю историю:\n{top10sales}\n\n')


# ТОП 10 СКОр
groupedArray = game_metrics.groupby('title').agg({
    'critic_score': 'first',
    'release_date':'first',
})
top10Scores = groupedArray[groupedArray['critic_score'] >= 9.8]
print(f'Игры с оценкой больше 9.8:\n{top10Scores}\n\n')


# ИЗДАТЕЛИ
groupedArray = game_metrics.groupby('publisher').agg({
    'total_sales': 'sum',
})
top10Publishers = groupedArray.nlargest(10, 'total_sales')
print(f'Топ 10 издателей:\n{top10Publishers}\n\n')

plt.figure(figsize=(8, 8))
plt.pie(top10Publishers['total_sales'], labels=top10Publishers.index, autopct='%1.0f%%')
plt.title('Топ 10 издателей по суммарным продажам')
plt.axis('equal')
plt.tight_layout()
plt.show()

# ТОП 10 жанров по продажам
groupedArray = game_metrics.groupby('genre').agg({
    'total_sales': 'sum',
    'publisher': lambda x: x.mode()[0] if not x.mode().empty else 'Unknown'
})
top10Genres = groupedArray.nlargest(10, 'total_sales')
print(f'Топ жанров по общим продажам:\n{top10Genres}\n\n')
plt.figure(figsize=(10, 6))
plt.bar(top10Genres.index, top10Genres['total_sales'], color='skyblue')

plt.title('Топ жанров по общим продажам', fontsize=16)
plt.xlabel('Жанры', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.ylabel('Общие продажи (в млн)', fontsize=12)
plt.tight_layout()
plt.show()


