# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    """ Added new Is Draft Customer boolean type field """
    is_draft_customer = fields.Boolean(string='Is Draft Customer ?')

    @api.model
    def create(self, vals):
        """
            - Create Draft Customer when using 'create and edit' from sale order
        """
        if self.env.context.get('from_create_edit'):
            vals.update({'customer_rank': 0, 'is_draft_customer': True})
        partner = super(ResPartner, self).create(vals)
        return partner

    def get_approved_draft_customer(self):
        """
            - Approved Draft Customer to Customer by Administrator
        """
        for partner in self:
            partner.write({'is_draft_customer': False})
            partner._increase_rank('customer_rank')
