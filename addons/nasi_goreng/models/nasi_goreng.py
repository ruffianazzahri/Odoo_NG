from odoo import models, fields

class NasiGoreng(models.Model):
    _name = 'nasi.goreng'
    _description = 'Model Nasi Goreng'
    _rec_name = 'name' 

    name = fields.Char(string="Nama", required=True)
    price = fields.Float(string="Harga")
    ingredients = fields.Text(string="Bahan")
    spicy_level = fields.Selection([
        ('kurang pedas', 'Kurang Pedas'),
        ('medium', 'Medium'),
        ('hot', 'Hot'),
    ], string="Level Pedas")

    # Pastikan record bisa diedit
    def write(self, values):
        return super(NasiGoreng, self).write(values)
