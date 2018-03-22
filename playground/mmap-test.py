import mmap

with open('shoppinglist.txt', 'r') as fd:
    mm = mmap.mmap(fd.fileno(), 0)
    print(mm[5:10])
    print(mm.readline())

    mm[5] = 'a'
    mm.seek(0)
    mm.close()
