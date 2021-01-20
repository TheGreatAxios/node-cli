#   -*- coding: utf-8 -*-
#
#   This file is part of node-cli
#
#   Copyright (C) 2019 SKALE Labs
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging

import click

from tools.helper import abort_if_false
from core.wallet import get_wallet_info, send_eth

logger = logging.getLogger(__name__)


@click.group()
def wallet_cli():
    pass


@wallet_cli.group('wallet', help="Node wallet commands")
def wallet():
    pass


@wallet.command('info', help="Get info about SKALE node wallet")
@click.option('--format', '-f', type=click.Choice(['json', 'text']))
def wallet_info(format):
    get_wallet_info(format)


@wallet.command('send', help="Send ETH from SKALE node wallet to address")
@click.argument('address')
@click.argument('amount', type=float)
@click.option('--gas-limit', type=int, default=None,
              help='Gas limit value for transaction')
@click.option('--gas-price', type=int, default=None,
              help='Gas price value in Gwei for transaction')
@click.option('--yes', is_flag=True, callback=abort_if_false,
              expose_value=False,
              prompt='Are you sure you want to send ETH tokens?')
def send(address, amount, gas_limit, gas_price):
    send_eth(address, amount, gas_limit, gas_price)
