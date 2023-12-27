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
        'amount_required': ("Amount is a required field."),
        'seller_required': ("Seller is a required field."),
        'buyer_required': ("Buyer is a required field."),
        'location_required': ("Location is a required field."),
    }
    amount = forms.CharField(label=("Amount"),
                                widget=forms.TextInput(attrs={'class': 'block w-full py-3 px-2 shadow-sm sm:text-sm focus:ring-grape-500 focus:border-grape-500 border-gray-300 rounded-md'}))
    seller = forms.ModelChoiceField(label=("Select Seller"),
                                queryset=CustomUser.objects.all(),
                                widget=forms.Select(attrs={'class': 'block w-full py-3 px-2 shadow-sm sm:text-sm focus:ring-grape-500 focus:border-grape-500 border-gray-300 rounded-md'}),
                                )
    buyer = forms.CharField(label=("Buyer"),
                                widget=forms.TextInput(attrs={'class': 'block w-full py-3 px-2 shadow-sm sm:text-sm focus:ring-grape-500 focus:border-grape-500 border-gray-300 rounded-md'}))
    location = forms.CharField(label=("Location"),
                                widget=forms.TextInput(attrs={'class': 'block w-full py-3 px-2 shadow-sm sm:text-sm focus:ring-grape-500 focus:border-grape-500 border-gray-300 rounded-md'}))

    class Meta:
        model = PlotSell
        fields = ['amount', 'seller', 'buyer', 'location']
