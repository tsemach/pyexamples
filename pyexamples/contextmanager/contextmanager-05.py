"""
from: https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/

Using contextlib.ContextDecorator.
It lets you define a context manager using the class-based approach,
by inheriting from contextlib.ContextDecorator.
By doing so, you can use your context manager with the with statement as normal or as a function decorator.
We could do something similar to the
HTML example above using this pattern (which is truly insane and shouldn't be done):
"""
from contextlib import ContextDecorator


class makeparagraph(ContextDecorator):
    def __enter__(self):
        print('<p>')
        return self

    def __exit__(self, *exc):
        print('</p>')
        return False


@makeparagraph()
def emit_html():
    print('Here is some non-HTML')

emit_html()
