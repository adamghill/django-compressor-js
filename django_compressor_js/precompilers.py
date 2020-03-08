from compressor.filters.base import FilterBase
from dukpy import babel_compile


class BabelCompiler(FilterBase):
    def __init__(
        self, content, attrs=None, filter_type=None, charset=None, filename=None
    ):
        # FilterBase doesn't handle being passed attrs, so fiddle the signature
        super(BabelCompiler, self).__init__(
            content=content, filter_type=filter_type, filename=filename
        )

    def input(self, **kwargs):
        options = {}
        src = babel_compile(self.content, **options)

        return src["code"]
