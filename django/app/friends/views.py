from django.shortcuts import render

from .models import School


def school_detail(request, pk):
    post = School.objects.get(id=pk)
    context = {
        'post': post,
    }
    return render(request, 'friends/school_detail.html', context)
