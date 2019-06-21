
from django.shortcuts import render, redirect
from .models import Video
from .forms import  VideoForm, videoeditForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserChangeForm


# Create your views here.
def movie_list(request):
    return render(request = request,
                  template_name='stuff/home.html',
                  context = {"movie":Video.objects.all()})
def video1(request,vid):
    movie = Video.objects.get(pk=vid)
    #form = VideoForm(request.FILES)
    return render(request, 'stuff/video_play.html', {'movie': movie})

def video(request):
    form = VideoForm(request.FILES, request.POST)
    if(request.POST):
        form = VideoForm(request.FILES, request.POST)
        return render(request,'stuff/home.html',{'form':form})

    return render(request = request,
                  template_name='stuff/video_play.html',
                  context={"movie": Video.objects.all})

def AddNewMovie(request):
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form=VideoForm()
    return render(request, 'stuff/AddNew.html', {
        'form':form
        })


def video_edit(request,mid):
    movie = Video.objects.get(pk=mid)
    if request.method=='POST':
        form = VideoForm(request.POST,request.FILES,instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/movielib')
    else:
        form=VideoForm(instance=movie)
        args={'form':form}
        return render(request, 'stuff/edit.html', {'form':form})


def delete_movie(request,movId):
    Video.objects.get(pk=movId).delete()
    return redirect('/movie_list')





