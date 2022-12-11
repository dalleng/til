# Lsof to get the process listening on given port

To show all networking related to a given port:

```bash
lsof -i TCP:port # port with specified protocol
lsof -i :22
```
	
-P disables port aliasing. Will show <HOST>:80 instead of <HOST>:http

```bash
lsof -P -i :port
```
