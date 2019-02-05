The solution for problem 1 is in file: HW01_Problem1.pdf  
The submission included all of the provided file, HW01_Problem1.pdf, README.md  
and docIndex.py (locate in data directory).  

**My program consist of four classes:**  
**DocumentIndex** -- This class has data member that is document index.The data  
member is a dictionary. Dictionary key is the document ID, dictionary value is  
number of terms in document.  

**PostingIndex** -- This class going to set up the revert index. I get document  
from file, tokenize it, remove stop word, apply stemming (I use the stem() function  
from nltk package), then save word to a dictionary(key = word, value = number of document  
contains word, list of postings)  

**ComputeWeight** -- This class going to comput TF, IDF, TF-IDF  

**test** -- This class use to test the program. It asks user to enter query until  
the user type QUIT  

**INSTRUCTIONS TO RUN PROGRAM**  
File docIndex.py contains all of the code. It locates in the data directory.  
To run the code, go to data directory, then use command: python3 docIndex.py  
I use python version 3.6.5. In order to run my code, you may have to install  
nltk package.