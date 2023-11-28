from typing import Any
from django.db import models
from django.shortcuts import render
from django.views.generic import FormView, UpdateView, DetailView, TemplateView
from . forms import UserRegistrationForm, UpdateAccountSettings
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth import authenticate, login
from .models import CustomUser
from core.models import UserGroups, Message, GroupMembers
from core.forms import GroupForm
from django.contrib import messages



class RegisterUser(FormView):
    template_name = 'accounts/register.html'
    form_class = UserRegistrationForm
    success_url = 'home'

    def form_valid(self, form):
        # perform a action here
        user_obj = form.save(commit=False)
        user_obj.staff = False
        user_obj.admin = False
        user_obj.is_customer = True
        user_obj.save()
        messages.add_message(self.request, messages.INFO, 'You have successfully registered, Please login to continue!')
        return HttpResponseRedirect(reverse('accounts:login'))


class LoginView(View):

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            messages.add_message(self.request, messages.INFO,
                                 'You have successfully logged in! Please continue to your dashboard!')
            login(request, user)
            return HttpResponseRedirect(reverse('accounts:dashboard'))
        else:
            messages.add_message(self.request, messages.ERROR, 'Failed to Login, please try again!')
            return HttpResponseRedirect(self.request.path_info)

    def get(self, request):
        return render(request, 'accounts/login.html', {})


class UpdateAccountSettings(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UpdateAccountSettings
    template_name = 'accounts/profile.html'

    def get_object(self, queryset=None):
        return CustomUser.objects.get(id=self.request.user.id)

    def form_valid(self, form):
        # perform a action here
        user_obj = form.save(commit=False)
        user_obj.staff = False
        user_obj.admin = False
        user_obj.save()
        messages.add_message(self.request, messages.INFO, 'You have successfully updated your account settings')
        return HttpResponseRedirect(reverse('accounts:dashboard'))


class AccountDashboard(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'accounts/dashboard.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        # pass all objects of UserGroups to the template
        kwargs['groups'] = UserGroups.objects.all()
        return super().get_context_data(**kwargs)

    def get_object(self, queryset=None):
        return CustomUser.objects.get(id=self.request.user.id)
    


class UserGroupDetailView(LoginRequiredMixin, DetailView):

    model = UserGroups
    template_name = 'group/group_detail.html'
    context_object_name = 'group'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        # pass all members and messages of the group to the template
        kwargs['messages'] = Message.objects.filter(group=self.get_object())
        kwargs['members'] = GroupMembers.objects.filter(group=self.get_object())
        return super().get_context_data(**kwargs)

    def get_object(self):
        # get the group id from the url
        group_id = self.kwargs.get('pk')
        group_obj = UserGroups.objects.get(id=group_id)
        return group_obj
    
    # handle post request
    def post(self, request, *args, **kwargs):
        # get the group object
        group_obj = self.get_object()
        # get the message from the form
        message = request.POST.get('message')
        # create a message object
        Message.objects.create(group=group_obj, sender=request.user, text=message)
        return HttpResponseRedirect(reverse('accounts:group-detail', kwargs={'pk': group_obj.id}))
        
    
    # delete view
    def delete(self, request, *args, **kwargs):
        # get the group object
        group_obj = self.get_object()
        # delete the group object
        group_obj.delete()
        messages.add_message(self.request, messages.INFO, 'You have successfully deleted the group!')
        return HttpResponseRedirect(reverse('accounts:dashboard'))
    

class CreateGroup(LoginRequiredMixin, FormView):

    template_name = 'group/create_group.html'
    success_url = reverse_lazy('accounts:dashboard')
    form_class = GroupForm
    model = UserGroups

    def form_valid(self, form):
        # perform a action here
        group_obj = form.save(commit=False)
        group_obj.createdBy = self.request.user
        group_obj.save()    
        messages.add_message(self.request, messages.INFO, 'You have successfully created a group!')
        return HttpResponseRedirect(reverse('accounts:dashboard'))
    

class Membership(LoginRequiredMixin, TemplateView):

    template_name = 'group/membership.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        # pass all objects of UserGroups to the template
        kwargs['groups'] = UserGroups.objects.all()
        kwargs['members'] = CustomUser.objects.all()
        return super().get_context_data(**kwargs)
    

    def post(self, request, *args, **kwargs):
        # get the group object
        group_id = request.POST.get('group')
        user_id = request.POST.get('user')
        level = request.POST.get('level')
        # create a message object
        group = UserGroups.objects.get(id=group_id)
        user = CustomUser.objects.get(id=user_id)
        # check if member already exists
        if GroupMembers.objects.filter(group=group, member=user).exists():
            messages.add_message(self.request, messages.ERROR, format(user.username) + ' is already a member of ' + format(group.name) + ' group!')
            return HttpResponseRedirect(reverse('accounts:dashboard'))
        GroupMembers.objects.create(group=group, member=user, level=level)
        # return formatted response
        messages.add_message(self.request, messages.INFO, format(user.username) + ' has been added to ' + format(group.name) + ' group!')
        return HttpResponseRedirect(reverse('accounts:dashboard'))
    

        

    

