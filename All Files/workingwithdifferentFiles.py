import json
import pandas as pd
import numpy as np
# pip install matplotlib
import matplotlib 
import matplotlib.pyplot as plt

# url ='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv'
# df = pd.read_csv(url,header=None)

# df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']
# df[['State']]

# df = df[['First Name', 'Last Name', 'Location ', 'City','State','Area Code']]
# df.columns
# reset = ['First Name', 'Last Name', 'City', 'Location ','Area Code','State']
# df = df[reset]

# df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
# df = df.transform(func = lambda x : x + 10)

# result = df.transform(func = ['sqrt'])
# df.loc[0:3]

# df.loc[[0,2], "a" ]

# df.iloc[[0,1,2], 1]

person = {
    'first_name' : 'Muhammad Umer',
    'last_name' : 'Khan',
    'age' : 18,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "Karachi",
        "state": "Kr",
        "postalCode": "10021-3100"
    }
}
with open('person.json', 'w') as f:  # writing JSON object
    json.dump(person, f)

with open('person.json', 'r') as Openfile: 
  
    # Reading from json file 
    json_Object = json.load(Openfile)    
# Serializing json  
json_Object = json.dumps(person, indent = 4) 
  
# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    outfile.write(json_object) 
    
with open('sample.json', 'r') as openfile: 
  
    # Reading from json file 
    json_object = json.load(openfile) 
  
print(json_object) 
print(type(json_object)) 