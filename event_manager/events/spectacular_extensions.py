from drf_spectacular.extensions import OpenApiFilterExtension


class DjangoFilterExtension(OpenApiFilterExtension):
    target_class = 'django_filters.rest_framework.backends.DjangoFilterBackend'

    def get_schema_operation_parameters(self, auto_schema, *args, **kwargs):
        result = []
        view = auto_schema.view
        if hasattr(
            view, 'filterset_fields'
            ) and isinstance(
                view.filterset_fields, (list, tuple)):
            for field in view.filterset_fields:
                result.append({
                    'name': field,
                    'required': False,
                    'in': 'query',
                    'description': f'Filtration by the {field} field.',
                    'schema': {'type': 'string'},
                })
        return result
    

class DRFSearchFilterExtension(OpenApiFilterExtension):
    target_class = 'rest_framework.filters.SearchFilter'

    def get_schema_operation_parameters(self, auto_schema, *args, **kwargs):
        return [{
            'name': 'search',
            'required': False,
            'in': 'query',
            'description': 'Search by the fields: ' + ', '.join(getattr(auto_schema.view, 'search_fields', [])),
            'schema': {'type': 'string'},
        }]
    

class DRFOrderingFilterExtension(OpenApiFilterExtension):
    target_class = 'rest_framework.filters.OrderingFilter'

    def get_schema_operation_parameters(self, auto_schema, *args, **kwargs):
        return [{
            'name': 'ordering',
            'required': False,
            'in': 'query',
            'description': 'Sort by the fields: ' + ', '.join(getattr(auto_schema.view, 'ordering_fields', [])),
            'schema': {'type': 'string'},
        }]