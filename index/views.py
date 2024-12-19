from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class TableRawDataView(TemplateView):
    def filter_raw_data(self, additional_data):
        foreign_key_fields = additional_data['foreign_key_fields']
        order_by_fields = additional_data['order_by_fields']
        foreign_key_choices = additional_data['foreign_key_choices']

        for field in foreign_key_fields:
            filter_value = self.request.GET.get(field)
            if filter_value:
                filtered_items = []
                for item in additional_data['items']:
                    if str(item.__getattribute__(field)) == str(foreign_key_choices[field].filter(pk=filter_value).first()):
                        filtered_items.append(item)
                additional_data['items'] = filtered_items

        for field in order_by_fields:
            filter_value = self.request.GET.get(field)
            if filter_value == 'ascending':
                additional_data['items'] = sorted(additional_data['items'], key=lambda x: x.__getattribute__(field), reverse=False)
            elif filter_value == 'descending':
                additional_data['items'] = sorted(additional_data['items'], key=lambda x: x.__getattribute__(field), reverse=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context["table_url"] = self.table_url
        context["creation_form_url"] = self.creation_form_url
        context["delete_several_url"] = self.delete_several_url
        return context