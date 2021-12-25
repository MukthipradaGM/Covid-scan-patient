from django.shortcuts import render
from django.http.response import HttpResponse
from io import StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from html import escape
from io import BytesIO
from .models import UserDataPatientRecord
import datetime
from django.contrib.auth.models import*



# Create your views here.
# searched = 'A50E765F0AB'
# record_list = UserDataPatientRecord.objects.filter(patient_ref_id=searched).values() 
# print(record_list)

def index(request):
    return render(request,'pages/index.html')

def report(request):
    return 0


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = context_dict
    html  = template.render(context)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))





def generate_report(request):
    if request.method == "POST":
        searched = request.POST['searched']
        record_list= UserDataPatientRecord.objects.filter(patient_ref_id=searched).values() 
        #print(record_list)

    


        #record_list = Patient_record.objects.all()
        return render(request,'user_data/report.html',
        {'searched' : searched,
        'record_list' : record_list})

    else:
        return render(request,'user_data/report.html',{})

def download_report(request):
    if request.method == "POST":
        id = request.POST['ref_id']
        print('888888888888888888888888888888888888')
        print(id)
        record_list= UserDataPatientRecord.objects.filter(patient_ref_id=id).values()

        # # Rendered
        # html_string = render_to_string('user_data/download_report.html', {'record_list' : record_list})
        # html = HTML(string=html_string)
        # result = html.write_pdf()

        # # Creating http response
        # response = HttpResponse(content_type='application/pdf;')
        # response['Content-Disposition'] = 'inline; filename=Report.pdf'
        # response['Content-Transfer-Encoding'] = 'binary'
        # with tempfile.NamedTemporaryFile(delete=True) as output:
        #     output.write(result)
        #     output.flush()
        #     output = open(output.name, 'r')
        #     response.write(output.read())

        # return response


        return render_to_pdf(
            'user_data/download_report.html',
            {
                    'record_list' : record_list
            }
           
        )
        #return render(request,'user_data/download_report.html',{'record_list' : record_list}) 
    return render(request,'user_data/download_report.html')

