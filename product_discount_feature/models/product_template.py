from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # discount_percentage = fields.Float(
    #     string="Discount Percentage",
    #     help="Enter the discount percentage for this product."
    # )


    discount_percentage = fields.Float(string='Discount Percentage', default=0.0)

    def _get_combination_info(self, combination, pricelist=None, parent_combination=None, only_template=False, add_qty=1, **kwargs):
        combination_info = super(ProductTemplate, self)._get_combination_info(
            combination, pricelist=pricelist, parent_combination=parent_combination, only_template=only_template, add_qty=add_qty, **kwargs
        )
        combination_info['discount_percentage'] = self.discount_percentage
        return combination_info


    @api.depends('list_price', 'discount_percentage')
    def _compute_discounted_price(self):
        for product in self:
            if product.discount_percentage > 0:
                product.discounted_price = product.list_price * (1 - (product.discount_percentage / 100))
            else:
                product.discounted_price = product.list_price

    discounted_price = fields.Float(
        string="Discounted Price",
        compute='_compute_discounted_price',
        store=True
    )

