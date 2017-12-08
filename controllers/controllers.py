# -*- coding: utf-8 -*-
from odoo import http

# class CustomSalesReports(http.Controller):
#     @http.route('/custom_sales_reports/custom_sales_reports/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_sales_reports/custom_sales_reports/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_sales_reports.listing', {
#             'root': '/custom_sales_reports/custom_sales_reports',
#             'objects': http.request.env['custom_sales_reports.custom_sales_reports'].search([]),
#         })

#     @http.route('/custom_sales_reports/custom_sales_reports/objects/<model("custom_sales_reports.custom_sales_reports"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_sales_reports.object', {
#             'object': obj
#         })