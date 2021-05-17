from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
#urlpatterns:  path('blog/', include('blog.urls'))
from .views import students_form, student_submit, nav
urlpatterns = [
    path('signup/', students_form, name='signup'),
    path('student_submit/', student_submit, name='student_submit'),
    path('nav/', nav )

]