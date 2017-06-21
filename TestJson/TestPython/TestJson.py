import json

d = {}
d['key'] = 'value'

json.dumps(d)

with open('test.json','w') as f:
    json.dump(d,f)

    d['key2'] = {'key3':'value3'}
    json.dump(d,f)

with open('test.json','r') as f:
    d2 = {}
    d2 = json.load(f) # これはエラーになる．ブレイスが２組並んでいるから．
    d2.dump2()





