There is an Apache-style access log at `/app/access.log`.

Create a JSON report at `/app/report.json` with exactly these fields:

- `total_requests`: the number of non-empty log lines in `/app/access.log`.
- `unique_ips`: the number of distinct client IP addresses. The client IP is the first whitespace-separated field on each non-empty log line.
- `top_path`: the request path that appears most often inside the quoted HTTP request, such as `/index.html`.

For the provided input file, the correct report is:

```json
{"total_requests": 6, "unique_ips": 3, "top_path": "/index.html"}
```

Do not include extra fields in the JSON output.
