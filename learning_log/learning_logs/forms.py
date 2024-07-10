from django import forms
from .models import Topic, Entry


class AddTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title']
        labels = {'title': 'Тема:'}
        
    title = forms.CharField(label='Название', 
                            widget=forms.TextInput(attrs={'class': 'form-control', 
                                                          'placeholder': 'Введите название'}))
        
        
class EditTopicForm(forms.ModelForm):
    
    class Meta:
        model = Topic
        fields = ['title']
        labels = {'title': 'Новое название темы'}
    
    title = forms.CharField(label='Название',
                            widget=forms.TextInput(attrs={'class': 'form-control', 
                                                          'placeholder': 'Введите новое название'}))
        
    def save(self, topic_id):
        Topic.objects.filter(pk=topic_id).update(title=self.cleaned_data['title'])
        
        
class AddEntryForm(forms.ModelForm):
    
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Текст записи'}
        
    text = forms.CharField(label='Новая запись', 
                           widget=forms.Textarea(attrs={'class': 'form-control', 
                                                          'placeholder': 'Введите текст записи'}))
        
    def save(self, topic_id):
        Entry.objects.create(text=self.cleaned_data['text'], topic_id=topic_id,)
        
