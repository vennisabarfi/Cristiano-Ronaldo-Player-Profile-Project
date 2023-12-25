#!/usr/bin/env python
# coding: utf-8

# In[1]:


#### Import packages and modules
import pandas as pd
import numpy as np
import data_processing_ronaldo as dp #Python file containing original dataframe



# In[2]:


table = dp.ret_df() #original dataframe with all the data
table2 = dp.ret_df2()


# In[3]:


table # view dataframe


# In[4]:


# Total goals scored analysis functions
def TotalGoals(): # Total career goals for Ronaldo
    goal_count = table['Date']
    return len(goal_count) 

# Total goals scored per club 
ron_alnassr = table[table["Squad"] == "Al-Nassr"] # filtering for AlNassr
ron_manutd = table[table["Squad"]== 'Manchester Utd'] # filtering for Man Utd
ron_realmadrid = table[table["Squad"] == "Real Madrid"] # filtering for Real Madrid
ron_juventus = table[table["Squad"] == "Juventus"] # filtering for Juventus
ron_sportingcp = table[table["Squad"] == "Sporting CP"] # filtering for Sporting CP

# Total goals scored for country
ron_portugal = table[table["Squad"] == "Portugal"] # filtering for Portugal

# Game-Starts per team 
start_alnassr = ron_alnassr[ron_alnassr["Start"] != "N"]
start_manutd = ron_manutd[ron_manutd["Start"] != "N"]
start_juventus = ron_juventus[ron_juventus["Start"]!="N"]
start_realmadrid = ron_realmadrid[ron_realmadrid["Start"] != "N"]
start_sportingcp = ron_sportingcp[ron_sportingcp["Start"] != "N"]

# Teams Ronaldo scored against the most
max_team = table["Opponent"].value_counts()
top_opponents1 = max_team.head(5)
top_opponents = pd.Series({"Sevilla" : 27,"Getafe":23,"Atlético Madrid":20, "Athletic Club":17,"Málaga":17  }) #create a series

print(len(start_realmadrid))
print(max_team)
print(top_opponents)


# In[5]:


# Building a class for data analysis based on team

class TeamAnalysis():
    
    def __init__(self,team_name, start):
        self.team_name = team_name
        self.start= start
        
        
    def goals_for_team(team_name): #total goals per team 
        return len(team_name)
    
    def team_start(start): #number of starts per team 
        return len(start)
    

        
        
#     def goals_per_game(team_name): 
# do average expected goals per team
# team Ronaldo scored the most against and how many
    


# In[6]:


TeamAnalysis.goals_for_team(ron_sportingcp)


# In[7]:


TeamAnalysis.team_start


# In[8]:


# Competition Analysis

#goals per major competitions
ron_uefa = table[table["Competition"]=="Champions Lg"] # champions leage
ron_premierlg = table[table["Competition"]=="Premier League"]
ron_laliga = table[table["Competition"]=="La Liga"]
ron_uefan = table[table["Competition"] == "UEFA Euro"] # uefa nations league
ron_serie_a =  table[table["Competition"]=="Serie A"] # serie a
ron_worldcup = table[table["Competition"]=="World Cup"] # world cup
ron_friendlies = table[table["Competition"]== "Friendlies (M)"] # friendlies
ron_primeira = table[table["Competition"] == "Primeira Liga"] # portuguese league

print(len(ron_primeira))


# In[9]:


# Personal Stats Analysis

# Type of goals
# Body Parts
left_foot_goals= table[table["Body Part"] == "Left Foot"] # goals scored with Ronaldo's left foot
right_foot_goals = table[table["Body Part"] == "Right Foot"] # right foot
header_goals = table[table["Body Part"] == "Head"]
# outside of the box shot and 18 yeard goals
eighteen_yard = table.query("Distance <= 18") # goals within the 18 yard box
out_eighteen_yard = table.query("Distance > 18") #goals beyond 18 yard box


def type_goal(goal):  # use for later. Can used these three options above
    return len(goal)

type_goal(out_eighteen_yard)

# Goal creating event
GCA1 = table["GCA1"].value_counts().head(5) # first offensive action leading directly to a shot s.a. take-ons, drawing fouls, passes etc.

# goalkeepers with most goals scored against
easy_goalkeepers = table["Goalkeeper"].value_counts().head(5)

# toughest goalkeepers against ronaldo
hardest_goalkeepers = table["Goalkeeper"].value_counts(ascending= True). head(5) #reverses order to find the lowest

# Player most received assists
player_assists = table["Assist"].value_counts()

overall_stats = pd.DataFrame(table.describe()) 

# longest distance to goal
overall_stats.iloc[7] # redo to just get the columns with the headers




# In[10]:


table2 # view 2nd dataframe


# In[12]:


# Time Series Analysis
# Goals per season
goals_per_season = table2["Gls"]

# Shots on Target per season
sot_per_season = table2["SoT"]


# Shot-to-goal conversion
stg_per_season = table2["G/SoT"]
print(stg_per_season)

# Average minutes played per 90 minutes per season
min_per_season = table2["90s"]


# In[10]:


pip install matplotlib


# In[13]:


import matplotlib.pyplot as plt
import matplotlib as mpl


# In[14]:


#### Graphing Statistics ###

# # Total goals scored per club 
# ron_alnassr = table[table["Squad"] == "Al-Nassr"] # filtering for AlNassr
# ron_manutd = table[table["Squad"]== 'Man Utd'] # filtering for Man Utd
# ron_realmadrid = table[table["Squad"] == "Real Madrid"] # filtering for Real Madrid
# ron_juventus = table[table["Squad"] == "Juventus"] # filtering for Juventus
# ron_sportingcp = table[table["Squad"] == "Sporting CP"] # filtering for Sporting CP

# # Total goals scored for country
# ron_portugal = table[table["Squad"] == "Portugal"] # filtering for Portugal



# In[15]:


my_color = list("bgc")
player_assists.head().plot(kind='bar', color= my_color)
plt.title("Top Assists", fontsize = 20, fontweight ="bold")
plt.xlabel("Player Name", fontweight ="bold", fontsize = 15)
plt.ylabel("Number of Assists", fontweight = "bold", fontsize = 15)


# In[16]:


# Teams Ronaldo has scored the most against
top_opponents1 = max_team.head(5)
top1 = list(top_opponents)

my_colors = list('ygbm')
top_opponents1.plot(kind='bar',color= my_colors)
plt.title("Teams with most conceded goals", fontsize =15, fontweight = "bold")
plt.xlabel("Team",fontweight = "bold")
plt.ylabel("Goals by Ronaldo", fontweight = "bold")




# In[17]:


# Type of goal scored by Ronaldo (Body Part)
# Type of goals
# Body Parts
left_foot_goals= table[table["Body Part"] == "Left Foot"] # goals scored with Ronaldo's left foot
right_foot_goals = table[table["Body Part"] == "Right Foot"] # right foot
header_goals = table[table["Body Part"] == "Head"]

lfg = len(left_foot_goals)
rfg = len(right_foot_goals)
hg = len(header_goals)
print(lfg)
print(rfg)
print(hg)

type_goal = pd.Series({"Right Foot": rfg, "Left Foot":lfg, "Headers":hg})
type_goal
labels1= ["Right Foot","Left Foot","Headers"]
labels2 = ["Right Foot: 110", "Left Foot: 35","Headers: 28"]
# labels2 = [110,35,28]
plt.title("Type of Goal", fontsize= 25)
plt.pie(type_goal,labels = labels1,
        startangle = 90,
shadow = True,
explode =(0,0.1,0.1),
autopct ='%1.1f%%')

plt.legend(loc="upper left",
           labels = labels2,
           draggable = "True", shadow="True")





# In[18]:


# Goals scored per team

# Total goals scored per club 
ron_alnassr = table[table["Squad"] == "Al-Nassr"] # filtering for AlNassr
ron_manutd = table[table["Squad"]== 'Manchester Utd'] # filtering for Man Utd
ron_realmadrid = table[table["Squad"] == "Real Madrid"] # filtering for Real Madrid
ron_juventus = table[table["Squad"] == "Juventus"] # filtering for Juventus
ron_sportingcp = table[table["Squad"] == "Sporting CP"] # filtering for Sporting CP
# Portugal
ron_portugal = table[table["Squad"] == "Portugal"] # filtering for Portugal

gal = len(ron_alnassr)
gmu = len(ron_manutd)
grm = len(ron_realmadrid)
gju = len(ron_juventus)
gsp = len(ron_sportingcp)
gpt = len(ron_portugal)

total_per_club = pd.Series({"Al Nassr": gal,"Manchester United":gmu,
                             "Real Madrid": grm,"Juventus": gju,
                             "Sporting Lisbon": gsp,"Portugal": gpt})

goals = [gal,gmu,grm,gju,gsp,gpt]

for index, value in enumerate(goals):
    plt.text(value, index,
             str(value))

my_colors = list('bgm')
total_per_club.plot.barh(color = my_colors)
plt.xlabel("Goals Scored", fontweight = "bold", fontsize = 16)
plt.ylabel("Team", fontweight = "bold", fontsize = 16)
plt.title("Goals Scored per Team", fontweight="bold", fontsize = 20)





# In[19]:


# Graph this:

# Competition Analysis

#goals per major competitions
ron_uefa = table[table["Competition"]=="Champions Lg"] # champions leage
ron_premierlg = table[table["Competition"]=="Premier League"]
ron_laliga = table[table["Competition"]=="La Liga"]
ron_serie_a =  table[table["Competition"]=="Serie A"] # serie a
ron_primeira = table[table["Competition"] == "Primeira Liga"] # portuguese league

ru = len(ron_uefa)
rpl = len(ron_premierlg)
rl = len(ron_laliga)
rs = len(ron_serie_a)
rpr = len(ron_primeira)


print(len(ron_primeira))

total_per_comp = pd.Series({"UEFA Champions League": ru,"English Premier League":rpl,
                             "La Liga": rl,"Serie A": rs,
                             "Primeira Liga": rpr})

club_goals = [ru,rpl,rl,rs,rpr]

for index, value in enumerate(club_goals):
    plt.text(value, index,
             str(value))

my_colors = list('rcy')
total_per_comp.plot.barh(color = my_colors)
plt.xlabel("Goals Scored", fontweight = "bold", fontsize = 16)
plt.ylabel("Competition", fontweight = "bold", fontsize = 16)
plt.title("Goals Scored per Competition (Club)", fontweight="bold", fontsize = 20)


# In[20]:


# National Team
ron_uefan = table[table["Competition"] == "UEFA Euro"] # uefa nations league
ron_worldcup = table[table["Competition"]=="World Cup"] # world cup
ron_friendlies = table[table["Competition"]== "Friendlies (M)"] # friendlies

rue = len(ron_uefan)
rwc = len(ron_worldcup)
rfr = len(ron_friendlies)

total_per_ncomp = pd.Series({"UEFA Nations League": rue,"FIFA World Cup":rwc,
                             "Friendlies": rfr})

club_goals1 = [rue,rwc,rfr]

for index, value in enumerate(club_goals1):
    plt.text(value, index,
             str(value))

my_colors = list('gcy')
total_per_ncomp.plot.barh(color = my_colors)
plt.xlabel("Goals Scored", fontweight = "bold", fontsize = 16)
plt.ylabel("Competition", fontweight = "bold", fontsize = 16)
plt.title("Goals Scored per Competition(Nation)", fontweight="bold", fontsize = 18)


# In[21]:


# Goals per season
goals_per_season.plot(kind='barh',color= 'blue')
plt.xlabel("Goals Scored", fontweight="bold",fontsize=16)
plt.ylabel("Season", fontweight="bold",fontsize=16)
plt.title("Goals Scored per Season", fontweight="bold", fontsize = 20)
# add labels to each bar
for index, value in enumerate(goals_per_season):
    plt.text(value, index,
             str(value))


# In[22]:


# Shots on Target per season
my_colors3 = list('rcyb')
sot_per_season.plot(color="c")
plt.xlabel("Season", fontweight="bold",fontsize=16)
plt.ylabel("Shots on Target", fontweight="bold",fontsize=16)
plt.title("Shots on Target per Season", fontweight="bold",fontsize=20)


# In[34]:


#Shot-to-goal conversion

stg_per_season.plot()
plt.xlabel("Season", fontweight='bold',fontsize=14)
plt.ylabel("Shot-to-Goal Conversion", fontweight="bold",fontsize=14)
plt.title("Shot-to-Goal Conversion per Season", fontweight="bold", fontsize=18)


# In[48]:


table.describe()


# In[41]:


# Then graph this
table2.describe()


# In[ ]:




