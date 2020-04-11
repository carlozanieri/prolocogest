from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Frame, Spacer, Image, Table, TableStyle, SimpleDocTemplate
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing  # , string
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.legends import Legend
from connect import Connect
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter,landscape, portrait
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from connect import Connect

class Pdf:

    def main():
        canv = Canvas("../static/pdf/report.pdf", pagesize=landscape(letter))
        styles = getSampleStyleSheet()
        style = styles["BodyText"]
        header = Paragraph("<bold><font size=18>Prima Nota Proloco San Piero</font></bold>", style)
        riga = Connect.primanota()

        data =[['DATA', 'DESCRIZIONE', 'CASSA USCITE', 'CASSA ENTRATE', 'BANCA USCITE', 'BANCA ENTRATE']]
       # data.append(['DATA', 'DESCRIZIONE', 'CASSA USCITE', 'CASSA ENTRATE', 'BANCA USCITE', 'BANCA ENTRATE'])
        for rigas in riga:
            data.append([rigas['data'], rigas['descrizione'], rigas['cassa_uscite'], rigas['cassa_entrate'], rigas['banca_uscite'], rigas['banca_entrate']])

        t = Table(data)
        t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                               ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black)]))
        data_len = len(data)

        for each in range(data_len):
            if each % 2 == 0:
                bg_color = colors.lightgrey
            else:
                bg_color = colors.whitesmoke

            t.setStyle(TableStyle([('BACKGROUND', (0, each), (-1, each), bg_color)]))

        aW = 640
        aH = 560

        w, h = header.wrap(aW, aH)
        header.drawOn(canv, 72, aH)
        aH = aH - h
        w, h = t.wrap(aW, aH)
        t.drawOn(canv, 72, aH - h)
        canv.save()

        file = "../static/pdf/report.pdf"
        print(file)
        return file