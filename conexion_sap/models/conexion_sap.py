# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError
import requests

class ConexionSap(models.TransientModel):
    _name = "conexion.sap"
    _description = "Conexion SAP"

    @api.multi
    def action_conexion_sap(self,val):
        #self.ensure_one()
        #if not self.move_lines and not self.move_line_ids:
        #raise UserError(_('Please add some items to move.'))
        url = 'http://54.39.106.92:9002/api/OdooSAP/GenerarEntradaCalidad'
        params = dict(
            ids= val,
            token= '66DrmLKRG7'
        )
        resp = requests.get(url=url, params=params)
        data = resp.json()
        if data['results'] != 'OK.' and data['results'] != 'Tranferencia Interna':
            raise UserError(_(data['results']))
        return True
