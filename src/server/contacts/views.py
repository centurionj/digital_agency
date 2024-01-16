from django.views.generic import TemplateView

from server.mixins.views_mixin import TitleMixin

class ContactsView(TitleMixin, TemplateView):
    """Клас отображения страницы с контактами"""
    template_name = 'contacts/contacts.html'
    title = 'Kinza - контакты'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(IndexView, self).get_context_data()
    #     context['services'] = Service.objects.all()
    #     return context
