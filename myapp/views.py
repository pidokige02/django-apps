from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Content

# Create your views here.
selectedId = None

def IndexView(request):
    global selectedId
    latest_content_list = Content.objects.all()
    selectedId = None
    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''
    context = {
        'latest_content_list': latest_content_list,
        'article': article
    }
    return render(request, 'myapp/content.html', context)

def read(request, id):
    global selectedId

    latest_content_list = Content.objects.all()
    selectedId = id
    selected_content = Content.objects.filter(id=int(id)).first()
    article = f'<h2>{selected_content.title}</h2>{selected_content.body}'
    context = {
        'latest_content_list': latest_content_list,
        'article': article,
        'selectedId' : selectedId
    }
    return render(request, 'myapp/content.html', context)


@csrf_exempt  #보안기능 면제하세요
def create(request):
    if request.method == 'GET':
        latest_content_list = Content.objects.all()
        article = '''
            <form action="/create/" method="post">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        context = {
            'latest_content_list': latest_content_list,
            'article': article
        }
        return render(request, 'myapp/content.html', context)

    elif request.method == 'POST':
        vtitle = request.POST['title']
        vbody = request.POST['body']

        c = Content(title=vtitle, body=vbody)
        c.save()

        last_content = Content.objects.filter(title=vtitle, body=vbody).last()

        url = '/read/'+str(last_content.id)
        return redirect(url)

@csrf_exempt
def update(request,id):
    global selectedId

    selectedId = id
    if request.method == 'GET':
        latest_content_list = Content.objects.all()
        selected_content = Content.objects.filter(id=int(id)).first()

        selectedContent = {
            "title" : selected_content.title,
            "body" : selected_content.body
        }
        article = f'''
            <form action="/update/{id}/" method="post">
                <p><input type="text" name="title" placeholder="title" value={selectedContent["title"]}></p>
                <p><textarea name="body" placeholder="body">{selectedContent['body']}</textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        context = {
            'latest_content_list': latest_content_list,
            'article': article,
            'selectedId' : selectedId
        }
        return render(request, 'myapp/content.html', context)
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        print("jinha", title, body)
        update_content = Content.objects.filter(id=int(id)).first()
        update_content.title = title
        update_content.body = body
        update_content.save()

        return redirect(f'/read/{id}')


@csrf_exempt
def delete(request):
    if request.method == 'POST':
        id = request.POST['id']
        Content.objects.filter(id=int(selectedId)).delete()

        return redirect('/')