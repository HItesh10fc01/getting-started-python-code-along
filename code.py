# --------------
import yaml


# Read the data of the format .yaml type
with open(path) as f:
    data = yaml.load(f)

# Find data type of the file
print(type(data))

# In which city, and at which venue the match was played and where was it played ?

city_name = data['info']['city']
venue_name = data['info']['venue']
print ("The Match played at {0} and The Name of venue {1}".format(city_name,venue_name))

# Which are all the teams that played in the tournament ? How many teams participated in total?
print (data['info']['teams'])
print (len(data['info']['teams']))

# Which team won the toss and what was the decision of toss winner ?
Toss_WIner = data['info']['toss']['winner']
Decision = data['info']['toss']['decision']
print ('The winer of toss is {0} and decision was {1}'.format(Toss_WIner,Decision))

# Find the first bowler and first batsman who played the first ball of the first inning
print (data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler'])
print (data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman'])

# How many deliveries were delivered in first inning ?
print(len(data['innings'][0]['1st innings']['deliveries']))

# How many deliveries were delivered in second inning ?
print(len(data['innings'][1]['2nd innings']['deliveries']))

# Which team won and how ?
print(data['info']['outcome']['winner'])
print (data['info']['outcome']['by']['runs'])



