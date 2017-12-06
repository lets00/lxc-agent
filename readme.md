## LXC

An agent that provides LXC cgroup data. This agent does not require sudo.

Requirements:
  * lxc

Sample config:

```
init_config:

instances:
    - container: all
      cpu: True
      mem: True
      swap: True
      blkio: True
      net: True
```

The LXC checks return the following metrics:

| Metric Name | Dimensions | Semantics |
| ----------- | ---------- | --------- |
| blkio.read | hostname, container_name, service=lxc | number of bytes read from the disk to the cgroup(container) |
| blkio.write | hostname, container_name, service=lxc | number of bytes written from the cgroup(container) to the disk |
| blkio.async | hostname, container_name, service=lxc | number of asynchronous bytes |
| blkio.sync | hostname, container_name, service=lxc | number of synchronous bytes |
| blkio.total | hostname, container_name, service=lxc | total number of bytes |
| cpuacct.usage | hostname, container_name, service=lxc | reports the total CPU time (in nanoseconds) consumed |
| cpuacct.usage_percpu.cpu{X} | hostname, container_name, service=lxc | reports the total CPU time (in nanoseconds) consumed by cpu X |
| cpuacct.user |  hostname, container_name, service=lxc| CPU time consumed by tasks in user mode. Unit defined by the USER_HZ variable |
| cpuacct.system |  hostname, container_name, service=lxc| CPU time consumed by tasks in kernel mode. Unit defined by the USER_HZ variable |
| memory.cache | hostname, container_name, service=lxc | page cache, including *tmpfs* (shmem), in bytes |
| memory.rss | hostname, container_name, service=lxc | anonymous and swap cache, not including tmpfs (shmem), in bytes |
| memory.mapped_file| hostname, container_name, service=lxc | size of memory-mapped mapped files, including tmpfs (shmem), in bytes |
| memory.pgpgin | hostname, container_name, service=lxc | number of pages paged into memory |
| memory.pgpgout | hostname, container_name, service=lxc | number of pages paged out of memory |
| memory.swap | hostname, container_name, service=lxc | swap usage in bytes |
| memory.active_anon | hostname, container_name, service=lxc | anonymous and swap cache on LRU list, in bytes |
| memory.inactive_anon | hostname, container_name, service=lxc | anonymous and swap cache on inactive LRU list, in bytes |
| memory.active_file | hostname, container_name, service=lxc | file-backed memory on active LRU list, in bytes |
| memory.inactive_file | hostname, container_name, service=lxc | file-backed memory on inactive LRU list, in bytes |
| memory.unevictable | hostname, container_name, service=lxc | memory that cannot be reclaimed, in bytes |
| memory.hierarchical_memory_limit | hostname, container_name, service=lxc | memory limit for the hierarchy that contains the memory cgroup, in bytes |
| memory.hierarchical_memsw_limit | hostname, container_name, service=lxc | memory plus swap limit for the hierarchy that contains the memory cgroup, in bytes |
| memory.usage_in_bytes | hostname, container_name, service=lxc | memory usage, in bytes |
| memory.memsw.usage_in_bytes | hostname, container_name, service=lxc | swap memory usage, in bytes |
| net.rx.bytes | hostname, container_name, service=lxc, iface | number of received bytes |
| net.rx.packets | hostname, container_name, service=lxc, iface | number of received packets |
| net.rx.errs | hostname, container_name, service=lxc, iface | number of received error packets |
| net.rx.drop | hostname, container_name, service=lxc, iface | number of received dropped packets |
| net.rx.fifo | hostname, container_name, service=lxc, iface | number of received fifo packets |
| net.rx.frame | hostname, container_name, service=lxc, iface | number of received frame packets |
| net.rx.compressed | hostname, container_name, service=lxc, iface| number of received compressed bytes |
| net.rx.multicast | hostname, container_name, service=lxc, iface | number of received multicast packets |
| net.tx.bytes | hostname, container_name, service=lxc, iface| number of transferred bytes |
| net.tx.packets | hostname, container_name, service=lxc, iface | number of transferred packets |
| net.tx.errs | hostname, container_name, service=lxc, iface | number of transferred error packets |
| net.tx.drop | hostname, container_name, service=lxc, iface | number of transferred dropped packets |
| net.tx.fifo | hostname, container_name, service=lxc, iface | number of transferred fifo packets |
| net.tx.frame | hostname, container_name, service=lxc, iface | number of transferred frame packets |
| net.tx.compressed | hostname, container_name, service=lxc, iface| number of transferred compressed bytes |
| net.tx.multicast | hostname, container_name, service=lxc, iface | number of transferred multicast packets |
| running_containers| hostname, service=lxc | number of running containers |
