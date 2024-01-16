from django.views.generic import TemplateView

from server.mixins.views_mixin import TitleMixin

class AboutView(TitleMixin, TemplateView):
    """Класс отображения страницы о нас"""
    template_name = 'about/about.html'
    title = 'Kinza - о нас'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(IndexView, self).get_context_data()
    #     context['services'] = Service.objects.all()
    #     return context
