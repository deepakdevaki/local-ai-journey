import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

np.random.seed(42)
X, _ = make_classification = lambda: (np.random.randn(1000, 5), None)
X = np.random.randn(1000, 5)
df = pd.DataFrame(X, columns=['exp','gpa','test','ref','int'])
df['female'] = np.random.binomial(1, 0.45, 1000)
df['hired'] = ((df['test'] + df['int'] + np.where(df['female'], -1.5, 0)) > 1.2).astype(int)

X = df[['exp','gpa','test','ref','int']]
y = df['hired']
prot = df['female']

X_train, X_test, y_train, y_test, p_train, p_test = train_test_split(X, y, prot, test_size=0.3, random_state=42, stratify=y)

model = RandomForestClassifier().fit(X_train, y_train)
pred = model.predict(X_test)

f_mask = (p_test == 1)
m_mask = (p_test == 0)
di = pred[f_mask].mean() / pred[m_mask].mean()

print("⚖️ Week 5: Fair Hiring Simulator")
print(f"Disparate Impact: {di:.2f} ({'Fair' if di >= 0.8 else 'Biased'})")