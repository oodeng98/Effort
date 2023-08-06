from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt


def HTMLTemplate(articleTag):
    return f"""
    {articleTag}
    <h2>JungTaeWan's Diary</h2>
    """


def index(request):
    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))