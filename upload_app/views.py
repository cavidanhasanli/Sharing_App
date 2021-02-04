from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from upload_app.forms import *
from upload_app.models import *
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()


# from django.utils import timezone
# from .tasks import delete_file
# from datetime import datetime, timedelta

# now = timezone.now() + timedelta(minutes=10)
# print(now)
# # delete_file(now)
# print(CreateFiles.objects.get(create_date__in=now))

# Create your views here.

@login_required()
def home_views(request):
    context = {}
    all_data = CreateFiles.objects.filter(user_id=request.user)
    context['all_data'] = all_data

    if request.method == 'POST':
        user_id = request.POST.get('data-user')
        file_id = request.POST.get('data-file')
        user_filter = User.objects.filter(username=user_id)
        print(request.user.username == user_id)
        if user_filter:

            if request.user.username != user_id:
                get_user = User.objects.get(username=user_id)
                SenderFiles.objects.create(user_id=int(request.user.id, ), sended_users_id=int(get_user.id),
                                           sended_files_id=int(file_id))
                return redirect('send_to_page')

            else:
                messages.info(request, 'Ozunuze gondere bilmersiz')
                return redirect('home_page')
        else:
            messages.info(request, 'Bele bir istifadeci adi yoxdur')
            return redirect('home_page')

    return render(request, 'home.html', context)


@login_required()
def send_from_views(request):
    send_from = SenderFiles.objects.filter(sended_users=request.user)

    my_data = []
    for i in send_from.values():
        files = CreateFiles.objects.filter(id=i['sended_files_id'])
        my_data.append(files)
    return render(request, 'send_from.html', context={'send_from': my_data})


@login_required()
def send_to_views(request):
    send_from = SenderFiles.objects.filter(user_id=request.user.id)

    my_data = []
    for i in send_from.values():
        files = CreateFiles.objects.filter(id=i['sended_files_id'])
        my_data.append(files)
    return render(request, 'send_to.html', context={'send_to': my_data})


@login_required()
def create_files_views(request):
    context = {}
    forms = CreateFilesForm()
    if request.method == 'POST':
        forms = CreateFilesForm(request.POST, request.FILES)
        if forms.is_valid():
            form = forms.save()
            form.user_id = request.user
            form.save()
            return redirect('home_page')

        else:
            forms = CreateFilesForm(request.POST, request.FILES)
            context['forms'] = forms
            return render(request, 'upload.html', context)
    else:
        context['forms'] = forms
        return render(request, 'upload.html', context)
