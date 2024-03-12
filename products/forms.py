from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        # Adds a placeholder to the 'quantity_per_kg' field if it exists in the form.
        if 'quantity_per_kg' in self.fields:
            self.fields['quantity_per_kg'].widget.attrs['placeholder'] = 'E.g., 0.5 for 500g'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'