from lib.jsonschema import JsonSchema


def validate_price_data(data):
    """
    Validate price data using JsonSchema
    """
    schema = {
        'title': 'Validate data of price',
        "type": "object",
        "required": [
            "price_fixed", "price_fractioned",
            "start", "end"
        ],
        "properties": {
            "active": {
                "type": "string",
                "enum": ["true", "false"]
            }
        }
    }
    jsonschema = JsonSchema()
    if (jsonschema.valid(schema, data) is False):
        return {'errors': jsonschema.getErrors()}
