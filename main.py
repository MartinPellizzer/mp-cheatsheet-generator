import jinja2
import pdfkit
from datetime import datetime

demo = datetime.today().strftime('%d %b, %Y')

value = '7 easy charts'

context = {
    'value': value,
}

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

template = template_env.get_template('template.html')
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
pdfkit.from_string(
    output_text, 
    'output.pdf', 
    configuration=config, 
    css='style.css',
    options={"enable-local-file-access": ""},
)
