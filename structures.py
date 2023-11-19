import numpy as np

# un type cle128 qui est un type numpy composé de deux uint64
cle128 = np.dtype([('key1', np.uint64), ('key2', np.uint64)])

# juste pour tester
def generate_key():
    generated =  np.random.randint(0, 2**64, 2, dtype=np.uint64)
    return np.array(tuple(generated), dtype=cle128)

def inf(cle1 , cle2):
    return np.less(cle1['key1'], cle2['key1']) | (np.equal(cle1['key1'], cle2['key1']) & np.less(cle1['key2'], cle2['key2']))

def eg(cle1, cle2):
    return np.equal(cle1['key1'], cle2['key1']) & np.equal(cle1['key2'], cle2['key2'])


def treat_from_file(filename):
    # Init d'une liste vide
    cle128_list = []
    
    # Ouverture du fichier en mode lecture
    with open(filename, 'r') as f:
        lines = f.readlines() # Récupération des lignes du fichier
        # on va dans chaque ligne
        for line in lines:
            # Extrait les 32 premiers caractères de la ligne comme key1 après avoir enlevé le 0x d'où le 2:18
            key1_hex = line[2:18]
            key1 = np.uint64(int(key1_hex, 16)) # Convertit la clé hexa en int , uint64 prend en paramètre un int
            key2_hex = line[18:34]
            key2 = np.uint64(int(key2_hex, 16))

            # on crée la clé à partir de key1 et key2 et on l'ajoute à la liste
            cle = np.array((key1, key2), dtype=cle128)
            cle128_list.append(cle)

    for cle in cle128_list:
        print(cle)
        
    return cle128_list


if __name__ == "__main__":
    cl = generate_key()
    print(cl)
    c2 = generate_key()
    print(c2)
    print(inf(cl, c2))
    print(eg(cl, c2))
    
    treat_from_file("cles_alea/jeu_1_nb_cles_1000.txt")
    treat_from_file("cles_alea/jeu_2_nb_cles_1000.txt")









