##from classPdf import Pdf
import webbrowser
from primanotaTabdf import Pdf
#file="static/pdf/risultati.pdf"
file2 = Pdf.main()
# print(file2)

dom = "prolocogest.it/"

#### webbrowser.open("http://" + dom + file2 + "/", autoraise=Pdf)
webbrowser.open("http://" + dom + file2 + "/", autoraise=Pdf)