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
# import matplotlib.pyplot as plt
from string import digits
import re
from rake_nltk import Rake 
import pprint

#write a for-loop to open many files -- leave a comment if you'd #like to learn how

filename = 'AlphaGoNaturePaper.pdf' 

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

# print text\
# testtext = "In general, text extraction from a PDF file (particularly when you want to include the formatting / spacing / layout of the text), is considered to be a task that may not always work 100% accurately. I got to know this from a support tech person at a company that produces a popular library (xpdf) for extracting text from PDFs, some time ago when I was working on a project in that area. At that time, I had explored several libraries for extracting PDF from text, including xpdf and some others. There are clear technical reasons for why they cannot always give perfect results (though they do in many cases); those reasons are to do with the nature of the PDF format and how PDF is generated. When you extract the text from some PDFs, the layout and spacing may not be preserved, even if you use an option to the library like keep_format=True or the equivalent."
# Start RAKE
pdfminer_text = open("AlphaGo.txt")
r = Rake()
pp = pprint.PrettyPrinter()
r.extract_keywords_from_text(pdfminer_text)
pp.pprint(r.get_ranked_phrases_with_scores()[:20])