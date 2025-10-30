from django import forms
from .models import UserGroups, Plot, PlotImages
from django.core.exceptions import ValidationError


class GroupForm(forms.ModelForm):
    error_messages = {
        'description_required': ("Description is a required field."),
        'name_required': ("Name is a required field."),
    }
    name = forms.CharField(label=("Name"),
                                widget=forms.TextInput(attrs={'class': 'block w-full py-3 px-2 shadow-sm sm:text-sm focus:ring-grape-500 focus:border-grape-500 border-gray-300 rounded-md'}))
    description = forms.CharField(label=("Description"),
                                widget=forms.Textarea(attrs={'class': 'block w-full py-3 px-2 shadow-sm sm:text-sm focus:ring-grape-500 focus:border-grape-500 border-gray-300 rounded-md'}),
                                )
    def clean_name(self):
        name = self.cleaned_data.get('name')
        
        # Check if the name exists and its length is less than 4
        if name and len(name) < 4:
            raise ValidationError("Name cannot be shorter than 4 letters.")
    
        return name

    class Meta:
        model = UserGroups
        fields = ['name', 'description']


class PlotForm(forms.ModelForm):

    error_messages = {
        'location_required': ("Location is a required field."),
        'price_required': ("Price is a required field."),
        'description_required': ("Description is a required field."),
    }
    location = forms.CharField(label=("Name"),
                                widget=forms.TextInput(attrs={'class': 'block w-full py-3 px-2 shadow-sm sm:text-sm focus:ring-grape-500 focus:border-grape-500 border-gray-300 rounded-md'}))
    price = forms.CharField(label=("Name"),
                                widget=forms.TextInput(attrs={'class': 'block w-full py-3 px-2 shadow-sm sm:text-sm focus:ring-grape-500 focus:border-grape-500 border-gray-300 rounded-md'}))
    description = forms.CharField(label=("Description"),
                                widget=forms.Textarea(attrs={'class': 'block w-full py-3 px-2 shadow-sm sm:text-sm focus:ring-grape-500 focus:border-grape-500 border-gray-300 rounded-md'}),
                                )
    
    class Meta:
        model = Plot
        fields = ['location', 'price', 'description']


class PlotImageForm(forms.ModelForm):

    error_messages = {
        'plot_required': ("Plot is a required field."),
        'title_required': ("Title is a required field."),
    }
    plot = forms.ModelChoiceField(label=("Plot"), queryset=Plot.objects.all(),
                                widget=forms.Select(attrs={'class': 'block w-full py-3 px-2 shadow-sm sm:text-sm focus:ring-grape-500 focus:border-grape-500 border-gray-300 rounded-md'}))
    title = forms.CharField(label=("Title"),
                                widget=forms.TextInput(attrs={'class': 'block w-full py-3 px-2 shadow-sm sm:text-sm focus:ring-grape-500 focus:border-grape-500 border-gray-300 rounded-md'}))
    image = forms.ImageField(label=("Image"),
                                widget=forms.ClearableFileInput(),
                                )
    
    class Meta:
        model = PlotImages
        fields = ['plot', 'title', 'image']
        required = ['plot', 'title']



