# Use a file to specify the http payload with curl

```shell
$ cat query.json
{"foo": "bar"}

$ curl -X POST -H "Content-Type: application/json" -H "Accept: application/json" https://httpbin.org/post --data-binary @query.json
{
  "args": {},
  "data": "{\"foo\": \"bar\"}\n",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "application/json",
    "Content-Length": "15",
    "Content-Type": "application/json",
    "Host": "httpbin.org",
    "User-Agent": "curl/8.7.1",
    "X-Amzn-Trace-Id": "Root=1-67fbcfb6-417ccb074ddf1ed41b114fa6"
  },
  "json": {
    "foo": "bar"
  },
  "origin": "181.94.226.181",
  "url": "https://httpbin.org/post"
}
```