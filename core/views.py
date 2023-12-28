from django.views.generic import FormView, UpdateView, ListView, DetailView
from . forms import PlotForm, PlotImageForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Plot, PlotImages
from django.contrib import messages


class ListPlotView(LoginRequiredMixin, ListView):
    model = Plot
    template_name = 'plots/list_plots.html'
    context_object_name = 'plots'

    def get_queryset(self):
        return Plot.objects.all()
    

class UpdatePlotView(LoginRequiredMixin, UpdateView):
    model = Plot
    template_name = 'plots/update_plot.html'
    context_object_name = 'plot'
    form_class = PlotForm

    def get_object(self):
        # get the level id from the url
        plot_id = self.kwargs.get('pk')
        plot_obj = Plot.objects.get(id=plot_id)
        return plot_obj

    def form_valid(self, form):
        # perform a action here
        level_obj = form.save(commit=False)
        level_obj.save()    
        messages.add_message(self.request, messages.INFO, 'You have successfully updated a plot!')
        return HttpResponseRedirect(reverse('plots:plot-list'))
    

class DetailPlotView(LoginRequiredMixin, DetailView):
    model = Plot
    template_name = 'plots/detail_plot.html'
    context_object_name = 'plot'

    def get_object(self):
        # get the level id from the url
        plot_id = self.kwargs.get('pk')
        plot_obj = Plot.objects.get(id=plot_id)
        return plot_obj
    

class CreatePlotView(LoginRequiredMixin, FormView):

    template_name = 'plots/add_plot.html'
    form_class = PlotForm
    model = Plot

    def form_valid(self, form):
        # perform a action here
        level_obj = form.save(commit=False)
        level_obj.createdBy = self.request.user
        level_obj.save()    
        messages.add_message(self.request, messages.INFO, 'You have successfully created a plot!')
        return HttpResponseRedirect(reverse('plots:plot-list'))
    

class ListPlotImageView(LoginRequiredMixin, ListView):
    model = PlotImages
    template_name = 'plots/list_plot_images.html'
    context_object_name = 'plot_images'

    def get_queryset(self):
        return PlotImages.objects.all()
    

class CreatePlotImageView(LoginRequiredMixin, FormView):

    template_name = 'plots/add_plot_image.html'
    form_class = PlotImageForm
    model = PlotImages

    def form_valid(self, form):
        # perform a action here
        level_obj = form.save(commit=False)
        level_obj.save()    
        messages.add_message(self.request, messages.INFO, 'You have successfully created a plot image!')
        return HttpResponseRedirect(reverse('plots:plot-images'))
    