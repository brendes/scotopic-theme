#!/usr/bin/env python3

import json
import yaml
from themes import themes


def generate_theme(theme_dict, template_file, output_file):
    """Generate a color-theme JSON file based on a theme dictionary."""
    with open(template_file, "r") as f:
        theme_template = yaml.safe_load(f)

    def recursive_format(value):
        if isinstance(value, str):
            return value.format(**theme_dict)
        elif isinstance(value, list):
            return [recursive_format(item) for item in value]
        elif isinstance(value, dict):
            return {key: recursive_format(val) for key, val in value.items()}
        else:
            return value

    theme_output = recursive_format(theme_template)

    with open(output_file, "w") as f:
        json.dump(theme_output, f, indent=2)


def main():
    generate_theme(
        themes["main"], "src/template.yml", "themes/scotopic-color-theme.json"
    )
    generate_theme(
        themes["amber"], "src/template.yml", "themes/scotopic-amber-color-theme.json"
    )
    generate_theme(
        themes["deep"], "src/template.yml", "themes/scotopic-deep-color-theme.json"
    )


if __name__ == "__main__":
    main()
