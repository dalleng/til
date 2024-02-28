# What does `real`, `user` and `sys` from the output of `time` mean?

The time command found in linux and other *nix OSes output the amount of time a program took to run.
The output is split into 3 categories, `real`, `user` and `sys`. For example:

```bash
$ time foo
real        0m0.003s
user        0m0.000s
sys         0m0.004s
```

What does `real`, `user` and `sys` mean?

- Real is wall clock time - time from start to finish of the call. This is all elapsed time including time slices used by other processes and time the process spends blocked (for example if it is waiting for I/O to complete).

- User is the amount of CPU time spent in user-mode code (outside the kernel) within the process. This is only actual CPU time used in executing the process. Other processes and time the process spends blocked do not count towards this figure.

- Sys is the amount of CPU time spent in the kernel within the process. This means executing CPU time spent in system calls within the kernel, as opposed to library code, which is still running in user-space. Like 'user', this is only CPU time used by the process. See below for a brief description of kernel mode (also known as 'supervisor' mode) and the system call mechanism.

[Source](https://stackoverflow.com/a/556411/238365)

