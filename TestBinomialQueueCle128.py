

from BinomialQueue import *


if __name__ == '__main__':
    binomialNode = BinomialNode(st.generate_key())
    print (binomialNode)
    binomialHeap = BinomialHeap()
    binomialHeap2 = BinomialHeap()
    print (binomialHeap)
    
    binomialHeap._ajout_iteratif([st.generate_key() for _ in range(4)])
    binomialHeap2._ajout_iteratif([st.generate_key() for _ in range(4)])
    
    print (binomialHeap)
    print (binomialHeap.degre())
    binomialHeap.union2Tid(binomialHeap2)
    print (binomialHeap)
    print ('-----------------decapite-----------------------------------------------')
    binomialQueue = binomialHeap.decapite()
    print (binomialQueue)
    print ('------------mindeg----------------------------------------------------')
    print (binomialQueue.minDeg())
    print ('--------------rest--------------------------------------------------')
    print (binomialQueue.reste())
    print ('---------ajoutMin------')
    minBinomialHeap = BinomialHeap()
    minBinomialHeap._ajout_iteratif([st.generate_key()])
    print (minBinomialHeap)
    print (binomialQueue.ajoutMin(minBinomialHeap))
    print ('----------union------------')
    newBinomialHeap1 = BinomialHeap()
    newBinomialHeap1._ajout_iteratif([st.generate_key()])
    
    newBinomialHeap2 = BinomialHeap()
    newBinomialHeap2._ajout_iteratif([st.generate_key() for _ in range(2)])
    
    newBinomialHeap3 = BinomialHeap()
    newBinomialHeap3._ajout_iteratif([st.generate_key() for _ in range(4)])
    
    newBinomialHeap4 = BinomialHeap()
    newBinomialHeap4._ajout_iteratif([st.generate_key() for _ in range(4)])
    
    newBinomialQueue1 = newBinomialHeap1.file()
    newBinomialQueue2 = newBinomialHeap2.file()
    newBinomialQueue3 = newBinomialHeap3.file()
    newBinomialQueue4 = newBinomialHeap4.file()
    
    print (newBinomialQueue1)
    print (newBinomialQueue2)
    print (newBinomialQueue3)
    print (newBinomialQueue4)
    
    res = newBinomialQueue1.union(newBinomialQueue2)
    print ("U1 <-> \n",res)
    
    res = res.union(newBinomialQueue3)
    print ("U2 -> \n",res)
    
    res = newBinomialQueue3.union(newBinomialQueue4)
    print ("U3 -> \n",res)
    
    print("----------------------supp----------------------------")
    # print (res.minimum)
    print (res)
    res.supprMin()
    print (res)
    print (res.minimum)
    print ('---------------------ajout--------------------------------------')
    newBinomialHeap5 = BinomialHeap()
    newBinomialQueue5 = BinomialQueue()
    newBinomialHeap5._ajout_iteratif([st.generate_key() for _ in range(2)])
    newBinomialQueue5.ajout(newBinomialHeap5)
    print (newBinomialQueue5)
    print('--------------------------------')
    print (res)
    res.ajout(newBinomialHeap5)
    # res.ajout(newBinomialHeap5)
    print (res)
    
    print ('---------------------construction--------------------------------------')
    newBinomialQueue = BinomialQueue()
    liste = [st.generate_key() for _ in range(4)]
    print (liste)
    print('--')
    newBinomialQueue.construction(liste)
    
    print (newBinomialQueue)
    
