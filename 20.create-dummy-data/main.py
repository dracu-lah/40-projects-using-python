#  install faker, pandas using pip

from faker import Faker

import pandas as pd
fake = Faker()
data = [fake.profile() for i in range(50)]
data = pd.DataFrame(data)
print(data.head())