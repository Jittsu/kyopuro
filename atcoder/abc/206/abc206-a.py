TEIKA = 206

nedan =  int(input())
zeikomi = nedan*1.08
zeikomi = int(zeikomi)
if zeikomi < 206:
    print('Yay!')
elif zeikomi == 206:
    print('so-so')
else:
    print(':(')