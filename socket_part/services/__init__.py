from .auth_deals import authentication
from .query_deals import get_query_values
from .rooms_deals import get_room


def log_print(**kwargs):
    from pprint import pprint
    print('***********')
    for key, value in kwargs.items():
        if isinstance(value, dict):
            print(f'{key=}')
            pprint(value)
        else:
            print(f'{key} {value}')
        print('------------------')
    print('***********')
