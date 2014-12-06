def readTextFile(file):
    #Returns clean text, i.e punctuation, \n,\t replaced by single space
    import string
    import codecs
    import re

    fl = codecs.open( file, "r", "utf-8" )
    txt = fl.read() # Returns a Unicode string from the UTF-8 bytes in the file
    
    fl.close()

    txt = txt.lower() #convert to lower case
    txt = txt.strip('\n')
    txt = re.sub('[^A-Za-z0-9]+', ' ', txt)
    txt = re.sub('\s{2,}', ' ', txt)
    return txt

#######################################################################









