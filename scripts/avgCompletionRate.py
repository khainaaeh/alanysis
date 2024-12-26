import pandas as pd
import matplotlib.pyplot as plt

game_metrics = pd.read_csv('../datasets/game_metrics.csv')
game_metrics['level_difficulty'] = game_metrics['completion_rate'].apply(lambda x: 'Сложный' if x < 0.5 else 'Простой')

game_metrics = game_metrics.groupby('level_difficulty')[['enemies_defeated', 'items_collected']].mean()


print(game_metrics)
