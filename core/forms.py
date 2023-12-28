from django import forms
from .models import UserGroups, Plot, PlotImages


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



