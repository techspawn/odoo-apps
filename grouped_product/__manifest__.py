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
    'images': ['static/description/main.jpg'],
    'category': 'Custom',
    'version': '1.0',
    'depends': ['base', 'sale_management'],

    'data': [
        'views/product_group_view.xml'
    ],

}
