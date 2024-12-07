import pandas as pd
from statsmodels.multivariate.manova import MANOVA


data = pd.DataFrame({
    'Autor': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Słowa_kluczowe': [15, 16, 14, 12, 11, 13, 20, 21, 19],
    'Sentyment': [0.8, 0.9, 0.7, -0.2, -0.1, -0.3, 0.5, 0.6, 0.4],
    'Cytowania': [25, 26, 24, 30, 29, 31, 15, 16, 14]
})




manova = MANOVA.from_formula('Słowa_kluczowe + Sentyment + Cytowania ~ Autor', data=data)
print(manova.mv_test())