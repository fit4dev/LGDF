# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Le Gout du Frais',
    'category': 'Inventory',
    'summary': 'The specific and easy-to-use system in Odoo allows addons features on the web.',
    'description': """ The specific and easy-to-use system in Odoo allows addons features on the web. """,
    'depends': [
        'base',
        'product',
        'point_of_sale'
    ],
    'data': [
        'views/product_template_form_inherited.xml',
        'views/view_report_pos_order_pivot_inherited.xml',
    ],
    'qweb': [
        'static/src/xml/Screens/ReceiptScreen/OrderReceiptExtended.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
