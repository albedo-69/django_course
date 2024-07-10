from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Entry, Topic
from .forms import AddEntryForm, AddTopicForm, EditTopicForm
from django.views import View
from django.contrib.auth import get_user_model, authenticate


def index(request):
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    user_id = request.user.id
    topics = Topic.objects.filter(author_id=user_id).order_by('-date_added')
    data = {'topics': topics}
    return render(request, 'learning_logs/topics.html', data)


@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entries.all().order_by('-date_added')
    data = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', data)


@login_required
def edittopic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method == 'POST':
        form = EditTopicForm(request.POST)
        if form.is_valid():
            form.save(topic_id)
            return redirect('/topics/')
    else:
        form = EditTopicForm()
    return render(request, 'learning_logs/edittopic.html', {'topic': topic,'form': form})


@login_required
def deltopic(request, topic_id):
    topic = Topic.objects.get(pk=topic_id)
    if request.method == 'POST':
        topic.delete()
        return redirect('/topics/')
    data = {'topic': topic}
    return render(request, 'learning_logs/confirm_del_topic.html', data)

       
class AddTopic(LoginRequiredMixin, View):
    form = AddTopicForm()
    
    def get(self, request):
        form = AddTopicForm()
        data = {'form': form}
        return render(request, 'learning_logs/addtopic.html', data)
    
    def post(self, request):
        if request.method == 'POST':
            form = AddTopicForm(request.POST)
            if form.is_valid():
                w = form.save(commit=False)
                w.author = self.request.user
                form.save()
                return redirect('/topics/')
            
    def form_valid(self, form):
        
        return super().form_valid(form)
    
    
class AddEntry(LoginRequiredMixin, View):
    def get(self, request, topic_id):
        form = AddEntryForm()
        data = {'form': form}
        return render(request, 'learning_logs/addentry.html', data)
    
    def post(self, request, topic_id):
        if request.method == 'POST':
            form = AddEntryForm(request.POST)
            if form.is_valid():
                form.save(topic_id)
                return redirect(f"/topics/{topic_id}")
        
        
        
