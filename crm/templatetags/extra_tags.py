from django import template
from crm.models import Operation

register = template.Library()


@register.simple_tag
def pending_aproved():
    return Operation.objects.filter(status_id=1).count()
