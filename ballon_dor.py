import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


player_data =  {'Name' : ["Ousmane Dembele","Lamine Yamal", "Vitinha","Raphinha", "Mohammed Salah", "Kylian Mbappe", 
                          "Achraf Hakimi","Desire Duoe", "Kvicha Kvaratshkelia", "Nuno Mendes"],
                          'Goal' : [37,21,8,39,36,46,13,16,15,7],
                          'Assist' : [16,26,8,25,24,7,13,16,15,12],
                          'Club' : ['Paris Saint Germain', 'Fc Barcelona', 'Paris Saint Germain', 'Fc Barcelona', 'Liverpool', 'Real Madrid',
                                    'Paris Saint Germain', 'Paris Saint Germain', 'Paris Saint Germain', 'Paris Saint Germain']}
Rank = [1,2,3,4,5,6,7,8,9,10]               


df = pd.DataFrame(data=player_data, index=Rank)
df['GA'] = df['Goal'] + df['Assist'] #--> creating a column names GA which shows the total contribution of the player

print(f"Printing Dataframe \n {df}")
print('\n\n',df.describe()) #--> gives the basic statistics for the data set like mean, count, standard deviation, min & max

#df.to_csv('Ballon_dor_2025.csv')--> creating a CSV file from the data set

#now lets perform individual analysis, lets perform analysis on mo salah

player_index = 2

player_stat = f"{df.loc[player_index,'Goal']} {df.loc[player_index,'Assist']}" #assigning the row with mo salah's stats
print(player_stat)

#calculating the goal and assist %
percent_goal = (df.loc[player_index,'Goal'] / df.loc[5,'GA']) * 100
percent_assist = (df.loc[player_index,'Assist'] / df.loc[5,'GA']) * 100
percent_assist = (df.loc[player_index,'Assist'] / df.loc[5,'GA']) * 100
print(f"{df.loc[player_index, 'Name']} Goals Covered {percent_goal}% of his GA ")
print(f"{df.loc[player_index, 'Name']} Assists Covered {percent_assist}% of his GA ")

#filtering data 
filter_ = df[(df['Goal']> 40)] 
print(filter_)

#sorting data on the basis of total goals and assists
sort = df.sort_values(by='GA', ascending=False)
print('\n\n', sort)

print()

#converting the dataframe into a numpy array
print(df.to_numpy)


#plotting a graph that shows the total goal contributions of the players 
plt.bar(df['Name'], df['GA'])
plt.xticks(rotation=45, ha='right')
plt.title('Total Goal Contributions (2025 Ballon d\'Or Candidates)')
plt.show()
