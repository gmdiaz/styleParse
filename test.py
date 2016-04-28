#Assignment 7: Concordance
#By Ha Le Phuong

def punctuation(text):
    '''this removes punctuations from text'''
    punc = '.,?!:;-\'"()/'
    for char in text: #run the loop thru each character in text (a string)
        if char in punc:
            text = text.replace(char,"")
    return text
    
def concordance(words,test,test):
    '''this returns a list of different words, each with its times of occurence'''
    Lconcord = []
    for word in words:
        occur = words.count(word)
        small = [occur,word] #create two-term sub-lists 
        if small not in Lconcord: #only append the sub-list that hasn't appeared in Lconcord
           Lconcord.append(small)
    return Lconcord
    
def main():
    filename = input('Filename: ')
    file = open(filename, 'r')

    text = file.read()
    text = text.lower()

    text = punctuation(text) #remove punctuations
 
    words = text.split() #turn into a list 
    n = len(words) #number of words with repetition in the list
    words.sort()

    Lconcord = concordance(words) #invoke function to produce a cleaned-up list 
    
    Lconcord.sort(reverse = True) #sort from most to least frequent
    
    print ('Concordance of', filename)
    print ('Text has', n, 'words (after cleanup & split())')
    print ('Top 50 words', '(out of', len(Lconcord), ') :') #number of distinct words
    print ('_'*30)
    for k in range(50): #run the loop through the first 50 words in Lconcord
        pair = Lconcord[k] #index each word with its times of occurence
        print ('#',k+1, pair[1],':', pair[0])

    file.close()
main()
