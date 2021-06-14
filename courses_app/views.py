from django.db.models.expressions import F
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course, Desc, Comment

def index(request):
    context = {
        "all_courses": Course.objects.all()
    }
    return render(request, "index.html", context)

def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/')

    elif request.method == "POST":
        new_desc = Desc.objects.create(desc=request.POST['description'])
        new_course = Course.objects.create(name=request.POST['name'], description=new_desc)
        print(new_course.__dict__)
        print(new_desc.__dict__)
        messages.success(request,"Course successfully created")
    
    return redirect('/')

def destroy(request, id):
    desc = Desc.objects.get(id=id)
    course = Course.objects.get(description=desc)
    context = {
        "course": course 
    }
    return render(request, "delete.html", context)


def confirm_destroy(request):
    if request.method == "POST":
        instance = Desc.objects.get(id=request.POST['desc_id']) # desc_id is hidden field from form
        instance.delete()                                       # delete the Desc, which cascades to the Course

    return redirect('/')

def comment(request, id):
    desc = Desc.objects.get(id=id)
    course = Course.objects.get(description=desc)
    context = {
        "course": course, 
        "all_comments": course.comments.all
    }
    return render(request, "comment.html", context)

def comment_add(request, id):
    if request.method == 'POST':
        desc = Desc.objects.get(id=id) 
        course = Course.objects.get(description=desc)
        new_comment = Comment.objects.create(name=request.POST['name'], comment=request.POST['comment'], course=course)
        print(new_comment.__dict__)
    
    return redirect(f'/courses/comment/{id}')






# Create your views here.
