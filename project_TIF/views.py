from django.views.generic import TemplateView

class Landing(TemplateView):
    template_name = "pages/landing_page.html"
    
class Catering(TemplateView):
    template_name = "pages/catering.html"

class Cerveza(TemplateView):
    template_name = "pages/cerveza.html"
    
class Contacto(TemplateView):
    template_name = "pages/contacto.html"
    
class Menu(TemplateView):
    template_name = "pages/menu.html"
    
class Postres(TemplateView):
    template_name = "pages/postres.html"