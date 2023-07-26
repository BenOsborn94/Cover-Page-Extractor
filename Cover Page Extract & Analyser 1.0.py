#Import required modules

import PyPDF4

import os
import time
import datetime

import progress
from progress.bar import Bar


#Introduce Program

print()
print('This program extracts the first page from multiple PDFs and merges those pages into one PDF document.')
print()
print('______________________________________________')
print()
print('Enter the file path for the folder containing documents requiring analysis:')


#Create working folder filepath, i.e. the filepath containing the PDFs you want to extract the first page from

path = input()
path = path.replace(os.sep, '/')

pathend = path.endswith('/')
if pathend == False:
    path = path + '/'
else:
    path = path

os.chdir(path)


#Create filename for exported pdf

AnalysisDate = datetime.datetime.now()
AnalysisDateFormatted = AnalysisDate.strftime("%Y-%m-%d %H%M%S")

FileName = str('First Page Extract ' + AnalysisDateFormatted +'.pdf')

#Enter the desired filepath for the exported file

print('Enter the filepath you want to export the file to:')
ExportFilePath = input()
ExportFilePath = ExportFilePath.replace(os.sep, '/')

ExportFilePathend = ExportFilePath.endswith('/')
if ExportFilePathend == False:
    ExportFilePath = ExportFilePath + '/'
else:
    ExportFilePath = ExportFilePath

#Iterate first pages out of pdfs in the filepath and export -> https://pythonprogramming.altervista.org/merge-only-first-page-of-many-pdf-files-with-python/?doing_wp_cron=1667922550.9954869747161865234375

x = [a for a in os.listdir() if a.endswith(".pdf")]         # list of pdf
merger = PyPDF4.PdfFileMerger()                             # merger object
with Bar('Processing...', max=len(x)) as bar:
    for pdf in x:                                           # add all file in the list to the merger object
        merger.append(open(pdf, 'rb'), pages=(0,1), import_bookmarks=False)
        time.sleep(0.02)
        bar.next()
    with open(ExportFilePath + FileName, "wb") as fout:                      # writes the merger object in the new file
        merger.write(fout)


print('1st Page Extraction Complete')
time.sleep(2)
