__author__ = 'dmicomrt'
import json
from pprint import pprint


foo = [{"id":1, "od":2},{"id":3, "od":4}]
fo = {"id":5, "od":6}
foo.append(fo)
foo[0]["id"] = 5


with open('data.txt', 'w') as outfile:
  json.dump(foo, outfile)


json_data=open('data.txt')
data = json.load(json_data)

print data
print data[0]["id"]