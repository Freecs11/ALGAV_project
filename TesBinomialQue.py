from BinomialQueue import *

if __name__ == '__main__':
    binomialNode = BinomialNode(5)
    print (binomialNode)
    binomialHeap = BinomialHeap()
    binomialHeap2 = BinomialHeap()
    print (binomialHeap)
    binomialHeap._ajout_iteratif([1,2,3,4])
    binomialHeap2._ajout_iteratif([5,6,7,8])
    
    print (binomialHeap)
    print (binomialHeap.degre())
    binomialHeap.union2Tid(binomialHeap2)
    print (binomialHeap)
    print ('----------ggg------------------------------------------------------')
    print (binomialHeap.decapite())
    print ('--------rr--------------------------------------------------------')
    binomialQueue = binomialHeap.decapite()
    print (binomialQueue)
    print ('------------mindeg----------------------------------------------------')
    print (binomialQueue.minDeg())
    print ('--------------rest--------------------------------------------------')
    print (binomialQueue.reste())
    print ('---------ajoutMin------')
    minBinomialHeap = BinomialHeap()
    minBinomialHeap._ajout_iteratif([8])
    print (minBinomialHeap)
    print (binomialQueue.ajoutMin(minBinomialHeap))
    print ('----------union------------')
    newBinomialHeap1 = BinomialHeap()
    newBinomialHeap1._ajout_iteratif([1])
    
    newBinomialHeap2 = BinomialHeap()
    newBinomialHeap2._ajout_iteratif([2,3])
    
    newBinomialHeap3 = BinomialHeap()
    newBinomialHeap3._ajout_iteratif([4,5,6,7])
    
    newBinomialHeap4 = BinomialHeap()
    newBinomialHeap4._ajout_iteratif([8,9,10,11])
    
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
    print ("U1 -> \n",res)
    
    res = res.union(newBinomialQueue4)
    print ("U1 -> \n",res)