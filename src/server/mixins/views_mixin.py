class TitleMixin:
    """Миксин для заголовка"""
    title = None

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context

class TitleDetailMixin:
    """Миксин для заголовка в детальном просмотре"""

    def get_context_data(self, **kwargs):
        context = super(TitleDetailMixin, self).get_context_data(**kwargs)
        context['title'] = f'Kinza - {self.object.title}'
        return context