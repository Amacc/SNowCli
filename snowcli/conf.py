import os

strings = {
    'continue?': (
        '==WARNING==\n'
        'This command will modify AWS resources.\n'
        'Do you want to continue?'),
    'error':(
        'Oops something went wrong, please check your '
        ' command and try again')
}

AUTH_METHOD = os.getenv('SNOWCLI_AUTH_METHOD','JSONv2')

USERNAME = os.getenv('SNOW_USERNAME','JSONv2')
INSTANCE = os.getenv('SNOW_INSTANCE','')
PASSWORD = os.getenv('SNOW_PASSWORD','')