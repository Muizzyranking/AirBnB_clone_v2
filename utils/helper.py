#!/usr/bin/python3
"""Contains helper functions for the project"""


def process_parameters(parameters):
    """Processes and extracts key-value pairs from parameters."""
    instance_kwargs = {}
    for param in parameters:
        if "=" not in param:
            continue

        key, value = param.split("=", 1)
        instance_kwargs[key] = parse_value(value)

    return instance_kwargs


def parse_value(value):
    """Parses a value based on its type (string, float, integer)."""
    try:
        if value.startswith('"'):
            return value.strip('"').replace('\\"', '"').replace('_', ' ')
        elif '.' in value:
            return float(value)
        else:
            return int(value)
    except ValueError:
        return value  # Return unchanged if conversion fails
