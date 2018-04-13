from django.views.generic import TemplateView
from engine.models import MerchantTheme

class PageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        ctx = super(PageView, self).get_context_data(**kwargs)
        #todo: Get MerchantTheme based on the middleware
        ctx['merchanttheme'] = MerchantTheme.objects.get(id=1)
        return ctx
