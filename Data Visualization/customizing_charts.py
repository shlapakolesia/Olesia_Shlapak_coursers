import pandas as pd
import plotly.express as px

data = {
    'Model': ['Model A', 'Model B', 'Model C', 'Model D'],
    'Accuracy': [0.85, 0.90, 0.75, 0.95],
    'F1 Score': [0.83, 0.88, 0.70, 0.92],
    'Training Time (s)': [120, 150, 90, 200]
}

df = pd.DataFrame(data)
print(df.head())

fig = px.line(df, x='Model', y='Accuracy', title='Model Accuracy Comparison')
fig.show()

fig = px.bar(df, x='Model', y='Training Time (s)', title='Model Training Time')
fig.show()

fig = px.pie(df, values='Accuracy', names='Model', title='Accuracy Proportion')
fig.show()

fig = px.box(df, y='Accuracy', title='Accuracy Distribution')
fig.show()
