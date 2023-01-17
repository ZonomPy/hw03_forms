from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    """ Класс AboutAuthorView для страницы about/author. """
    template_name = 'about/author.html'


class AboutTechView(TemplateView):
    """ Класс AboutTechView для страницы about/tech. """
    template_name = 'about/tech.html'
