from urllib.parse import parse_qs


def get_query_values(environ: dict, needed_params: tuple) -> dict:
    query = environ['QUERY_STRING']
    # print(query)
    resp_dict = dict()
    parsed_q = parse_qs(query)
    for i in needed_params:
        parsed = parsed_q.get(i)
        if isinstance(parsed, (list, tuple)) and len(parsed):
            parsed = parsed[0]
        resp_dict[i] = parsed
    # print(resp_dict)
    return resp_dict
