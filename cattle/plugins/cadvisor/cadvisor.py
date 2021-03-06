import os

from cattle import Config
from cattle.process_manager import background


class Cadvisor(object):

    def on_startup(self):
        cmd = ['cadvisor',
               '-logtostderr=true',
               '-listen_ip', Config.cadvisor_ip(),
               '-port', str(Config.cadvisor_port())]

        wrapper = Config.cadvisor_wrapper()

        if len(wrapper):
            cmd.insert(0, wrapper)
        else:
            if os.path.exists('/host/proc/1/ns/mnt'):
                cmd = ['nsenter', '--mount=/host/proc/1/ns/mnt', '--'] + cmd

        background(cmd)
