# Place this in the directory of the pdf files 
for file in *.pdf; do pdf2txt.py -o ../txt_files/$file.txt $file; done
