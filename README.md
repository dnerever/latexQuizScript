# latexQuizScript
A Python and a Bash script that I created for use during my timed Algorithms Quizzes to save time opening, copying and writing to latex and pdf documents.

## Requirements

- Unix based OS (Ubuntu, Fedora, etc)
- Python3
- xclip


## Instructions

- Save autoCompleteInfo, codeExtractorAndInfoFiller.py, and info.py in the directory quizzes will be saved to.
- Dowload the first Quiz##.pdf
- Immediately run the script: 
```
python3 codeExtractorAndInfoFiller.py
```
- Now the script has searched the pdf file to find the quiz code and copied it to the user's clipboard.
- Paste the copied code in Canvas to unlock the Quiz##.tex file.
- Download the Quiz##.tex file.
- When the Quiz##.tex is downloaded it will search and replace 'Student Name', 'Student ID' and sign the plagramism agreement using all of your info stored in 'info.py'.