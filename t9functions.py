#Returns clean text, i.e punctuation, \n,\t replaced by single space

def readTextFile(file):
        import string
        import codecs
        import re

        fl = codecs.open( file, "r", "utf-8" )
        txt = fl.read() # Returns a Unicode string from the UTF-8 bytes in the file
    
        fl.close()

        txt = txt.lower() #convert to lower case
        txt = txt.strip('\n')
        txt = re.sub('[^A-Za-z]+', ' ', txt)
        txt = re.sub('\s{2,}', ' ', txt)
        return txt

#######################################################################


#get transition probability into a 26x26 matrix - N

def getNMatrix(text):
        import numpy
        N = numpy.zeros((26, 26))
        sp = 0;
        for i, c in enumerate(text[:-1]) :
                cval = ord(c)
                cvalp = ord(text[i + 1])
                if (cval >=97) & (cval <= 122) & (cvalp >=97) & (cvalp <= 122) :
                        m = cval - 97;
                        n = cvalp - 97;
                        N[m,n] = N[m,n] + 1
                elif (cval ==32) | (cvalp == 32) :
                        sp = sp + 1                       
                else:
                        print(c)
                        print("error")
        return N, sp
                
        
        






