import pandas as pd

game_metrics = pd.read_csv('../datasets/game_metrics.csv')

def categorized_session_duration_rate(rate):
    if rate < 30:
        return "Короткая"
    elif rate <= 60:
        return "Средняя"
    else:
        return "Высокая"

game_metrics['session_duration_segment'] = game_metrics['session_duration_min'].apply(categorized_session_duration_rate)

segmentation_analysis = game_metrics.groupby('session_duration_segment')[['items_collected', 'enemies_defeated', 'currency_earned']].mean()
print(segmentation_analysis)