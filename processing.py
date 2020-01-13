def do_generate(message):
    import re
    import numpy as np
    import matplotlib.pyplot as plt
    source_text = message
    input = source_text.lower()
    input = re.sub(r'\W+', '', input)

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters = letters+"0123456789/"
    def rank(x, d = dict((letr,n%26+1) for n,letr in enumerate(letters[0:62]))):
        return d[x]

    list = sorted(set((str(rank(letter))[-1] for letter in input)))
    list_np = np.array(list,dtype='int')

    #define grid
    a=np.ones((9,9))
    b=np.full((9,9), False)

    for x in range (1,10):
        for y in range (1,10):
            a[x-1,y-1] = int(str(x*y)[-1])
            b[x-1,y-1] = np.any(list_np[:] == a[x-1,y-1])

    brev = np.fliplr(b)
    bcombo = np.hstack((b,brev))
    bvert = np.flipud(bcombo)
    bcombo = np.vstack((bcombo,bvert))
    fourup = np.hstack((bcombo,bcombo))
    fourup = np.vstack((fourup,fourup))
    np.savetxt('plot.csv',bcombo,fmt='%s',delimiter=',')
#    fig = plt.figure()
#    fig.add_subplot(2,2,1)
#    plt.imshow(bcombo,cmap=plt.cm.Blues,interpolation='nearest')
#    fig.add_subplot(2,2,2)
#    plt.imshow(bcombo,cmap=plt.cm.Blues_r,interpolation='nearest')
#    fig.add_subplot(2,2,3)
#    plt.imshow(fourup,cmap=plt.cm.Blues,interpolation='nearest')
#    fig.add_subplot(2,2,4)
#    plt.imshow(fourup,cmap=plt.cm.Blues_r,interpolation='nearest')
#    fig.savefig(input+'_plot.png')

    fig1 = plt.figure()
    fig1.add_subplot(1,2,1)
    plt.imshow(bcombo,cmap=plt.cm.Blues,interpolation='nearest',extent=[18,1,1,18])
    fig1.add_subplot(1,2,2)
    plt.imshow(bcombo,cmap=plt.cm.Blues_r,interpolation='nearest',extent=[18,1,1,18])
    fig1.savefig("mymessage/assets/images/"+input+'_plot.png',dpi=50)

    fig2 = plt.figure()
    fig2.add_subplot(1,2,1)
    plt.imshow(fourup,cmap=plt.cm.Blues,interpolation='nearest',extent=[36,1,1,36])
    fig2.add_subplot(1,2,2)
    plt.imshow(fourup,cmap=plt.cm.Blues_r,interpolation='nearest',extent=[36,1,1,36])
    plt.show()
    fig2.savefig("mymessage/assets/images/"+input+'_plot4x4.png',dpi=75)

    return input