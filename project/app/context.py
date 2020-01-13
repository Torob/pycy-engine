# Whatever you define here, will be defined only once,
# and will be accessible from different places.

from persistqueue import PDict
from concurrent.futures import ThreadPoolExecutor

from .mod_wrappers import TestMod1


# Singletons are instantiated here ...
qStore = PDict('data', 'qStore')
mod1_instance = TestMod1(qstore_path='data', qstore_name='qStore')
executors = ThreadPoolExecutor(max_workers=4)


def init_qStore():
    if 'is_initialized' in qStore and qStore['is_initialized'] == 'True':
        return

    qStore['is_initialized'] = 'True'
    qStore['download_job_status'] = 'not_started'

    qStore['current_job'] = ''
    qStore['classifier_is_live'] = False


def reload_all_instances():
    mod1_instance.go_fake()
    mod1_instance.start_loading()
    mod1_instance.renew()
