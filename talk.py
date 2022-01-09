talk = []
with open('input.txt','r',encoding='utf-8') as f:
    for line in f:
        talk.append(line.strip())
talk[0]=talk[0].replace('\ufeff','')

message = ''
count = 0
for i in talk:
    if 'Tom' in i or 'Allen' in i :
        if 'Tom' in i :
            count = 2
        elif 'Allen' in i:
            count = 1
        continue
    #print(count)
    elif count == 1:
        message = message +'Allen:'+ i + '\n'
    elif count == 2:
        message = message +'Tom:'+ i + '\n'
with open('output.txt','w',encoding='utf-8') as f:
    f.write(message)


