# library
import matplotlib.pyplot as plt
from matplotlib_venn import venn3
import random

set1 = {random.randint(0,4000) for _ in range(1000)}
set2 = {random.randint(1000,5000) for _ in range(1000)}
set3 = {random.randint(3500,6000) for _ in range(1000)}

# Use the venn2 function
venn3([set1, set2, set3], ['set1', 'set2', 'set3'])
plt.show()
