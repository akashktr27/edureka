from django.urls import path
from webapp.views import employeelist, homepage, nav, bootstrap, signin, register
from django.conf import settings
from django.conf.urls.static import static
#urlpatterns:  path('blog/', include('blog.urls'))

urlpatterns = [
    path('emp/', employeelist),
    path('home/', homepage),

    path('nav/', nav),
    path('boot/', bootstrap),
    path('signin/', signin),
    path('register/', register, name='register'),

]



