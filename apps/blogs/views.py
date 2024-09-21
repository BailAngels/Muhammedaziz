from django.shortcuts import render, redirect

from apps.blogs.models import Blog


def homepage(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', locals())

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        blog_create = Blog.objects.create( title = title, description = description, image = image )

    return render(request, 'create.html')

def retrieve(request, pk):
    blogs = Blog.objects.get(id=pk)
    return render(request, 'retrieve.html', locals())

def update(request, pk):
    blog = Blog.objects.get(id=pk)

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        
        blog.title = title
        blog.description = description
        blog.image = image 
        blog.save()

    return render(request, 'update.html', {'blog' : blog})

def delete(request, pk):
    if request.method == 'POST':
        blog = Blog.objects.get(id=pk)
        blog.delete()
        return redirect('index')
    return render(request, 'delete.html')


