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
    new=request.GET.get('text','default')
    rp=request.GET.get('removepunc','off')
    fc=request.GET.get('fullcaps','off')
    lc=request.GET.get('lowercaps','off')
    nlr=request.GET.get('nlr','off')
    sr=request.GET.get('sr','off')
    analyzed=""
    punctuations=''' _ - + = !#@$!^$3#&# * # @( ) @ * ) @ ! * ^ $ ^ $ % @{ } [ ] " " ' ' : ; . / ? > ? < ,  '''
    if rp=='on':
        for char in new:
            if char not in punctuations:
                analyzed= analyzed+char
    elif(fc=='on'):
        analyzed=""
        for char in new:
            analyzed+=char.upper()
        context={
            "punctuations":punctuations,
            "analyzed":analyzed,
            "new":new,
            "fc":fc,
        }
        return render(request,'analyze.html',context)
    elif(lc=='on'):
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
        return render(request,"analyze.html",context)
    elif(nlr=="on"):
        analyzed=""
        for char in new:
            if char !="\n":
                analyzed+=char
        context={
            "punctuations":punctuations,
            "analyzed":analyzed,
            "new":new,
            "fc":fc,
            "lc":lc,
            "nlr":nlr,
        }

        return render(request,"analyze.html",context)
    elif(sr=="on"):
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

        return render(request,"analyze.html",context)        
    else :
        return HttpResponse ("Error")
    context={
        "punctuations":punctuations,
        "analyzed":analyzed,
        'new':new,
    }
    return render(request,'analyze.html',context)