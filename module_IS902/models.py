from odoo import models,fields

class Todo(models.Model):
    _name = "md.is902"

    name = fields.Char("Nombre")
    status = fields.Selection(selection=[("borrador","Borrador"),("hecho","Hecho")])