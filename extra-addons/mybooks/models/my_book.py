from odoo import models, fields, api


class Book(models.Model):
    _name = "my_books.book"
    _description = "My Book"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Name", required=True, default="New", tracking=True)
    author = fields.Char(string="Author", required=True)
    editable_date = fields.Date(string="Date", required=True, default=fields.Date.today)
    description = fields.Text(string="Description")
    image = fields.Image(string="Image")

    date_publication = fields.Date(
        string="Date of publication",
        help="Date of publication of the book",
        groups="purchase.group_purchase_manager",
    )

    type_book = fields.Selection(
        selection=[
            ("fantasy", "Fantaisie"),
            ("adventure", "Aventure"),
            ("medical", "Médical"),
        ],
        string="Type de livre",
        default="medical",
        required=True,
    )

    author_new = fields.Many2one("res.partner", string="Author", required=True)

    author_3 = fields.Many2many(
        comodel_name="res.partner",
        relation="book_partner_author_rel",
        column1="book_id",
        column2="partner_id",
        string="Auteurs",
        required=True,
    )

    contact = fields.Many2many(
        comodel_name="res.partner",
        relation="book_partner_contact_rel",
        column1="book_id",
        column2="partner_id",
        string="Contacts",
        required=True,
    )

    status = fields.Selection(
        selection=[
            ("draft", "Brouillon"),
            ("in_progress", "En cours"),
            ("done", "Terminé"),
            ("cancel", "Annulé"),
        ],
        string="Statut",
        default="draft",
        tracking=True,
    )

    book_sales_count = fields.Integer(
        string="Nombre de ventes", compute="_compute_book_sales_count",store= True
    )

    @api.depends()  # on peut ajouter des champs dépendants si besoin
    def _compute_book_sales_count(self):
        for book in self:
            book.book_sales_count = 10  # valeur fixe temporaire pour test

    def afficherId(self):
        for record in self:
            print("This is the ID ", record.id)
        # for book in self:
        #     _logger = self.env["ir.logging"]
        #     _logger.info(f"ID du livre : {book.id}")

    def action_view_book_sales(self):
        self.ensure_one()
        return {
            "name": "Lignes de vente du livre",
            "type": "ir.actions.act_window",
            "view_mode": "tree,form",
            "res_model": "sale.order.line",
            "domain": [("product_id.product_tmpl_id", "=", self.id)],
            "context": {"default_product_id": self.id},
        }
    def action_set_in_progress(self):
        for record in self:
            record.status = "in_progress"
    def action_set_done(self):
        for record in self:
            record.status = "done"
    def action_cancel(self):
        for record in self:
            record.status = 'cancel'
 
