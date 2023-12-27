from typing import Any
from django.views.generic import FormView, UpdateView, DetailView, TemplateView, ListView
from . forms import LevelForm, PlotSellForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from levels.models import Level, PlotSell
from django.contrib import messages


class ListLevelView(LoginRequiredMixin, ListView):
    model = Level
    template_name = 'levels/list_affiliates.html'
    context_object_name = 'levels'

    def get_queryset(self):
        return Level.objects.all()
    

class DetailLevelView(LoginRequiredMixin, DetailView):
    model = Level
    template_name = 'levels/detail_level.html'
    context_object_name = 'level'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class CreateLevelView(LoginRequiredMixin, FormView):

    template_name = 'levels/add_affiliate.html'
    success_url = reverse_lazy('accounts:dashboard')
    form_class = LevelForm
    model = Level

    def form_valid(self, form):
        # perform a action here
        group_obj = form.save(commit=False)
        group_obj.createdBy = self.request.user
        group_obj.save()    
        messages.add_message(self.request, messages.INFO, 'You have successfully created a level!')
        return HttpResponseRedirect(reverse('levels:list'))
    


    

