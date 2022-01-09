talk = []
with open('LINE-Viki.txt','r',encoding='utf-8-sig') as f:
    for i in f:
        talk.append(i.strip().split(' ')[1:])

#說話分類
number_allen = []
number_viki = []
pic_allen = 0
pic_viki = 0
sticker_allen = 0
sticker_viki = 0
for i in talk:
    if 'Allen' in i and '圖片' in i :
        pic_allen += 1
    elif 'Allen' in i and '貼圖' in i :
        sticker_allen += 1
    elif 'Allen' in i :
        number_allen.append(i[1:])
    elif 'Viki' in i and '圖片' in i :
        pic_viki += 1
    elif 'Viki' in i and '貼圖' in i :
        sticker_viki += 1
    elif 'Viki' in i :
        number_viki.append(i[1:])

#計算字串長度
Allen = ''
viki = ''
for i in number_allen:
    Allen += i[0]
for i in number_viki:
    viki += i[0]

a= f'Allen總共講了{len(Allen)}個字，傳了{pic_allen}圖片,傳了{sticker_allen}貼圖'
b= f'Viki總共講了{len(viki)}個字，傳了{pic_viki}圖片,傳了{sticker_viki}貼圖'

people =[a,b]
with open('output_2.txt','w',encoding='utf-8') as f:
    for i in people:
        f.write(i + '\n')