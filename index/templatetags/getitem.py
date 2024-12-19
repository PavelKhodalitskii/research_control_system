from django import template
register = template.Library()

@register.filter
def getitem (obj, item):
    try:
        return obj[item]
    except AttributeError:
         return  obj.get(item, None)
    except:
        return None