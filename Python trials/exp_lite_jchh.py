import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import fileinput
import glob

#Funcion para unir listas
def join(lista) :
    union = lista[0]
    for i in range(len(lista)) :
        union = list(set(union).union(set(lista[i])))
    return union

# Toma cualquier nombre del libro con comienzo "literature_" y terminación ".txt"
archivos = glob.glob("../General literature books/training/literature_*.txt")
archivos.sort()
training = []
words_list = []
for i in range(20) :
    training.append(archivos[i])
    
for linea in fileinput.input(training, openhook=fileinput.hook_encoded("utf-8")):
    if fileinput.isfirstline():
        # Files name
        book = fileinput.filename()

        literature_1 = open(book, encoding="utf-8").read()

        print("Libro:",book)

        literature1 = nltk.word_tokenize(literature_1)

        literature1=[w.lower() for w in literature1 if w.isalpha()]

        stop_words = set(stopwords.words('english'))

        filtered_book = [w for w in literature1 if not w in stop_words]

        single_character = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'eg',
                              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z', 'σi', 'σn',
                              'α', 'β', 'βn', 'xn', 'αv', 'ν', 'ϕ', 'ba', 'ip', 'fi', 'kr', 'fr', 'ij',
                              'bd', 'nj', 'ac', 'bd', 'hk', 'gc', 'xg', 'dn', 'bi', 'mn', 'αu', 'hg',
                              'zn', 'nth', 'mmc','gcd', 'cd', 'ub', 'di', 'ad', 'ab','gh', 'στ', 'σ', 'ai',
                              'cis', 'abab', 'aabb', 'id', 'sn', 'ax', 'bx', 'αn','px', 'acr', 'bcs', 'hn',
                              'kx', 'ζ', 'η', 'θ', 'κ', 'λ', 'μ', 'ξ', 'ρ', 'τ', 'φ', 'χ', 'ψ',
                              'ω', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                              'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Ω', 'Ψ', 'Σ', 'Π',
                              'Ξ', 'Λ', 'Θ', 'Δ', 'Γ', 'aβ', 'aβj', 'βj', 'gf', 'pn', 'bp', 'zp',
                              'bch', 'http://', 'http', 'xm','µx', 'also', 'url','ª', 'solu', 'equa')

        filtered_book = [w for w in filtered_book if not w in single_character]

        filtered_book_dist = nltk.FreqDist(w.lower() for w in filtered_book)
        most_common_words = filtered_book_dist.most_common(10)
        
        words_list.append(most_common_words)
        #print(filtered_book, '\n')
        #print("\n\nLibro:", book, "Frecuentes:", most_common_words)
        print("Libro terminado: ",book)

#Separar las palabras mas frequentes sin tomar en cuenta sus distribuciones
#La lista common_words_lists contiene las 20 listas de palabras (una por cada
#libro), y cada lista contiene el numero de palabras mas frecuentes que se desee
common_words_lists = []
for i in range(20) :
    words = []
    for j in range(10) :
        words.append(words_list[i][j][0])
    
    common_words_lists.append(words)

#Encontrar las uniones entre todas las listas de palabras mas frecuentes
#entre los N libros considerados
palabras = join(common_words_lists)