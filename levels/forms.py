from django import forms
from levels.models import PlotSell, Level
from accounts.models import CustomUser


class LevelForm(forms.ModelForm):
    error_messages = {
        'lead_required': ("Lead is a required field."),
        'subject_required': ("Subject is a required field."),
        'level_required': ("Level is a required field."),
        'share_percentage_required': ("Share Percentage is a required field."),
    }
    lead = forms.ModelChoiceField(label=("Select Lead"),
                                queryset=CustomUser.objects.all(),
                                widget=forms.Select(attrs={'class': 'block w-full py-3 px-2 shadow-sm sm:text-sm focus:ring-grape-500 focus:border-grape-500 border-gray-300 rounded-md'}))
    subject = forms.ModelChoiceField(label=("Select Subject"),
                                queryset=CustomUser.objects.all(),
                                widget=forms.Select(attrs={'class': 'block w-full py-3 px-2 shadow-sm sm:text-sm focus:ring-grape-500 focus:border-grape-500 border-gray-300 rounded-md'}),
                                )
    level = forms.CharField(label=("Level"),
                            widget=forms.TextInput(attrs={'class': 'block w-full py-3 px-2 shadow-sm sm:text-sm focus:ring-grape-500 focus:border-grape-500 border-gray-300 rounded-md'}))
    share_percentage = forms.CharField(label=("Share Percentage"),
                                       widget=forms.TextInput(attrs={'class': 'block w-full py-3 px-2 shadow-sm sm:text-sm focus:ring-grape-500 focus:border-grape-500 border-gray-300 rounded-md'}))
    
    
    class Meta:
        model = Level
        fields = ['lead', 'subject', 'level', 'share_percentage']


class PlotSellForm(forms.ModelForm):
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
        model = PlotSell
        fields = ['name', 'description']
