from django.forms import ModelForm

from core.models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        #fields = ["pub_date", "headline", "content", "reporter"]