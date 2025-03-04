#!/usr/bin/env python3

themes = {
    "main": {
        "theme_name": "Scotopic",
        "base_0": "#000000",
        "base_1": "#281818",
        "base_2": "#482828",
        "base_3": "#683838",
        "base_4": "#cc6666",
        "base_5": "#ee8888",
        "base_6": "#ff9999",
    },
    "deep": {
        "theme_name": "Scotopic Deep",
        "base_0": "#000000",
        "base_1": "#220000",
        "base_2": "#441111",
        "base_3": "#581111",
        "base_4": "#cc3333",
        "base_5": "#ee4444",
        "base_6": "#ff5555",
    },
}

for key, theme in themes.items():
    theme["bg_main"] = theme["base_0"]
    theme["bg_subtle"] = theme["base_1"]
    theme["bg_faint"] = theme["base_2"]
    theme["bg_fade"] = theme["base_2"]
    theme["bg_hl"] = theme["base_3"]
    theme["bg_sel"] = theme["base_3"] + "e8"
    theme["bg_match"] = theme["base_4"] + "78"
    theme["bg_drop"] = theme["bg_hl"] + "88"
    theme["fg_bold"] = theme["base_6"]
    theme["fg_main"] = theme["base_5"]
    theme["fg_accent"] = theme["base_4"]
    theme["fg_subtle"] = theme["fg_main"] + "c8"
    theme["fg_dim"] = theme["fg_main"] + "c0"
    theme["fg_fade"] = theme["fg_main"] + "88"
    theme["fg_faint"] = theme["fg_main"] + "55"
    theme["border_soft"] = theme["fg_faint"]
    theme["border_hard"] = theme["fg_fade"]
