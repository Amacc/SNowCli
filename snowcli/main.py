''' Base module for ***REMOVED*** ***REMOVED***

.. ***REMOVED***ck:: cloud***REMOVED***.main:main
   :prog: cloud***REMOVED***
   :show-nested:

'''

from typing import Union, Tuple, List

import ***REMOVED***ck
import json

from snow***REMOVED*** import conf
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

@***REMOVED***ck.option('--custom-table', 'custom', is_flag=True)
@***REMOVED***ck.option('--param', 'param', multiple=True, type=***REMOVED***ck.Tuple([str, str]))
@***REMOVED***ck.argument('action')
@***REMOVED***ck.argument('table')
@***REMOVED***ck.command()
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
