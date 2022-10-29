from django.http import HttpResponse, HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django import forms
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
import asyncio
from django.views import View
from portal.models.file import File
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


def example_view(request, id):
    print(request.scheme) #http or https
    print(request.META) # get meta info

    # if True:
    #     return HttpResponseNotFound('<h1>Page not found</h1>')
    # else:
    #     return HttpResponse('<h1>Page was found</h1>')
    # response = HttpResponse()
    # return response.write("<p>Here's the text of the web page.</p>")
    return HttpResponse("<p>Here's the text of the web page.</p>")

@require_http_methods(["GET", "POST"])
def my_view(request):
    # I can assume now that only GET or POST requests make it this far
    # ...
    pass

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

# Imaginary function to handle an uploaded file.
def handle_uploaded_file():
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

class AboutView(TemplateView):
    template_name = "about.html"

class FileListView(ListView):
    model = File

    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest('created_on')
        response = HttpResponse(
            # RFC 1123 date format.
            headers={'Last-Modified': last_book.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')},
        )
        return response

class AsyncView(View):
    async def get(self, request, *args, **kwargs):
        # Perform io-blocking view logic using await, sleep for example.
        await asyncio.sleep(1)
        return HttpResponse("Hello async world!")



class FormView(View):
    form_class = UploadFileForm
    initial = {'key': 'value'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
