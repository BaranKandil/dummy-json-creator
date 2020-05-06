import json
import random
import string

n = input("Enter entry count: ")



f = open('rand_db.json',mode='w')
for num in range(int(n)):

    if num%10000 == 0:
        print(str(num+1) + "/" + n )

    res = ''
    for i in range(random.randrange(25, 40)):

        word = ''.join(random.choices(string.ascii_lowercase
                            , k = random.randrange(4, 12)))
        res += ' ' + word

    t = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21']

    tags = []

    r = random.randrange(6)

    for i in range(r):

        random_index = random.randrange(len(t))
        tags.append(t[random_index])
        t.pop(random_index)



    main_dict = {
    'id' : num,

    'tags': tags,

    'mainText' : res


    }


    mainText_json = json.dumps(main_dict)


    f.write(mainText_json,)
    f.write('\n')
f.close()