## Task 0.1: Preparations - Python
"""
ITU KSADMAL1KU-NLP - Advanced Machine Learning for NLP in KCS 2024

by Stefan Heinrich, Bertram Højer, Christian H. Rasmussen, & material by Kevin Murphy.

All info and static material: https://learnit.itu.dk/course/view.php?id=3024579

-------------------------------------------------------------------------------
"""


print("Testing all requirements. You are good if no exception pops up.")

import numpy as np
a = np.array([1, 2])

import pandas as pd

b = pd.read_csv("../data/test.csv", names=['a', 'b'])

from sklearn.preprocessing import normalize
c = normalize(b.values, axis=0, norm='max')

import matplotlib.pyplot as plt
d = plt.plot(b)
plt.savefig('pandas_test.png')
plt.close()

import seaborn as sns
e = sns.lineplot(data=c)
e.get_figure().savefig('seaborn_test.png')

print("Testing done.")
