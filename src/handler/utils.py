def parse_query(queries: list[str]):
    ql: dict[str, str] = {}

    for q in queries:
        name, value = q.split("=", 1)
        ql[name] = value

    return ql


def parse_request(request: str):
    split = request.split()

    query_split = split[1].split("?")
    query = query_split[1].split("&") if len(query_split) > 1 else []
    return split[0].lstrip("b'"), query_split[0], query


def response(status: str, body: str = ""):
    return f"HTTP/1.0 {status}\r\nContent-Type: text/text\r\n\r\n", body
