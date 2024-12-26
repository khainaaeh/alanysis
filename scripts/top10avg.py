import pandas as pd
import matplotlib.pyplot as plt

GameMetrics = pd.read_csv("../datasets/game_metrics.csv")

TopTenPercent = GameMetrics.nlargest(int(len(GameMetrics) * 0.1), 'session_duration_min')

MeanValues = TopTenPercent[['level', 'items_collected', 'currency_spent', 'currency_earned']].mean()

print(MeanValues)

