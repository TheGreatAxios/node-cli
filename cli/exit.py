import click
import logging
from core.helper import get_request, post_request, abort_if_false
from core.print_formatters import print_err_response, print_exit_status
from tools.texts import Texts

logger = logging.getLogger(__name__)
TEXTS = Texts()
BLUEPRINT_NAME = 'exit'


@click.group()
def exit_cli():
    pass


@exit_cli.group('exit', help="Exit commands")
def node_exit():
    pass


@node_exit.command('start', help="Start exiting process")
@click.option('--yes', is_flag=True, callback=abort_if_false,
              expose_value=False,
              prompt='Are you sure you want to destroy your SKALE node?')
def start():
    status, payload = post_request(
        blueprint=BLUEPRINT_NAME,
        method='start'
    )
    if status == 'ok':
        msg = TEXTS['exit']['start']
        logger.info(msg)
        print(msg)
    else:
        print_err_response(payload)


@node_exit.command('status', help="Get exit process status")
@click.option('--format', '-f', type=click.Choice(['json', 'text']))
def status(format):
    status, payload = get_request(
        blueprint=BLUEPRINT_NAME,
        method='status'
    )
    if status == 'ok':
        exit_status = payload
        if format == 'json':
            print(exit_status)
        else:
            print_exit_status(exit_status)
    else:
        print_err_response(payload)


@node_exit.command('finalize', help="Finalize exit process")
def finalize():
    pass
