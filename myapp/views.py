from django.shortcuts import render, HttpResponse
import random

# Create your views here.
topics = [  #list
    {'id':1, 'title':'routing', 'body':'Routing is ..'},  # dictionary
    {'id':2, 'title':'view', 'body':'View is ..'},
    {'id':3, 'title':'Model', 'body':'Model is ..'},
]

def index(request):
    global topics  # 전역변수임
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>' # f를 붙이면 중괄호일때 변수를 바로 사용할 수 있다
    return HttpResponse(f'''
    <html>
    <body>
        <h1>Django</h1>
        <ol>
            {ol}
        </ol>
        <h2>Welcome</h2>
        Hello, Django
    </body>
    </html>
    ''')

def create(request):
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse('Read!'+id)