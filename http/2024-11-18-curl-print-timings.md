# Check Latency with `curl`

You can measure the time it takes to complete a request using the `-w` (write-out) option with specific variables for timing.

## Example

```bash
curl -w "DNS lookup: %{time_namelookup}s\nConnect: %{time_connect}s\nPre-transfer: %{time_pretransfer}s\nStart-transfer: %{time_starttransfer}s\nTotal time: %{time_total}s\n" "https://httpbin.org/uuid"
```

## Example Output

```
{
  "uuid": "742b57d3-3b6d-4145-ba29-ed7d56348ccf"
}
DNS lookup: 0.090516s
Connect: 0.266375s
Pre-transfer: 0.676725s
Start-transfer: 1.326602s
Total time: 1.332040s
```

## Explanation of Timing Variables

- **DNS lookup (time_namelookup)**: Time to resolve the DNS to an IP address.
- **Connect (time_connect)**: Time to establish the TCP connection to the server.
- **Pre-transfer (time_pretransfer)**: Time from the start until the beginning of the transfer (just before the first byte).
- **Start-transfer (time_starttransfer)**: Time until the server sends the first byte (a measure of server processing).
- **Total time (time_total)**: Total time from start to finish.

## Additional Flags

If you don't care about the output and just want to obtain the timings, you can use the `-o` option to redirect output to `/dev/null`. Additionally, the `-s` (silent mode) option disables the output of additional text like progress or error messages. So if you just want the timings without anything else, use the following example:

```bash
curl -o /dev/null -s -w "Total time: %{time_total}s\n" https://httpbin.org/uuid
```