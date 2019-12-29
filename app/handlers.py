from pycy.core import BaseEngineRequestHandler
from pycy.utils import BasicAuthMixin
from .mod_wrappers import TestMod1

# time to create some cy. instances
mod1_instance = TestMod1()


class MainHandler(BaseEngineRequestHandler):
    def get(self):
        self.write(dict(
            service='torob_FAST_pycy_server',
            version='0.1.1'
        ))


class HealthHandler(BaseEngineRequestHandler):
    def get(self):
        self.write(dict(
            healthy=True,
            live=True,
        ))


class ProtectedEndpointHandler(BasicAuthMixin, BaseEngineRequestHandler):
    def get(self):
        self.write(dict(
            message='congrats! you are now allowed here!'
        ))


class SampleModuleHandler(BaseEngineRequestHandler):
    def get(self):
        q = self.get_argument('q', None)
        answer = mod1_instance.handler.get_answer(q.encode('utf-8'))
        self.write(dict(
            answer=answer
        ))
