
import json 
import pandas as pd
from collections import defaultdict
import matplotlib.pyplot as plt

file = "laureate.json"

#Step 1: convert file to json
with open(file) as json_file: 
    content = json.load(json_file)
    laureates = content['laureates']

# Step 2: Count laureats by bornCountryCode,
# using defaultdict(int) as a counter:
counts = defaultdict(int)
for laureate in laureates:
    counts[laureate.get('bornCountry', 'Missing: Born Country')] += 1

df = pd.DataFrame([[k] + [v] for k, v in counts.items()], 
                   columns=['bornCountry', 'count']).sort_values(by='count')
top_countries = df[df['count'] > 10 ]

fig, ax = plt.subplots()
fig.set_tight_layout(True)
plt.barh( top_countries['bornCountry'] , top_countries['count'], height=0.5 , color="slateblue" )
plt.gca().invert_yaxis()
plt.title('Count of Nobel Laureates by their country of birth')
plt.ylabel ('Country')
plt.xlabel('Count')

_, xmax = plt.xlim()
plt.xlim(0, xmax+50)
for i, v in enumerate(top_countries['count']):
    ax.text(v + 20, i, str(v), color='black', fontweight='bold', fontsize=8, ha='left', va='center')
plt.show()
