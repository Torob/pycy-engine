from .handlers import (
    MainHandler,
    HealthHandler,
    SampleModuleHandler
)


url_patterns = [
    (r"/", MainHandler),
    (r"/health", HealthHandler),
    (r"/mod-test", SampleModuleHandler)
]
