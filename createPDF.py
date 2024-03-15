from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def create_pdf(file_name, text):
    # PDF erstellen
    c = canvas.Canvas(file_name, pagesize=A4)

    # Hinzufügen von Text
    c.drawString(100, 750, "Hier folgt ein kurzer Text:")
    c.drawString(100, 730, text)

    # Speichern und Schließen der PDF
    c.save()

# Testinhalt
text = "Hallo, ich ist ein kleiner Text. hier steht nicht viel, ich wollte nur etwas stehen haben."

# Name der PDF
file_name = "files/example.pdf"

# Erstellen der PDF
create_pdf(file_name, text)
