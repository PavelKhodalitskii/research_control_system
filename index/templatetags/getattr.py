from django import template
register = template.Library()

@register.filter
def getattr (obj, arg):
    (attribute, default) = arg, None
    try:
        return obj.__getattribute__(attribute)
    except AttributeError:
         return  obj.__dict__.get(attribute, default)
    except:
        return default