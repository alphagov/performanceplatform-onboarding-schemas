import json
import jsonschema
from jsonschema import Draft4Validator
from jsonschema import SchemaError


class Draft4StrictValidator(Draft4Validator):
    # strict validation ... whatch out ... use of '$ref' in 'oneOf' can barf!!!
    META_SCHEMA = dict(Draft4Validator.META_SCHEMA,additionalProperties=False)