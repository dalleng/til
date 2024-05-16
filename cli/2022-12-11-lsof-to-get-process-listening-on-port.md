# Lsof to get the process listening on a given port

To show all networking related to a given port:

```bash
lsof -i TCP:port # port with specified protocol
lsof -i :22
```
	
`-P` disables port aliasing. Will show <HOST>:80 instead of <HOST>:http

```bash
lsof -P -i :port
```

`-p` lets you specify a given pid. In the following example, we would get
all TCP connections opened by process with process id `<pid>`. 

`-a` makes
all conditions specified by the different flags be ANDed.

```bash
lsof -i TCP -P -a -p <pid>
```
