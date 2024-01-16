from django.shortcuts import render
from django.views.generic import TemplateView

from server.mixins.views_mixin import TitleMixin


class LandingView(TitleMixin, TemplateView):
    """Класс отображения лэндинга"""
    template_name = 'landing/index.html'
    title = 'Kinza'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(IndexView, self).get_context_data()
    #     context['services'] = Service.objects.all()
    #     return context


def handler404(request, exception, *args, **argv):
    context = {
        'error': str({exception}),
        'code': 404,
    }
    response = render(request, 'error.html', context=context)
    response.status_code = 404
    return response


def handler400(request, exception, *args, **argv):
    context = {
        'error': str({exception}),
        'code': 400,
    }

    response = render(request, 'error.html', context=context)
    response.status_code = 400
    return response
