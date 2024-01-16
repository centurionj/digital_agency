from django.views.generic import TemplateView

from server.mixins.views_mixin import TitleMixin


class PortfolioView(TitleMixin, TemplateView):
    """Класс отображения портфолио"""
    template_name = 'portfolio/portfolio.html'
    title = 'Kinza - Portfolio'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(IndexView, self).get_context_data()
    #     context['services'] = Service.objects.all()
    #     return context
