# -*- coding: utf-8 -*-
{
    'name': "Order Line Serial Number",

    'summary': """
        Adds Serial Numbers to Order Lines""",

    'description': """
        This Module Adds Serial Numbers to order Lines in Sales orders and in Purchase orders Dynamically After the Products added and Saved.
    """,

    'author': "Techspawn Solutions",
    'website': "http://www.techspawn.com",

    'category': 'Others',
    'version': '0.1',

    'depends': ['base', 'sale', 'purchase'],
    
    'images': [
        'images/main.jpg',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
}
