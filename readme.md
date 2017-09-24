## LXC

An agent that provides LXC cgroup data.

Requirements:
  * lxc

Sample config:

```
init_config:
    humanize: yes

instances:
    - container: all
      state: True
      cpu: True
      mem: True
      blkio: True
      net: True
```

The LXC checks return the following metrics:

| Metric Name | Dimensions | Semantics |
| ----------- | ---------- | --------- |
|  | hostname, container_name, service=lxc |  |
| cpuacct.usage | hostname, container_name, service=lxc | reports the total CPU time (in nanoseconds) consumed |
| cpuacct.usage_percpu.cpu{X} | hostname, container_name, service=lxc | reports the total CPU time (in nanoseconds) consumed by cpu X |
| cpuacct.user |  hostname, container_name, service=lxc| CPU time consumed by tasks in user mode. Unit defined by the USER_HZ variable |
| cpuacct.system |  hostname, container_name, service=lxc| CPU time consumed by tasks in kernel mode. Unit defined by the USER_HZ variable |
| memory.cache | hostname, container_name, service=lxc | page cache, including *tmpfs* (shmem), in bytes |
| memory.rss | hostname, container_name, service=lxc | anonymous and swap cache, not including tmpfs (shmem), in bytes |
| memory.mapped_file| hostname, container_name, service=lxc | size of memory-mapped mapped files, including tmpfs (shmem), in bytes |
| memory.pgpgin | hostname, container_name, service=lxc | number of pages paged into memory |
| memory.pgpgout | hostname, container_name, service=lxc | number of pages paged out of memory |
