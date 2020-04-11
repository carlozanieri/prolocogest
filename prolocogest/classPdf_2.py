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
class Pdf:

    def main(self):

        subject1 = 'carlo zanieri'
        subject2 = 'bruna baldini'
        results1 = [30, 33, 42, 46, 6666]
        results2 = [34, 47, 44, 31, 6666]


# take the data and make ready for paragraph
        def dataToParagraph(name, data):
            p = '<strong>Nome Soggetto: </strong>' + name + '<br/>' + '<strong>Data: </strong>  ('
            for i in range(len(data)):
                p += str(data[i])
                if i != len(data) - 1:
                    p += ', '
                else:
                    p += ')'
            return p


# take the data and convert to list of strings ready for table
        def dataToTable(name, data):
            data = [str(x) for x in data]
            data.insert(0, name)
            return data


# create the table for our document
        def myTable(tabledata):
            # first define column and row size
            colwidths = (70, 50, 50, 50, 50, 50)
            rowheights = (25, 20, 20)

            t = Table(tabledata, colwidths, rowheights)

            GRID_STYLE = TableStyle(
            [('GRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('ALIGN', (1, 1), (-1, -1), 'RIGHT')]
    )

            t.setStyle(GRID_STYLE)
            return t


# create a bar chart and specify positions, sizes, and colors
        def myBarChart(data):
            drawing = Drawing(400, 200)

            bc = VerticalBarChart()
            bc.x = 50
            bc.y = 50
            bc.height = 125
            bc.width = 300
            bc.data = data
            bc.barWidth = .3 * inch
            bc.groupSpacing = .2 * inch

            bc.strokeColor = colors.black

            bc.valueAxis.valueMin = 0
            bc.valueAxis.valueMax = 100
            bc.valueAxis.valueStep = 10

            bc.categoryAxis.labels.boxAnchor = 'ne'
            bc.categoryAxis.labels.dx = 8
            bc.categoryAxis.labels.dy = -2

            catNames = ('Trial1 Trial2 Trial3 Trial4 Trial5').split()
            bc.categoryAxis.categoryNames = catNames

            bc.bars[0].fillColor = colors.red
            bc.bars[1].fillColor = colors.lightblue

            drawing.add(bc)

            return drawing


# add a legend for the bar chart
        def myBarLegend(drawing, name1, name2):
            "Add sample swatches to a diagram."
            d = drawing or Drawing(400, 200)

            swatches = Legend()
            swatches.alignment = 'right'
            swatches.x = 80
            swatches.y = 160
            swatches.deltax = 60
            swatches.dxTextSpace = 10
            swatches.columnMaximum = 4
            items = [(colors.red, name1), (colors.lightblue, name2)]
            swatches.colorNamePairs = items

            d.add(swatches, 'legend')
            return d


########   Now lets put everything together.   ########

# create a list and add the elements of our document (image, paragraphs, table, chart) to it
        story = []

# define the style for our paragraph text
        styles = getSampleStyleSheet()
        styleN = styles['Normal']
        styleH = styles['Heading1']
# First add the Vizard Logo
        imagePath ='static/img/ultimo.JPG'
        im = Image(imagePath, width=1 * inch, height=1 * inch)
        im.hAlign = 'CENTER'
        story.append(im)

# add the title
        story.append(Paragraph("<strong>Risultati sperimentali</strong>", styleN))
        story.append(Spacer(1, .25 * inch))

# convert data to paragraph form and then add paragraphs
        story.append(Paragraph(dataToParagraph(subject1, results1), styleN))
        story.append(Spacer(1, .25 * inch))
        story.append(Paragraph(dataToParagraph(subject2, results2), styleN))
        story.append(Spacer(1, .5 * inch))

# add our table - first prepare data and then pass this to myTable function
        riga = Connect.pdf('8001120835888')
        for rigas in riga:
            tabledata = (
                ('', str(rigas['descrizione'])),
                dataToTable(str(rigas['cassa_uscite']),str(rigas['banca_uscite'])))
            story.append(myTable(tabledata))
            story.append(Spacer(1, .5 * inch))
# add our barchart and legend
            drawing = myBarChart([results1, results2])
            drawing = myBarLegend(drawing, subject1, subject2)
            drawing.hAlign = 'CENTER'
            story.append(drawing)

     #   riga = Connect.pdf('8001120835888')
            x = 0
            y = 500
       # for rigas in riga :
            nome = str(rigas['data']) + str(rigas['descrizione'])
            y += 20
            story.append(Paragraph(nome, styleH))


# build our document with the list of flowables we put together
        file = "static/pdf/report.pdf"
        doc = SimpleDocTemplate(file, pagesize=letter, topMargin=0)
        doc.build(story)

        return file