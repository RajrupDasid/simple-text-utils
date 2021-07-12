from django.http import HttpResponse
from django.shortcuts import render
#project module views.py
def index(request):
    name='Manjaro'
    type='Linux'
    context={
        'name':name,
        'type':type,
    }  
    return render (request,'index.html',context)

def about(request):
    return HttpResponse("This is about page")
def analyze(request):
    new=request.POST.get('text','default')
    rp=request.POST.get('removepunc','off')
    fc=request.POST.get('fullcaps','off')
    lc=request.POST.get('lowercaps','off')
    nlr=request.POST.get('nlr','off')
    sr=request.POST.get('sr','off')
    analyzed=""
    punctuations=''' _ - + = !#@$!^$3#&# * # @( ) @ * ) @ ! * ^ $ ^ $ % @{ } [ ] " " ' ' : ; . / ? > ? < ,  '''
    if rp=='on':
        for char in new:
            if char not in punctuations:
                analyzed= analyzed+char
        context={
        "punctuations":punctuations,
        "analyzed":analyzed,
        'new':new,
        }
        new=analyzed
        #return render(request,'analyze.html',context)
    if(fc=='on'):
        analyzed=""
        for char in new:
            analyzed+=char.upper()
        context={
            "punctuations":punctuations,
            "analyzed":analyzed,
            "new":new,
            "fc":fc,
        }
        new=analyzed
        #return render(request,'analyze.html',context)
    if(lc=='on'):
        analyzed=""
        for char in new:
            analyzed+=char.lower()
        context={
            "punctuations":punctuations,
            "analyzed":analyzed,
            "new":new,
            "fc":fc,
            "lc":lc,
        }
        new=analyzed
        #return render(request,"analyze.html",context)
    if(nlr=="on"):
        analyzed=""
        for char in new:
            if char !="\n" and  char!="\r":
                analyzed+=char
        context={
            "punctuations":punctuations,
            "analyzed":analyzed,
            "new":new,
            "fc":fc,
            "lc":lc,
            "nlr":nlr,
        }
        new=analyzed
        #return render(request,"analyze.html",context)
    if(sr=="on"):
        analyzed=""
        for index,char in enumerate(new):
            if new[index] ==" " and new[index+1] ==" ":
                pass
            else:
                pass
        context={
            "punctuations":punctuations,
            "analyzed":analyzed,
            "new":new,
            "fc":fc,
            "lc":lc,
            "nlr":nlr,
            'sr':sr,
        }
        new=analyzed
    if(rp!="on" or fc!="on" and nlr!="on" and sr!="on" and lc!="on"):
        return HttpResponse("error")
    return render(request,"analyze.html",context)  
    