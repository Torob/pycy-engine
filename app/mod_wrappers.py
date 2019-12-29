from pycy.utils import BasicCythonWrapper
from ..mods import pMod1


class TestMod1(BasicCythonWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.q_prefix = 'mod1_'
        self.handler = None
        self.is_loading = False
        self.is_live = False

    def init(self):
        if not self.handler:
            self.handler = pMod1()
            self.handler.initiate()
            self.end_loading()
            self.go_live()
