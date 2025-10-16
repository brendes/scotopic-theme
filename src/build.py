#!/usr/bin/env python3

import json

themes = {
    "Scotopic": {
        "base_0": "#000000",
        "base_1": "#281818",
        "base_2": "#482828",
        "base_3": "#683838",
        "base_4": "#cc6666",
        "base_5": "#ee8888",
        "base_6": "#ff9999",
    },
    "Scotopic Deep": {
        "base_0": "#000000",
        "base_1": "#301010",
        "base_2": "#481414",
        "base_3": "#581818",
        "base_4": "#cc3333",
        "base_5": "#ee4444",
        "base_6": "#ff5555",
    },
}

for key, theme in themes.items():
    theme["theme_name"] = key
    theme["bg_main"] = theme["base_0"]
    theme["bg_subtle"] = theme["base_1"]
    theme["bg_fade"] = theme["base_2"]
    theme["bg_hl"] = theme["base_3"]
    theme["bg_sel"] = theme["base_3"] + "e8"
    theme["bg_match"] = theme["base_4"] + "78"
    theme["bg_drop"] = theme["bg_hl"] + "88"
    theme["fg_bold"] = theme["base_6"]
    theme["fg_main"] = theme["base_5"]
    theme["fg_accent"] = theme["base_4"]
    theme["invisible"] = "#00000000"

    if key == "Scotopic Deep":
        theme["fg_subtle"] = theme["base_5"] + "d0"
        theme["fg_dim"] = theme["base_5"] + "c8"
        theme["fg_fade"] = theme["base_5"] + "aa"
        theme["fg_faint"] = theme["base_5"] + "68"
    else:
        theme["fg_subtle"] = theme["base_5"] + "c8"
        theme["fg_dim"] = theme["base_5"] + "c0"
        theme["fg_fade"] = theme["base_5"] + "9b"
        theme["fg_faint"] = theme["base_5"] + "55"

    theme["border_soft"] = theme["fg_faint"]
    theme["border_hard"] = theme["fg_dim"]


def generate_theme(theme_dict, template_file, output_file):
    """Generate a color-theme JSON file based on a theme dictionary."""
    with open(template_file, "r", encoding="utf-8") as f:
        theme_template = json.load(f)

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

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(theme_output, f, indent=2)


def main():
    generate_theme(
        themes["Scotopic"], "src/template.json", "themes/scotopic-color-theme.json"
    )
    generate_theme(
        themes["Scotopic Deep"], "src/template.json", "themes/scotopic-deep-color-theme.json"
    )


if __name__ == "__main__":
    main()
