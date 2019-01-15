''' Base module for KochCloud cli

.. click:: cloudcli.main:main
   :prog: cloudcli
   :show-nested:

'''

from typing import Union, Tuple, List

import click
import json

from snowcli import conf
from servicenow import ServiceNow, Connection
from toolz.curried import pipe

def __convert_to_dict(tuple_set:List[Tuple[str,str]])-> dict :
	return { v[0]:v[1] for v in tuple_set }

def __create_custom_table(custom_table:str):
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

@click.option('--custom-table', 'custom', is_flag=True)
@click.option('--param', 'param', multiple=True, type=click.Tuple([str, str]))
@click.argument('action')
@click.argument('table')
@click.command()
def main(table, action, param, custom):
    ''' Command '''
    param=__convert_to_dict(param)

    try:
        pipe(
            __get_connection(),
            lambda conn: __create_custom_table(table)(conn) if \
                custom else getattr(ServiceNow, table)(conn),
            lambda snow: getattr(snow, action)(param),
            json.dumps,
            print
        )
    except AttributeError as e:
        print(e)
        #TODO Figure out how to inspect to find caller of AttrErr
        # To return valid options
        print(conf.strings['error'])
        exit(1)
    except Exception as e:
        print(e)
        print(conf.strings['error'])
        exit(1)
