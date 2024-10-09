from django.forms import *
from core.models import Category


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Category Name',
                    'autofocus': 'true'
                }
            ),
            'desc': Textarea(
                attrs={
                    'rows': 3,
                    'cols': 6,
                }
            )

        }
        # fields = ["pub_date", "headline", "content", "reporter"]


class ProcesoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs ['autofocus'] = True


    # def save(self, commit=True):
    #     data = {}
    #     form = super()
    #     try:
    #         if form.is_valid():
    #             form.save()
    #         else:
    #             data['errors'] = form.errors
    #     except Exception as e:
    #         data['errors'] = str(e)
    #     return data
