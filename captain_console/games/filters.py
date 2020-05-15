from consoles.models import Consoles
import django_filters

class ConsoleFilter(django_filters.FilterSet):
    class Meta:
        model = Consoles
        fields = {'name': ['icontains'],
                  'description': ['exact'],
                  'brand': ['exact'], 
                  'price': ['gt', 'lt'],
                 }