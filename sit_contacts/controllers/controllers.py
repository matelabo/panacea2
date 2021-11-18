# -*- coding: utf-8 -*-
# from odoo import http


# class SitContacts(http.Controller):
#     @http.route('/sit_contacts/sit_contacts/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sit_contacts/sit_contacts/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sit_contacts.listing', {
#             'root': '/sit_contacts/sit_contacts',
#             'objects': http.request.env['sit_contacts.sit_contacts'].search([]),
#         })

#     @http.route('/sit_contacts/sit_contacts/objects/<model("sit_contacts.sit_contacts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sit_contacts.object', {
#             'object': obj
#         })
