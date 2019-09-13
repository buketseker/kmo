# -*- coding: utf-8 -*-

from odoo import fields, models, api


class HelpdeskTicket(models.Model):
    """Extend with number field and generate it via sequence on create."""

    _inherit = 'helpdesk.ticket'

    name_no = fields.Char('No.', readonly=True)

    @api.model
    def create(self, vals):
        """Generate and return sequence number for ticket."""
        name_no = self.env['ir.sequence'].next_by_code('helpdesk.ticket.no')
        if name_no:
            vals['name_no'] = name_no
        return super(HelpdeskTicket, self).create(vals)

    @api.multi
    @api.depends('name', 'name_no')
    def name_get(self):
        """Extend to include sequence number in name."""
        res = []
        for rec in self:
            if rec.name_no:
                res.append((rec.id, "[%s] %s" % (rec.name_no, rec.name)))
            else:
                res.append((rec.id, "%s" % rec.name))
        return res
