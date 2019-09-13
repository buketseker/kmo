# -*- coding: utf-8 -*-
# Author: Paulius Stundžia. Copyright: JSC Boolit.
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Helpdesk Ticket Sequence',
    'version': '1.0.0',
    'category': 'Helpdesk',
    'summary': 'helpdesk, sequence',
    'description': """
    Implement sequence for helpdesk tickets.
    """,
    'author': 'Boolit',
    'website': 'www.boolit.eu',
    'depends': [
        'helpdesk'
    ],
    'data': [
        'views/helpdesk_ticket_views.xml',
        'data/sequence.xml',
    ],
    'license': 'LGPL-3',
}
