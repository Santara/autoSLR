import PyPDF2 
import textract
import nltk
nltk.download('punkt')
nltk.download('stopwords')
# nltk.set_proxy('172.16.2.30:8080')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import collections
import pandas as pd
import matplotlib.pyplot as plt
from string import digits
import re

#write a for-loop to open many files -- leave a comment if you'd #like to learn how

filename = 'sud1.pdf' 

#open allows you to read the file

pdfFileObj = open(filename,'rb')

#The pdfReader variable is a readable object that will be parsed

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#discerning the number of pages will allow us to parse through all #the pages

num_pages = pdfReader.numPages
count = 0
text = ""

#The while loop will read each page
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

#This if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.

if text != "":
   text = text

#If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text

else:
   text = textract.process(fileurl, method='tesseract', language='eng')

# Now we have a text variable which contains all the text derived #from our PDF file. Type print(text) to see what it contains. It #likely contains a lot of spaces, possibly junk such as '\n' etc.

# Now, we will clean our text variable, and return it as a list of keywords.
# print "Success!"
#The word_tokenize() function will break our text phrases into #individual words

tokens = word_tokenize(text)

#we'll create a new list which contains punctuation we wish to clean
punctuations = ['(',')',';',':','[',']',',']

#We initialize the stopwords variable which is a list of words like #"The", "I", "and", etc. that don't hold much value as keywords

stop_words = stopwords.words('english')

#We create a list comprehension which only returns a list of words #that are NOT IN stop_words and NOT IN punctuations.

# keywords = [word for word in tokens if not word in stop_words and  not word in string.punctuation]
keywords = [word for word in tokens if not word in stop_words and  not word in punctuations]

# useless keywords
useless_keywords = ["table", "crossref", "of", "pp", "pubmed", "see", "forinstance" "huang", "etal", "huangetal", "wu", "avalentin", "jhspangenbergenvironimpactassessmentrev", "ment", "etc", "ie", "schu", "infig", "hinterbergerf"]

# print keywords
wordcount = {}

for word in keywords:
	word = word.lower()
	word = re.sub('[^a-zA-Z0-9\n\.]', ' ', word)
	word = ''.join([i for i in word if not i.isdigit()])
	word = word.replace(".","")
	word = word.replace(",","")
	word = word.replace(":","")
	word = word.replace("\"","")
	word = word.replace("!","")
	word = word.replace("*","")
	word = word.replace(" ","")
	if word is not '' and len(word) > 1 and word not in useless_keywords:
		if word not in wordcount:
			wordcount[word] = 1
		else:
			wordcount[word] += 1

# Print most common word
n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)


lst = word_counter.most_common(n_print)
df = pd.DataFrame(lst, columns = ['Word', 'Count'])
df.plot.bar(x='Word',y='Count')