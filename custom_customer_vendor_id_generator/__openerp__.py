# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright © 2016 Techspawn Solutions. (<http://techspawn.in>).
#    Copyright (C) 2004-2015 OpenERP S.A. (<http://www.odoo.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Custom Customer Supplier ID Generator",
    'version': '1.0',
    'summary': """
        Unique ID for Customers and Suppliers.""",

    'description': """
        This module generates unique ID for Customers and Suppliers According to customers/Suppliers name as Prefix.
        Included Sequence Code for Customer and Suppliers.
    """,

    'author': "Techspawn Solutions",
    'website': "http://www.techspawn.com",
    'category': 'Others',
    'version': '0.1',
    'depends': ['base','sale','purchase'],
    'data': [
        'sequence.xml',
        'partner.xml',
    ],

}