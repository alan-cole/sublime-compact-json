import json
from sublime_plugin import TextCommand
from sublime import Region
from .src.py.compact_json.formatter import Formatter, EolStyle

def main(view, edit):
    # Prep the formatter
    formatter = Formatter()
    formatter.indent_spaces = 2
    formatter.max_inline_complexity = 10
    formatter.json_eol_style = EolStyle.LF

    # Get region
    region = [Region(0, view.size())]
    if not view.sel()[0].empty():
        region = view.sel()

    for sel_region in region:
        # Get Content
        selected_text = view.substr(sel_region)
        obj = json.loads(selected_text)
        formatted_text = formatter.serialize(obj)
        view.replace(edit, sel_region, formatted_text)

class CompactjsonCommand(TextCommand):
    def run(self, edit):
        main(self.view, edit)
