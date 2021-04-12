import yaml
import random

with open(r'./config.yml') as file:
    yamlfile = yaml.load(file, Loader=yaml.FullLoader)
    active = 0
    passive = 0
    mode = ['active', 'passive']
    index = 0
    length = 0
    var = 0
    act_list = []
    p_list = []
    choosers = [5, 10, 15, 20, 25, 30, 35, 40, 45]
    choosers_r = [1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600]
    shifts = yamlfile['shifts']
    for i in shifts:
        if i['state'] == 'active':
            active += i['duration']['base']
        elif i['state'] == 'dormant':
            passive += i['duration']['base']
    while active > 0 or passive > 0:
            dur = random.choice(choosers)*60
            dur_pas = random.choice(choosers)*60
            #print(dur)
            if active-dur < 0:
                act_list.append({'state':'active', 'duration':{'base': active, 'variation':random.choice(choosers_r)}})
                act_list.append({'state':'dormant', 'duration':{'base': passive, 'variation':random.choice(choosers_r)}})
                break
            elif passive-dur < 0:
                act_list.append({'state':'active', 'duration':{'base': active, 'variation':random.choice(choosers_r)}})
                act_list.append({'state':'dormant', 'duration':{'base': passive, 'variation':random.choice(choosers_r)}})
                break
            else:
                active -= dur
            #    print(active)
                passive -= dur_pas
            #    print(passive)
                act_list.append({'state':'active', 'duration':{'base': dur, 'variation':random.choice(choosers_r)}})
                act_list.append({'state':'dormant', 'duration':{'base': dur_pas, 'variation':random.choice(choosers_r)}})
yamlfile['shifts'] = act_list
with open(r'config.yml', 'w') as file:
    documents = yaml.dump(yamlfile, file)
