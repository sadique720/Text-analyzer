from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def remove_punc(request):
    return render(request,'remove_punc/index.html')

def analyze(request):
    # Get the text
    djtext=(request.GET.get("text",'dafault'))

    # Check checkbox values
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')

    # print(analyze)
    # print(djtext)
    # analyzed=djtext
    # Check which checkbox is on

    if removepunc =="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char

        params={'purpose':'Remove Punchuations','analyzed_text':analyzed}
        return render(request,'remove_punc/anlayze.html',params)
    elif (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request,'remove_punc/anlayze.html',params)

    elif newlineremover=='on':
        analyzed=''
        for char in djtext:
            if char!='\n' and char !='\r':
                analyzed=analyzed+char
        params = {'purpose': 'New line Remover', 'analyzed_text': analyzed}
        return render(request, 'remove_punc/anlayze.html', params)
    elif extraspaceremover=='on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra space Remover', 'analyzed_text': analyzed}
        return render(request, 'remove_punc/anlayze.html', params)

    else:
        return  HttpResponse("Error")