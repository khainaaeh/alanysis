import pandas as pd

game_metrics = pd.read_csv('../datasets/game_metrics.csv')
print(f'Всего сессий: {int(len(game_metrics))}')

game_metrics['session_type'] = game_metrics['session_duration_min'].apply(lambda x: 'Длинная' if x > 60 else 'Короткая')

segmented_data = game_metrics.groupby('session_type')[['completion_rate']].mean()

longSessionCount = game_metrics['session_type'].value_counts()['Длинная']
shortSessionCount = game_metrics['session_type'].value_counts()['Короткая']
print(f'Количество коротких сессий: {shortSessionCount}')
print(f'Количество длинных сессий: {longSessionCount}')


print(segmented_data)