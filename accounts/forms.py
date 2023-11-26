from django import forms
from .models import CustomUser
from django.core.validators import FileExtensionValidator


class UserRegistrationForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
        'username_required': ("User name is a required field."),
        'valid_images': {"Image uploaded is not in valid form, must be in png or jpg format!"}
    }
    password1 = forms.CharField(label=("Password"),
                                widget=forms.PasswordInput(attrs={'class': 'block w-full py-3 px-2 shadow-sm sm:text-sm focus:ring-grape-500 focus:border-grape-500 border-gray-300 rounded-md'}))
    password2 = forms.CharField(label=("Password confirmation"),
                                widget=forms.PasswordInput(attrs={'class': 'block w-full py-3 px-2 shadow-sm sm:text-sm focus:ring-grape-500 focus:border-grape-500 border-gray-300 rounded-md'}),
                                help_text=("Enter the same password as above, for verification."))
    username = forms.CharField(label=("Please Enter Username"),
                               widget=forms.TextInput(attrs={'class': 'block w-full py-3 px-2 shadow-sm sm:text-sm focus:ring-grape-500 focus:border-grape-500 border-gray-300 rounded-md'}))
    email = forms.EmailField(label=("Please Enter Your Email"),
                             widget=forms.TextInput(attrs={'class': 'block w-full py-3 px-2 shadow-sm sm:text-sm focus:ring-grape-500 focus:border-grape-500 border-gray-300 rounded-md'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email',]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def clean_user_name(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError(
                self.error_messages['username_required'],
                code='username_required'
            )
        return username

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    

class UpdateAccountSettings(forms.ModelForm):

    error_messages = {
        'valid_images': {"Image uploaded is not in valid form, must be in png or jpg format!"}
    }

    username = forms.CharField(label=("Please Enter Username"),
                               widget=forms.TextInput(attrs={'class': 'block w-full py-3 px-2 shadow-sm sm:text-sm focus:ring-grape-500 focus:border-grape-500 border-gray-300 rounded-md'}))
    firstName = forms.CharField(label=("Please Enter Your First Name"),
                             widget=forms.TextInput(attrs={'class': 'block w-full py-3 px-2 shadow-sm sm:text-sm focus:ring-grape-500 focus:border-grape-500 border-gray-300 rounded-md'}))
    
    lastName = forms.CharField(label=("Please Enter Your Last Name"),
                             widget=forms.TextInput(attrs={'class': 'block w-full py-3 px-2 shadow-sm sm:text-sm focus:ring-grape-500 focus:border-grape-500 border-gray-300 rounded-md'}))
    profile_image = forms.ImageField(label=("Please Upload Your Profile Image"),
                                    widget=forms.FileInput(attrs={'class': 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'}),
                                    validators=[FileExtensionValidator(['png', 'jpg'])])
    
    def clean_profile_image(self):
        # if size of profile image is > 2 MB return error
        profile_image = self.cleaned_data.get('profile_image')
        if profile_image.size > 2097152:
            raise forms.ValidationError("Image file too large ( > 2mb )")
        return profile_image
 

    class Meta:

        model = CustomUser
        fields = ['username', 'firstName', 'lastName', 'profile_image',]

    


