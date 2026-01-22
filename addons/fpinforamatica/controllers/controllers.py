# -*- coding: utf-8 -*-
# from odoo import http


# class Fpinforamatica(http.Controller):
#     @http.route('/fpinforamatica/fpinforamatica', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fpinforamatica/fpinforamatica/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fpinforamatica.listing', {
#             'root': '/fpinforamatica/fpinforamatica',
#             'objects': http.request.env['fpinforamatica.fpinforamatica'].search([]),
#         })

#     @http.route('/fpinforamatica/fpinforamatica/objects/<model("fpinforamatica.fpinforamatica"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fpinforamatica.object', {
#             'object': obj
#         })

