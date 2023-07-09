from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = "page/index.html"
    
class Catering(TemplateView):
    template_name = "page/catering.html"

class Cerveza(TemplateView):
    template_name = "page/cerveze.html"
    
class Contacto(TemplateView):
    template_name = "page/contacto.html"
    
class Menu(TemplateView):
    template_name = "page/menu.html"
    
class Postres(TemplateView):
    template_name = "postres.html"