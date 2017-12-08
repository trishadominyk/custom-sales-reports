# -*- coding: utf-8 -*-
from odoo import api, models, _
from odoo.exceptions import UserError

class CollectionReport(models.AbstractModel):
	_name = 'report.account.report_invoice_cr'

	@api.model
	def render_html(self, docids, data=None):
		print "oh hai"
		Report = self.env['report']
		PosOrder = self.env['pos.order']
		ids_to_print = []
		invoiced_posorders_ids = []
		selected_orders = PosOrder.browse(docids)
		print docids
		print selected_orders
		for order in selected_orders.filtered(lambda o: o.invoice_id):
		# for order in selected_orders:
			ids_to_print.append(order.invoice_id.id)
			invoiced_posorders_ids.append(order.id)
		print ids_to_print
		not_invoiced_orders_ids = list(set(docids) - set(invoiced_posorders_ids))
		if not_invoiced_orders_ids:
			not_invoiced_posorders = PosOrder.browse(not_invoiced_orders_ids)
			not_invoiced_orders_names = list(map(lambda a: a.name, not_invoiced_posorders))
			raise UserError(_('No link to an invoice for %s.') % ', '.join(not_invoiced_orders_names))

		return Report.sudo().render('custom_sales_reports.report_collection', {'docs': self.env['account.invoice'].sudo().browse(ids_to_print)})

	# @api.model
	# def render_html(self, docids, data=None):
	# 	report_obj = self.env['report']
	# 	# PosOrder = self.env['pos.order']
	# 	report = report_obj._get_report_from_name('account.report_invoice_cr')
	# 	docargs = {
	# 		'doc_ids': docids,
	# 		'doc_model': report.model,
	# 		'docs': self,
	# 	}
	# 	return report_obj.render('account.report_invoice_cr', docargs)