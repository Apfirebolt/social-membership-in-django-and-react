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
    

class UpdateLevelView(LoginRequiredMixin, UpdateView):
    model = Level
    template_name = 'levels/update_affiliate.html'
    context_object_name = 'level'
    form_class = LevelForm

    def get_object(self):
        # get the level id from the url
        level_id = self.kwargs.get('pk')
        level_obj = Level.objects.get(id=level_id)
        return level_obj

    def form_valid(self, form):
        # perform a action here
        level_obj = form.save(commit=False)
        level_obj.save()    
        messages.add_message(self.request, messages.INFO, 'You have successfully updated a level!')
        return HttpResponseRedirect(reverse('levels:list'))
    

class CreateLevelView(LoginRequiredMixin, FormView):

    template_name = 'levels/add_affiliate.html'
    form_class = LevelForm
    model = Level

    def form_valid(self, form):
        # perform a action here
        level_obj = form.save(commit=False)
        level_obj.createdBy = self.request.user
        level_obj.save()    
        messages.add_message(self.request, messages.INFO, 'You have successfully created a level!')
        return HttpResponseRedirect(reverse('levels:list'))
    

class ListPlotSellView(LoginRequiredMixin, ListView):
    model = PlotSell
    template_name = 'levels/list_sell.html'
    context_object_name = 'sells'

    def get_queryset(self):
        return PlotSell.objects.all()
    

class UpdatePlotSellView(LoginRequiredMixin, UpdateView):
    model = PlotSell
    template_name = 'levels/update_sell.html'
    context_object_name = 'sell'
    form_class = PlotSellForm

    def get_object(self):
        # get the sell id from the url
        sell_id = self.kwargs.get('pk')
        sell_obj = PlotSell.objects.get(id=sell_id)
        return sell_obj

    def form_valid(self, form):
        # perform a action here
        sell_obj = form.save(commit=False)
        sell_obj.save()    
        messages.add_message(self.request, messages.INFO, 'You have successfully updated a sell!')
        return HttpResponseRedirect(reverse('sells:list'))
    

class CreatePlotSellView(LoginRequiredMixin, FormView):

    template_name = 'levels/add_sell.html'
    form_class = PlotSellForm
    model = PlotSell

    def form_valid(self, form):
        # perform a action here
        sell_obj = form.save(commit=False)
        sell_obj.save()    
        messages.add_message(self.request, messages.INFO, 'You have successfully addad a Plot sell!')
        return HttpResponseRedirect(reverse('sells:list'))
    


    

