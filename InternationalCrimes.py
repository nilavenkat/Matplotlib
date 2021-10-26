import pandas as pd
import matplotlib.pyplot as plt
 
df = pd.read_csv ('InternationalCrimes.csv')

NationalLevelSexualAssault = df[df["Series"]=="Total Sexual Violence at the national level"]
#print(len(NationalLevelSexualAssualt))
#print (NationalLevelSexualAssualt.columns)
all_sexual_assault = NationalLevelSexualAssault[['Year', 'Value']].groupby('Year').mean('Value').reset_index()
#print (all_sexual_assault.columns)
#print (all_sexual_assault)
NationalLevelTheft = df[df["Series"]=="Theft at the national level, population"]
all_theft = NationalLevelTheft[['Year', 'Value']].groupby('Year').mean('Value').reset_index()

fig, ax = plt.subplots()
fig.set_tight_layout(True)

plt.plot(all_sexual_assault['Year'],all_sexual_assault['Value'], label = 'Total Sexual Assualts in the world per 100,000')
plt.plot(all_theft['Year'],all_theft['Value'], label = 'Total Theft in the world per 100,000')
plt.title('Crime in the world per 100,000')
plt.xlabel('Year')
plt.ylabel('per 100,000')
plt.grid(color='grey', linestyle='-.', linewidth=0.5)
ax.legend()
plot1 = plt.figure(1)
#plt.show()

plt.show()
