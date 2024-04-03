from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    encoding = 'UTF-8'
    html_encoded = html.encode(encoding)
    pdf = pisa.pisaDocument(BytesIO(html_encoded), result, encoding=encoding)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None