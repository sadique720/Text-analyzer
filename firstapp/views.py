from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Github <a href='https://github.com/sadique720'>github</a><br>"
                        "flipkart <a href='https://www.flipkart.com/'>flipkart</a><br>"
                        "amazon <a href='https://www.amazon.in/'>amazon</a><br>"
                        "snapdeal <a href='https://www.snapdeal.com/'>snapdeal</a><br> ")

# Create your views here
def variable(request):
    # get the text
    print(request.GET.get('text','default'))
    varibale={'name':'sadique','place':'mumbai','sirname':'shaikh'}
    return render(request,"temp.html",varibale)

def text_analyzer(request):
    return render(request,'text_analyzer.html')