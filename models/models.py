# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools import amount_to_text_en

class CustomInvoice(models.Model):
	_inherit = 'account.invoice'

	@api.multi
	def amount_to_text(self, amount, currency):
		convert_amount = amount_to_text_en.amount_to_text(amount,lang='en',currency='Pesos')
		return convert_amount