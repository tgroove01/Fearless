import datetime
import logging
import json

from urllib.request import ssl, socket


log_var = logging.getLogger(__name__)


def check_ssl_cert(hostname: str, port: str) -> dict:
    """
    This function is check ssl certificate
    :param hostname:
    :param port:
    :return:
    """
    create_default_context = ssl.create_default_context()

    try:
        with socket.create_connection(address=(hostname, port), timeout=3) as sock:
            with create_default_context.wrap_socket(sock, server_hostname=hostname) as ssock:
                certs = ssock.getpeercert()

        certExp = datetime.datetime.strptime(
            certs['notAfter'], '%b %d %H:%M:%S %Y %Z')

        data = {
            'status': 200,
            'expiration_day': f"{certExp.year}-{certExp.month}-{certExp.day}",
            'remaining_day': (certExp - datetime.datetime.now()).days
        }
    except Exception as e:
        log_var.error(e)
        data = {
            'status': 500,
            'message': 'Server Error! Try again or contact admin.'
        }

    return data


def lambda_handler(event, context):
    """
    Check SSL Service
    :param event:
    :param context:
    :return:
    """
    request_body = json.dumps(event.get('body'))
    #print(event.keys())
    print(request_body)
    hostname = request_body.find('hostname')
    print(hostname)
    port = request_body.find('port', 443)
    print(port)

    if not hostname:
       return {'ok': False, 'message': 'Wrong request parameters.'}
    print(check_ssl_cert)
    return check_ssl_cert(hostname=hostname, port=str(port))
   

   
