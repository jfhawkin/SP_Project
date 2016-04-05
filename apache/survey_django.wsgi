import os, sys

sys.path.append('C:/SPWebDeveloper') #CHANGE ME AS APPROPRIATE. The parent folder of the PROJECT PATH 
os.environ['DJANGO_SETTINGS_MODULE'] = 'spGenerator.settings' #CHANGE ME AS APPROPRIATE, e.g. 'web_output.mapit_settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


