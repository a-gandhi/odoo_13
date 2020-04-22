# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sale Extension',
    'category': 'Tools',
    'version': '13.0.1.0.0',
    'sequence': 1,
    'author': 'Ankit H Gandhi',
    'summary': 'Manage Draft Customer and Approved to Customer',
    'description':
        """
This module cover below points
===============================
* When create customer using (create and edit) option from sale order. A new customer appear on 'Draft Customer' menu.
* Once draft customer Approved by Administrator then moved to 'Customer' menu.
        """,
    'depends': ['sale_management'],
    'data': [
        'views/sale_views.xml',
        'views/res_partner_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
