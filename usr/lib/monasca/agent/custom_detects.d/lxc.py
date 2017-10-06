import os
import logging

import monasca_setup.agent_config
import monasca_setup.detection

_LXC_CGROUP_CPU_PWD = '/sys/fs/cgroup/cpu/lxc/'
log = logging.getLogger(__name__)

class LXC(monasca_setup.detection.Plugin):
    """Detect if LXC is present on the host.

    LXC uses cgroup and namespaces to create a controlled and isolated
    environment. You can easily detect if lxc is installed on machine, searching
    for /var/lib/lxc. But, if you uninstall lxc, this dir must not be
    removed. THIS DETECT CAN NOT VERIFY ALL CONTAINERS (RUNNING AND STOPPED)
    WITHOUT ROOT ACCESS TO MONASCA-AGENT USER. Only running containers will be
    detect.

    To detect if any container is running, You can search if there are any
    folders in /sys/fs/cgroup/cpu/lxc/. Folders name are the same containers
    running name.
    """

    def __init__(self, template_dir, overwrite=True, args=None):
        self.service_name = 'lxc'
        super(LXC, self).__init__(template_dir, overwrite, args)

    def _detect(self):
        """Verify if there are running containers."""
        for name_all in os.listdir(_LXC_CGROUP_CPU_PWD):
            if os.path.isdir(name_all):
                self.available = True
                break

    def build_config(self):
        config = monasca_setup.agent_config.Plugins()
        config['default'] = {'init_config': None,
                             'instances': [
                             {'container': 'all',
                              'state': True,
                              'cpu': True,
                              'mem': True,
                              'blkio': True,
                              'net': True
                             }]}
        return config

    def dependencies_installed(self):
        return True
