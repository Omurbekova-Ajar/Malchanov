from django import forms
from .models import Tag
from django.core.exceptions import ValidationError

class TagForm(forms.Form):
    title = forms.CharField(max_length=50)
    slug = forms.CharField(max_length=50)

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'], lower()

        if new_slug == 'create':
            raise ValidationError('Slug my not be "Create"')
        return new_slug

    def save(self):
        new_tag = Tag.objects.create(title=self.cleaned_data['title'],
                                     slug=self.cleaned_data['slug']
                                     )
        return new_tag