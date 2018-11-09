'''
The tests serve as the manual / documentation.
I link to specific test cases to display the apo.

When I change the tests, the links break,
so I wrote this script to update them.
'''

from pathlib import Path


URL = 'https://github.com/cessor/kazookid/blob/master/test/'


paths = [
    (path.name, path.read_text())
    for path in Path('test').iterdir()
    if not path.name.startswith('__')
]

for path, code in paths:
    for i, line in enumerate(code.split('\n'), start=1):
        if not line.strip().startswith("'''"):
            continue

        # Remove clutter
        caption = line.replace("'''", '')
        caption = caption.replace("Substitute:", '')
        caption = caption.replace("Context:", '')
        caption = caption.strip()

        # Docstrings are one line beneath the function signature
        line_number = i - 1

        # Markdown List Item with url
        entry = f' - [{caption}]({URL}{path}#L{line_number})'

        print(entry)
