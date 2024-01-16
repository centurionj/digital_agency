from django.views.generic import TemplateView

from server.mixins.views_mixin import TitleMixin


class ServicesListView(TitleMixin, TemplateView):
    """Класс отображения услуг"""
    template_name = 'services/services.html'
    title = 'Kinza - Portfolio'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(IndexView, self).get_context_data()
    #     context['services'] = Service.objects.all()
    #     return context
