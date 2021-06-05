
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    print(request.GET.get('a'))
    print(type(request))
    html = '''
            <!DOCTYPE html>
        <html>
        <body>

        <h1>This is heading 1</h1>
        <h2>This is heading 2</h2>
        <h3>This is heading 3</h3>
        <h4>This is heading 4</h4>
        <h5>This is heading 5</h5>
        <h6>This is heading 6</h6>

        </body>
        </html>
        '''

    return HttpResponse(html)

def sum(request):
   
    html = '''
            <!DOCTYPE html>
        <html>
        <body>

  SUM

        </body>
        </html>
        '''

    return HttpResponse(html)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('sum',sum)
]
