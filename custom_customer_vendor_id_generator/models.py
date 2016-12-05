# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Vendor_customer_id_field(models.Model):
	_inherit = 'res.partner'

	customer_id = fields.Char(string="Customer ID", readonly=False, required=False)
	supplier_id = fields.Char(string="Vendor ID", readonly=False, required=False)

	@api.model
	def create(self, data):

		sequence = self.env['ir.sequence']
		if data['customer'] == True:
			prefix = 'C'+data['name'][:1].upper()
			sequence = self.env['ir.sequence'].search([('prefix','=',prefix),('code','=','res.partner.customer')])
			if not sequence:
				padding = 4
				implementation='no_gap'
				active=True
				sequence = self.env['ir.sequence'].create({'prefix':prefix,'padding':padding,'implementation':implementation,'active':active, 'name':'Customer Id '+prefix,'code':'res.partner.customer'})
			data['customer_id'] = sequence.next_by_id()

		elif data['customer'] == False:
			prefix = 'V'+data['name'][:1].upper()
			sequence = self.env['ir.sequence'].search([('prefix','=',prefix),('code','=','res.partner.supplier')])
			if not sequence:
				padding = 4
				implementation='no_gap'
				active=True
				sequence = self.env['ir.sequence'].create({'prefix':prefix,'padding':padding,'implementation':implementation,'active':active, 'name':'Supplier Id '+prefix,'code':'res.partner.supplier'})
			data['supplier_id'] = sequence.next_by_id()

		return super(Vendor_customer_id_field, self).create(data)

	@api.multi
	def write(self, vals):

		sequence = self.env['ir.sequence']
		if 'customer_id' in vals.keys():
			prefix = 'C'+self['name'][:1].upper()
			sequence = self.env['ir.sequence'].search([('prefix','=',prefix),('code','=','res.partner.customer')])
			if not sequence:
				padding = 4
				implementation='no_gap'
				active=True
				sequence = self.env['ir.sequence'].create({'prefix':prefix,'padding':padding,'implementation':implementation,'active':active, 'name':'Customer Id '+prefix,'code':'res.partner.customer'})
			vals['customer_id'] = sequence.next_by_id()

		elif 'supplier_id' in vals.keys():
			prefix = 'V'+self['name'][:1].upper()
			sequence = self.env['ir.sequence'].search([('prefix','=',prefix),('code','=','res.partner.supplier')])
			if not sequence:
				padding = 4
				implementation='no_gap'
				active=True
				sequence = self.env['ir.sequence'].create({'prefix':prefix,'padding':padding,'implementation':implementation,'active':active, 'name':'Supplier Id '+prefix,'code':'res.partner.supplier'})
			vals['supplier_id'] = sequence.next_by_id()

		return super(Vendor_customer_id_field, self).write(vals)
