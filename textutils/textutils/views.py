# i can create this file for myself
from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'index2.html')
def analyze(request):
    djtext=request.GET.get('text','default')
    removepun=request.GET.get('removepun','off')
    capatalize=request.GET.get('capatalize','off')


    if removepun=="on":
        analyise=""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyise =analyise+char
        djtext =analyise

    if (capatalize == "on"):
        capz=''
        for i in djtext:
            capz=capz + i.upper()
        djtext = capz
    data = {"data1": "Your text Analayze The Desire Result Output", "data2": djtext}
    return render(request, 'analyze2.html', data)



