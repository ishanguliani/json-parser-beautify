# json-parser-beautify
This script came up while trying to go through a 5 GB dataset with json data. There was a need to sift throught the json attributes in a nice looking (indented, spaced) json format to understand it better. This would then be represented it in an ER diagram. 

Basically view a file 'one_file.json' with garbled json data 
`{"business_id":"1SWheh84yJXfytovILXOAQ","name":"Arizona Biltmore Golf Club","address":"2818 E Camino Acequia Drive","city":"Phoenix","state":"AZ","postal_code":"85016","latitude":33.5221425,"longitude":-112.0184807,"stars":3.0,"review_count":5,"is_open":0,"attributes":{"GoodForKids":"False"},"categories":"Golf, Active Life","hours":null}
{"business_id":"QXAEGFB4oINsVuTFxEYKFQ","name":"Emerald Chinese Restaurant","address":"30 Eglinton Avenue W","city":"Mississauga","state":"ON","postal_code":"L5R 3E7","latitude":43.6054989743,"longitude":-79.652288909,"stars":2.5,"review_count":128,"is_open":1,"a`

as a beautiful data
`
{
  "business_id": "1SWheh84yJXfytovILXOAQ",
  "name": "Arizona Biltmore Golf Club",
  "address": "2818 E Camino Acequia Drive",
  "city": "Phoenix",
  "state": "AZ",
  "postal_code": "85016",
  "latitude": 33.5221425,
  "longitude": -112.0184807,
  "stars": 3.0,
  "review_count": 5,
  "is_open": 0,
  "attributes": {
    "GoodForKids": "False"
  },
  "categories": "Golf, Active Life",
  "hours": null
}
`



# How to use (works with python 2.7 and python 3)

NOTE: download the file `parse.py` in the same working directory as your json files then run the following commands from terminal or unix shell

`$cd your_work_directory`

`$python3 parse.py your_file_name.json`

## Examples -
`$python3 parse.py business.json`  
`$python3 parse.py review.json`    
`$python3 parse.py user.json`     
`$python3 parse.py checkin.json`
