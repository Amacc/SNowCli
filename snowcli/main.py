''' Base module for cli

.. click:: snowcli.main:main
   :prog: snowclli
   :show-nested:

'''

from typing import Tuple, List

import json
import click

from toolz.curried import pipe
from servicenow import ServiceNow, Connection
from snowcli import conf

def __convert_to_dict(tuple_set: List[Tuple[str, str]])-> dict:
    return {v[0]:v[1] for v in tuple_set}

def __create_custom_table(custom_table: str):
    def _out(conn):
        custom = ServiceNow.Base(conn)
        custom.__table__ = custom_table
        return custom
    return _out

# TODO: Allow toggle in the future
def __get_connection():
    # conn = Connection.Auth(
    #     username=conf.USERNAME, password=conf.PASSWORD,
    #     instance=conf.INSTANCE)
    return Connection.Auth(
        username=conf.USERNAME, password=conf.PASSWORD,
        instance=conf.INSTANCE, api='JSONv2')

@click.option('--custom-table', 'custom', is_flag=True,
              help="Used to interact with data in custom table")
@click.option('--param', 'param', multiple=True, type=click.Tuple([str, str]),
              help="Used to pass paramaters to the servicenow query.")
@click.argument('action')
@click.argument('table')
@click.command()
def main(table, action, param, custom):
    ''' Documentation: https://amacc.github.io/SNowCli/ '''
    param = __convert_to_dict(param)

    try:
        pipe(
            __get_connection(),
            lambda conn: __create_custom_table(table)(conn) if \
                custom else getattr(ServiceNow, table)(conn),
            lambda snow: getattr(snow, action)(param),
            json.dumps,
            print
        )
    except AttributeError as err:
        print(err)
        #TODO Figure out how to inspect to find caller of AttrErr
        # To return valid options
        print(conf.strings['error'])
        exit(1)
    except Exception as err: #pylint: disable=W0703
        print(err)
        print(conf.strings['error'])
        exit(1)
