# core/templatetags/group_tags.py

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag(takes_context=True)
def get_group_action(context, group):
    user = context.get('user')
    
    if user and user.is_authenticated:
        if user.id == group.createdBy.id:
            html = '<a href="/edit/group/{}">Edit Group</a>'.format(group.id) 
        else:
            html = '<a href="/view/group/{}">View Group</a>'.format(group.id) 
    else:
        html = 'Login to see options'
        
    return mark_safe(html)