import graphene
from graphene_django.registry import get_global_registry
from graphql_relay import from_global_id

registry = get_global_registry()


def get_model_name(model):
    """Return name of the model with first letter lowercase."""
    model_name = model.__name__
    return model_name[:1].lower() + model_name[1:]


def get_output_fields(model, return_field_name):
    """Return mutation output field for model instance."""
    model_type = registry.get_type_for_model(model)
    fields = {return_field_name: graphene.Field(model_type)}
    return fields


def clean_seo_fields(data):
    """Extract and assign seo fields to given dictionary."""
    seo_fields = data.pop('seo', None)
    if seo_fields:
        data['seo_title'] = seo_fields.get('title')
        data['seo_description'] = seo_fields.get('description')


def snake_to_camel_case(name):
    """Convert snake_case variable name to camelCase."""
    if isinstance(name, str):
        split_name = name.split('_')
        return split_name[0] + "".join(map(str.capitalize, split_name[1:]))
    return name


def get_nodes(ids, graphene_type=None):
    pks = []
    types = []
    for graphql_id in ids:
        _type, _id = from_global_id(graphql_id)
        if graphene_type:
            assert str(graphene_type) == _type, (
                'Must receive an {} id.').format(graphene_type._meta.name)
        pks.append(_id)
        types.append(_type)

    # If `graphene_type` was not provided, check if all resolved types are
    # the same. This prevents from accidentally mismatching IDs of different
    # types.
    if types and not graphene_type:
        assert len(set(types)) == 1, 'Received IDs of more than one type.'
        # get type by name
        type_name = types[0]
        for model, _type in registry._registry.items():
            if _type._meta.name == type_name:
                graphene_type = _type
                break

    nodes = list(graphene_type._meta.model.objects.filter(pk__in=pks))
    if not nodes:
        raise Exception(
            "Could not resolve to a nodes with the global id list of '%s'."
            % ids)
    nodes_pk_list = [str(node.pk) for node in nodes]
    for pk in pks:
        assert pk in nodes_pk_list, (
            'There is no node of type {} with pk {}'.format(_type, pk))
    return nodes
