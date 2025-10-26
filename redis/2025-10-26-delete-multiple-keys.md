# Delete multiple keys in redis

This is mainly for dev. Do not use in prod as `keys` blocks redis.

`redis-cli keys 'pattern' | xargs redis-cli del`

✅ Safe for production (uses SCAN)

Redis’ SCAN command iterates over keys incrementally. You can combine it with xargs:

`redis-cli --scan --pattern 'pattern' | xargs -r -L 100 redis-cli del`

- `-r` avoids xargs on empty input
- `-L` call utility in batches 