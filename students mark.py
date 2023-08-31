import numpy as np
import pandas as pd
a={'maths':['40','23','33','45','87'],
   'science':['23','56','78','89','34'],
   'english':['23','76','43','76','80'],
   'history':['34','56','78','98','48']}
b=pd.DataFrame(a)
print(b)
science=np.array([23,56,78,89,34])
mean=np.mean(science)
print(mean)
