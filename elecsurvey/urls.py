from django.conf.urls import patterns, url
from elecsurvey import views

urlpatterns=patterns('',
    url(r'^survey/',views.survey_sheet, name='survey_sheet'),
    url(r'^main_factor/',views.main_factor, name='main_factor'),
    url(r'^surveycomplete/',views.survey_complete, name='survey_complete'),
    url(r'^help/',views.help, name='help'),
)
