#import pandas
import pandas as pd

dict = {
    "Name" : ["Haider", "Haidee", "King"],
    "City" : ["Pindi", "Islamabad", "Karachii"],
    "Games" : ["Pubg", "GTA 5", "DragonnBall Z"]
}
pd = pd.DataFrame(dict)
print(pd)

print('--------------------------------')
pd.index = ['First', 'Second', 'Third']
print(pd)

print(type(pd))  # type of pandas

