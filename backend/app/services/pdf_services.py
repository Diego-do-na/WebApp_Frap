from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generar_pdf_reporte(data):
    doc = SimpleDocTemplate("reporte.pdf")
    styles = getSampleStyleSheet()
    elementos = []

    r = data["reporte"]
    p = data["paciente"]

    encabezado = f"""
    <b>Reporte #{r.id_Reporte}</b><br/>
    Paciente: {p.nombre}<br/>
    Edad: {p.edad}<br/>
    Género: {p.genero}<br/><br/>
    <b>Observaciones:</b><br/>
    {r.observaciones}<br/><br/>
    <b>Recomendaciones:</b><br/>
    {r.recomendaciones}
    """

    elementos.append(Paragraph(encabezado, styles["Normal"]))
    elementos.append(Spacer(1, 12))

    doc.build(elementos)

    return "reporte.pdf"