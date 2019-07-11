import click
from readsettings import ReadSettings

from cli import __version__
from cli.schains import schains_cli
from cli.containers import containers_cli
from cli.logs import logs_cli
from cli.node import node_cli

from core.helper import login_required, safe_load_texts, local_only
from core.config import CONFIG_FILEPATH
from core.wallet import get_wallet_info
from core.user import register_user, login_user, logout_user, show_registration_token
from core.host import test_host, show_host, fix_url, reset_host


config = ReadSettings(CONFIG_FILEPATH)
TEXTS = safe_load_texts()


@click.group()
def cli():
    pass


@cli.command('version', help="Show SKALE node CLI version")
@click.option('--short', is_flag=True)
def version(short):
    if short:
        print(__version__)
    else:
        print(f'SKALE Node CLI version: {__version__}')


@cli.command('attach', help="Attach to remote SKALE node")
@click.argument('host')
@click.option('--skip-check', is_flag=True)
def attach(host, skip_check):
    host = fix_url(host)
    if not host: return
    if test_host(host) or skip_check:
        config['host'] = host
        print(f'SKALE host: {host}')
    else:
        print(TEXTS['service']['node_host_not_valid'])


@cli.command('host', help="Get SKALE node endpoint")
@click.option('--reset', is_flag=True)
def host(reset):
    if reset:
        reset_host(config)
        return
    show_host(config)


@cli.group('user', help="SKALE node user commands")
def user():
    pass


@user.command('token', help="Show registration token if avaliable. Server-only command.")
@local_only
def user_token():
    show_registration_token()


@user.command('register', help="Create new user for SKALE node")
@click.option(
    '--username', '-u',
    prompt="Enter username",
    help='SKALE node username'
)
@click.option(
    '--password', '-p',
    prompt="Enter password",
    help='SKALE node password',
    hide_input=True
)
@click.option(
    '--token', '-t',
    prompt="Enter one-time token",
    help='One-time token',
    hide_input=True
)
def register(username, password, token):
    register_user(config, username, password, token)


@user.command('login', help="Login user in a SKALE node")
@click.option(
    '--username', '-u',
    prompt="Enter username",
    help='SKALE node username'
)
@click.option(
    '--password', '-p',
    prompt="Enter password",
    help='SKALE node password',
    hide_input=True
)
def login(username, password):
    login_user(config, username, password)


@user.command('logout', help="Logout from SKALE node")
def logout():
    logout_user(config)


@cli.group('wallet', help="Node wallet commands")
def wallet():
    pass


@wallet.command('info', help="Get info about SKALE node wallet")
@click.option('--format', '-f', type=click.Choice(['json', 'text']))
@login_required
def wallet_info(format):
    get_wallet_info(config, format)


if __name__ == '__main__':
    cmd_collection = click.CommandCollection(
        sources=[cli, schains_cli, containers_cli, logs_cli, node_cli])
    cmd_collection()
