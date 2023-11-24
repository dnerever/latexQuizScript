import functions as f
import info as i

try:                                                    # Extract the quiz code from the most recently downloaded file (soon to be only PDF captured) and then copied to clipboard (Linux only) 
    recentPdf = f.findRecentFile(".pdf")                       #finds most recently modified file in current directory
    code = f.getCode(recentPdf)
    f.copyToClipboard(code, recentPdf)
finally:
    f.waitForTexFile(i.name, i.idNum)
    f.confirmChanges()