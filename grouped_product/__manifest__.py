# -*- coding: utf-8 -*-
{
    'name': "Product  Bundle",

    'summary': """
        Module is used to create grouped product in odoo.""",

    'description': """
        This module is used to create group which will contain multiple product of similar/disimilar type.
    """,

    'author': "Techspawn Solutions",
    'website': "http://www.techspawn.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Custom',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'views/product_group_view.xml'
    ],

}
