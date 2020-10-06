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

import click
from terminaltables import SingleTable

from core.helper import get_request, safe_load_texts
from core.print_formatters import print_err_response


TEXTS = safe_load_texts()


@click.group()
def sgx_cli():
    pass


@sgx_cli.group('sgx', help="SGX commands")
def sgx():
    pass


@sgx.command(help="Info about connected SGX server")
def info():
    status, payload = get_request('sgx_info')
    if status == 'ok':
        data = payload
        table_data = [
            ['SGX info', ''],
            ['Server URL', data['sgx_server_url']],
            ['SGXWallet Version', data['sgx_wallet_version']],
            ['Node SGX keyname', data['sgx_keyname']],
            ['Status', data['status_name']]
        ]
        table = SingleTable(table_data)
        print(table.table)
    else:
        print_err_response(payload)
