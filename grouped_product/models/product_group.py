# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright © 2016 Techspawn Solutions. (<http://techspawn.in>).
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

from openerp import models, fields, api


class grouped_product(models.Model):

    '''
    extra fields required for grouped_product added
    '''
    _inherit = 'product.template'

    grouped = fields.Boolean(
        string="Grouped", help="Group product can contain multiple product")
    parent_id = fields.Many2one(
        comodel_name='product.template', string='Parent Product', domain=[('grouped', '=', True)])
    group_product = fields.One2many(
        comodel_name='product.template', string='Group IDS', inverse_name='parent_id', readonly=False, required=False,)
