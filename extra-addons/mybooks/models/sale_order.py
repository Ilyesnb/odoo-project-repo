from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"
    bl = fields.Char(string="Bon de commande Client")  
