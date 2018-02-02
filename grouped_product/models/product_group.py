# -*- coding: utf-8 -*-

from odoo import models, fields, api


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
