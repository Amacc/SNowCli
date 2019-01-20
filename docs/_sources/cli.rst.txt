Snow CLI Commands
=================

Usage
=====

To connect to your ServiceNow instance the environment variables
**SNOW_USERNAME**, **SNOW_INSTANCE**, **SNOW_PASSWORD** are used.
The authentication used is JSONv2.


.. ***REMOVED***ck:: snow***REMOVED***.main:main
   :prog: snow***REMOVED***
   :show-nested:


**Included Tables**

    - Call
    - Change
    - Group
    - Incident
    - Journal
    - Problem
    - Request
    - Server
    - Task
    - Ticket
    - User
    - Utils

**Suported Actions**

    - create
    - create_multiple
    - delete
    - delete_multiple
    - fetch_all
    - fetch_all_by_query
    - fetch_one
    - format
    - last_updated
    - list
    - list_by_query
    - update


**Example**::

    snow***REMOVED*** Task fetch_one

    >>{
    >>    "applied": "false",
    >>    "sys_mod_count": "0",
    >>    "sys_updated_on": "2019-01-20 11:18:15",
    >>    "sys_tags": "",
    >>    "applied_date": "",
    >>    "ci_item": "e81865980a0a0aa700d60a8cd1283082",
    >>    "sys_id": "02f6c8724f032300173da88ca310c730",
    >>    "sys_updated_by": "admin",
    >>    "task": "c2f6c8724f032300173da88ca310c72f",
    >>    "sys_created_on": "2019-01-20 11:18:15",
    >>    "xml": "",
    >>    "manual_proposed_change": "false",
    >>    "sys_created_by": "admin",
    >>    "__status": "success"
    >>}

**Custom Table Example**::

    # using custom Tables
    snow***REMOVED*** incident_list.do fetch_one --custom-table --param number INC0000053

    >>{"parent": "", "made_sla": "true", ...

**Fetch Server Example**:

    snow***REMOVED*** Server fetch_one --param name Car-3

    >>{"firewall_status": "", "os_address_width": "", "operational_status":...

**Create Server Example**::

    snow***REMOVED*** Server create --param name TestServer1

    >>{"records": [{"firewall_status": "Intranet", "os_address_width": "", ...
