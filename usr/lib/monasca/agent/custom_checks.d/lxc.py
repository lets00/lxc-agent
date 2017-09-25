#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os

import monasca_agent.collector.checks as checks

_LXC_CGROUP_PWD = '/sys/fs/cgroup'
_LXC_CGROUP_CPU_PWD = '{0}/cpu/lxc'.format(_LXC_CGROUP_PWD)
_LXC_CGROUP_CPUSET_PWD = '{0}/cpuset/lxc'.format(_LXC_CGROUP_PWD)
_LXC_CGROUP_MEM_PWD = '{0}/memory/lxc'.format(_LXC_CGROUP_PWD)

class LXC(checks.AgentCheck):

    """ Docfile """

    def check(self, instance):
        #TODO: Using log warning to view temp log
        self.log.warning("Running LXC collector...")
        self.instance = instance

        self.containers = self._containers_name()
        self.log.warning("Containers: {0}".format(str(self.containers)))
        for container_name in self.containers:
            self.dimensions = self._set_dimensions({'container_name':
                                                    container_name,
                                                    'service': 'lxc'}, self.instance)
            self._collect_cpu_metrics(container_name)
            self._collect_mem_metrics(container_name)
            #self._disk()
            #self._net()

    def _containers_name(self):
        container_name = self.instance.get('container')
        if container_name == 'all':
            return [name for name in os.listdir(_LXC_CGROUP_CPU_PWD)
                    if os.path.isdir(_LXC_CGROUP_CPU_PWD + name)]

        if os.path.isdir('{0}/{1}'.format(_LXC_CGROUP_CPU_PWD, container_name)):
            self.log.info('\tContainer name: ' + container_name)
            return [container_name]
        else:
            self.log.error('\tContainer {0} does not find'.format(container_name))
            return

    def _collect_cpu_metrics(self, container_name):
        if not self.instance.get('cpu', True):
            return
        self.log.warning('\tDimensions: '+ str(self.dimensions))
        self.log.warning('\tInstance: '+ str(self.instance))
        metrics = self._get_cpu_metrics(container_name)
        for metric, value in metrics.iteritems():
            self.log.warning('\tMetric: {0}, value: {1}'.format(metric,value))
            self.gauge(metric, value, dimensions=self.dimensions)

    def _collect_mem_metrics(self, container_name):
        if not self.instance.get('mem', True):
            return
        metrics = self._get_mem_metrics(container_name)
        for metric, value in metrics.iteritems():
            self.log.warning('\tMetric: {0}, value: {1}'.format(metric,value))
            self.gauge(metric, value, dimensions=self.dimensions)

    def _collect_net_metrics(self, container_name):
        if not self.instance.get('net', True):
            return
        metrics = self._get_net_metrics(container_name)
        for metric, value in metrics.iteritems():
            self.log.warning('\tMetric: {0}, value: {1}'.format(metric,value))
            self.gauge(metric, value, dimensions=self.dimensions)

    def _get_cpu_metrics(self, container_name):
        cpu_cgroup = '{0}/{1}/'.format(_LXC_CGROUP_CPU_PWD, container_name)
        cpuset_cgroup = '{0}/{1}/'.format(_LXC_CGROUP_CPUSET_PWD, container_name)
        metrics = {}

        metrics['cpuacct.usage'] = int(open(cpu_cgroup + 'cpuacct.usage', 'r')\
                                      .readline().rstrip('\n'))
        # CPUs that container can use
        #metrics['cpuset.cpus'] = open(cpuset_cgroup + 'cpuset.cpus', 'r')\
        #                              .readline().rstrip('\n')
        cpuacct_usage_percpu = open(cpu_cgroup + 'cpuacct.usage_percpu' , 'r')\
                                    .readline().rstrip(' \n').split(' ')
        for cpu in range(len(cpuacct_usage_percpu)):
            metrics['cpuacct.usage_percpu.cpu{0}'.format(cpu)] = int(cpuacct_usage_percpu[cpu])

        cpu_file = open(cpu_cgroup + 'cpuacct.stat', 'r').read().split('\n')
        metrics_stat = self._get_metrics_by_file(cpu_cgroup + 'cpuacct.stat', 'cpuacct')
        metrics.update(metrics_stat)
        return metrics

    def _get_mem_metrics(self, container_name):
        mem_cgroup = '{0}/{1}/'.format(_LXC_CGROUP_MEM_PWD, container_name)
        metrics = self._get_metrics_by_file(mem_cgroup + 'memory.stat', 'memory')
        return metrics

    def _get_net_metrics(self, container_name):
        pass

    def _get_metrics_by_file(self, filename, pre_key):
        metrics = {}
        with open(filename, 'r') as cgroup_file:
            for line in cgroup_file:
                resource_post_key, resource_value = line.split(' ')
                resource_key = '{0}.{1}'.format(pre_key,resource_post_key)
                metrics[resource_key] = int(resource_value)
        return metrics
