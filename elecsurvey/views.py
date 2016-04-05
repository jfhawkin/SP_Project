from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from elecsurvey.models import Factor
from elecsurvey.forms import FactorForm
from django.db import transaction, connections
import random
import ast
from datetime import datetime
 
def survey_sheet(request):
    context=RequestContext(request)
    survey_title = settings.SURVEY_TITLE
    resultDict=[]
    resp_num = int(request.POST.get('respNum',1))

    
    c = connections['default'].cursor()
    c.execute("SELECT * FROM public.option_list")
    series = c.fetchall()
    
    alt_ids = random.sample(range(len(series)), 2)
    
    c.execute("SELECT * FROM public.alternative_list WHERE id IN {0}".format(tuple(alt_ids)))
    alt_list = c.fetchall()
    part_id = datetime.now()
    alt_chosen = request.POST.get('alt',1)
	
    if request.method=='POST':

        if(resp_num<4):
            for i in range(0,2):
                query=""
                query += "INSERT INTO public.resp_list (alt_id,resp_num,alt_chosen, participant_id) VALUES({0},{1},{2},'{3}');".format(alt_list[i][0],resp_num,alt_chosen,part_id)
            c.execute(query)
            resp_num = resp_num+1
            return render_to_response ('elecsurvey/survey_form.html', {'respNum':resp_num, 'altList':alt_list, 'altIds':alt_ids, 'surveyTitle':survey_title, 'partId': part_id}, context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/electricity-preferences/main_factor/')
    return render_to_response ('elecsurvey/survey_form.html', {'respNum':resp_num,'altList':alt_list, 'altIds':alt_ids,'surveyTitle':survey_title, 'partId': part_id}, context_instance=RequestContext(request))

def main_factor(request):
    context=RequestContext(request)
    part_id = datetime.now()
	
    survey_title = settings.SURVEY_TITLE
    if request.method=='POST':
        form=FactorForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return render_to_response('elecsurvey/survey_complete.html',{'form':form, 'partId':part_id},context)
        else:
            print form.errors
    else:
        form=FactorForm()
    return render_to_response('elecsurvey/main_factor.html',{'form':form,'surveyTitle':survey_title},context)
    
    
def survey_complete(request):
    return render_to_response ('elecsurvey/survey_complete.html', context_instance=RequestContext(request))
    
def help(request):
    return render_to_response ('elecsurvey/help.html', context_instance=RequestContext(request))
    