from django import template
from engine.models import MerchantTheme, SimpleText

register = template.Library()
@register.simple_tag()

def create_simple_text(merchanttheme, blockname):
    merchanttheme = MerchantTheme.objects.get(id=merchanttheme)
    return SimpleText.objects.get(
        merchanttheme=merchanttheme,
        blockname = blockname
    )