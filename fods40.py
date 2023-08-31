import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("sports_data.csv", encoding='latin-1')
# Calculate the average age of players
average_age = data['Age'].mean()
# Display the names of players above the average age
above_average_age_players = data[data['Age'] > average_age]['Name']
position_counts = data['Position'].value_counts()
plt.bar(position_counts.index, position_counts.values)
plt.xlabel('Position')
plt.ylabel('Number of Players')
plt.title('Distribution of Players Based on Positions')
plt.xticks(rotation=45)
plt.show()

print("Top 5 Goal Scorers:")
print(data.nlargest(5, 'Goals'))
print("\nTop 5 Highest Salaries:")
print(data.nlargest(5, 'Salary'))
print(f"\nAverage Age of Players: {average_age:.2f}")
print("\nPlayers Above Average Age:")
print(above_average_age_players)


'''
sample output 
Top 5 Goal Scorers:
                 Name  Age    Position  Goals   Salary
0        Lionel Messi   34     Forward     45  1000000
1   Cristiano Ronaldo   36     Forward     40   900000
4  Robert Lewandowski   33     Forward     38   700000
3       Kylian Mbappé   22  Midfielder     35   750000
2           Neymar Jr   29     Forward     30   800000

Top 5 Highest Salaries:
                 Name  Age    Position  Goals   Salary
0        Lionel Messi   34     Forward     45  1000000
1   Cristiano Ronaldo   36     Forward     40   900000
2           Neymar Jr   29     Forward     30   800000
3       Kylian Mbappé   22  Midfielder     35   750000
4  Robert Lewandowski   33     Forward     38   700000

Average Age of Players: 29.20

Players Above Average Age:
0          Lionel Messi
1     Cristiano Ronaldo
4    Robert Lewandowski
6           Luka Modric
7          Sergio Ramos
Name: Name, dtype: object
'''
