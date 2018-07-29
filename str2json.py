import json
line='工具:碎石机01;成品:石材 1;原料:岩石 11,'


def convert(str):
    str=str.replace('工具','tool')
    str=str.replace('成品','product')
    str=str.replace('原料','ingredients')

    data=str.split(';')

    D={}
    for item in data:
        item=item.split(':') 
        
        D[item[0]]=item[1]
        
    ings=D['ingredients']
    D['ingredients']=[]
    for ing in ings.split(','):
        if not ing:
            continue
        ing=ing.split()
        D['ingredients'].append({'name':ing[0],'count':int(ing[1])})

    JSON=json.dumps(D)
    return JSON

print(json.loads(convert(line)))
