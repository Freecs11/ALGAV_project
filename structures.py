import numpy as np

# declare a type cle128 which is a 128-bit key represnted by two 64-bit unsigned integers
cle128 = np.dtype([('key1', np.uint64), ('key2', np.uint64)])

def main():
    # Write your algorithm code here
    
    def generate_cle128():
        return np.random.randint(0, 2**64, 2, dtype=np.uint64) 
    
    def add_cle(cle1, cle2 , out):
        return np.add(cle1, cle2, out=out , dtype=cle128)
    
    k = generate_cle128()
    print(k)
    k2 = generate_cle128()
    print(k2)
    res = np.zeros(1, dtype=cle128)
    add_cle(k, k2, res)
    print(res)
    
    return 0

if __name__ == "__main__":
    main()









