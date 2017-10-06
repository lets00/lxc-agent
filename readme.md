## LXC

An agent that provides LXC cgroup data. This agent does not required sudo.

Requirements:
  * lxc

Sample config:

```
init_config:

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
| ... | hostname, container_name, service=lxc | ... |
| net.rx.bytes | hostname, container_name, service=lxc, iface | number of received bytes |
| net.rx.packets | hostname, container_name, service=lxc, iface | number of received packets |
| net.rx.errs | hostname, container_name, service=lxc, iface | number of received error packets |
| net.rx.drop | hostname, container_name, service=lxc, iface | number of received dropped packets |
| net.rx.fifo | hostname, container_name, service=lxc, iface | number of received fifo packets |
| net.rx.frame | hostname, container_name, service=lxc, iface | number of received frame packets |
| net.rx.compressed | hostname, container_name, service=lxc, iface| number of received compressed bytes |
| net.rx.multicast | hostname, container_name, service=lxc, iface | number of received multicast packets |
| net.tx.bytes | hostname, container_name, service=lxc, iface| number of transfered bytes |
| net.tx.packets | hostname, container_name, service=lxc, iface | number of transfered packets |
| net.tx.errs | hostname, container_name, service=lxc, iface | number of transfered error packets |
| net.tx.drop | hostname, container_name, service=lxc, iface | number of transfered dropped packets |
| net.tx.fifo | hostname, container_name, service=lxc, iface | number of transfered fifo packets |
| net.tx.frame | hostname, container_name, service=lxc, iface | number of transfered frame packets |
| net.tx.compressed | hostname, container_name, service=lxc, iface| number of transfered compressed bytes |
| net.tx.multicast | hostname, container_name, service=lxc, iface | number of transfered multicast packets |
