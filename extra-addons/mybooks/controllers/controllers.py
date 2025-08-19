# -*- coding: utf-8 -*-
# from odoo import http


# class .\extra-addons\mybooks(http.Controller):
#     @http.route('/.\extra-addons\mybooks/.\extra-addons\mybooks', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/.\extra-addons\mybooks/.\extra-addons\mybooks/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('.\extra-addons\mybooks.listing', {
#             'root': '/.\extra-addons\mybooks/.\extra-addons\mybooks',
#             'objects': http.request.env['.\extra-addons\mybooks..\extra-addons\mybooks'].search([]),
#         })

#     @http.route('/.\extra-addons\mybooks/.\extra-addons\mybooks/objects/<model(".\extra-addons\mybooks..\extra-addons\mybooks"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('.\extra-addons\mybooks.object', {
#             'object': obj
#         })

