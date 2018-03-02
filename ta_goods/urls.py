
from django.urls import re_path,path

from ta_goods.views import *

urlpatterns = [

        re_path('^list_(\d+)_(\d+)_(\d+)$' , typelist),
        re_path('^(\d+)$',detail),
        re_path('^$', index, name='index')
]
