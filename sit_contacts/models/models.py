# -*- coding: utf-8 -*-

# from odoo import models, fields, api
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from odoo.tools.translate import _
from dateutil.relativedelta import relativedelta


class sit_contacts(models.Model):
#     _name = 'sit_contacts.sit_contacts'
     _inherit = 'res.partner'
     _description = 'sit_contacts.sit_contacts'
     sit_nro_cliente = fields.Integer(string="Nro de Cliente")
     sit_nombre_fantasia = fields.Text(string="Nombre de Fantasía")
     
     sit_categoria_farmacos  = fields.Many2many('sit_categoria_farmaco', 'tipo_rel', 'categoria_id', 'sit_categoria_farmaco_id', string='Categoria FARMACOS')
     sit_categoria_alimentos  = fields.Many2many('sit_categoria_alimento', 'tipo_al_rel', 'categoria_al_id', 'sit_categoria_alimento_id', string='Categoria ALIMENTOS')
     
     sit_canal_de_venta  = fields.Many2many('sit_canales_venta', 'tipo_canvent_rel', 'canales_id', 'sit_canales_venta_id', string='Canales de Venta')
# grupo facturacion
     sit_contado_anticipado = fields.Selection([('S','Si'), ('N','No')],default='S',string='Contado Anticipado', tracking=True)
     control_tarifa=fields.Char()
     control_deuda_atras = fields.Selection([('S','Si'), ('N','No')],default='S',string='Control deuda atrás', tracking=True)
     control_tope_de_cr = fields.Selection([('S','Si'), ('N','No')],default='',string='Control tope de Crédito', tracking=True)
     credit_limit = fields.Float('Monto Establecido')
#     sit_codigo_iva
# grupo usuario 
     sit_dado_de_baja = fields.Selection([('S','Dado de baja'), ('N','Está vigente')],default='',string='Dato de Baja?', tracking=True)
     sit_field_rlgKm = fields.Char('rlgKm')
# grupo usuario 
     sit_website_user = fields.Selection([('W','Es usuario Web'), ('N','No es usuario web')],default='N',string='Es usuario web?', tracking=True)
# grupo facturacion
     sit_factura_rc = fields.Selection([('S','Si'), ('N','No')],default='S',string='.Factura RC', tracking=True)
     sit_fecha_alic_cero_caba = fields.Date('Fecha alicuota Cero CABA')
     sit_fecha_de_alta = fields.Date(string='Fecha de Alta', default='')
     sit_problemas_de_cuit = fields.Selection([('S','Sin problemas'), ('P','Con problemas')],default='S',string='.Problemas de CUIT', tracking=True)
     sit_fecha_de_verificacion =  fields.Date(string='Fecha de verificación', default='')
     sit_fecha_de_vencimiento_verificacion =  fields.Date(string='Fecha de Vencimiento de verificación', default='')

     sit_fecha_de_ultima_compra_farmacos =  fields.Date(string='Fecha de Ultima compra de Fármacos', default='')
     sit_fecha_de_ultima_compra_alimentos =  fields.Date(string='Fecha de última compra de Alimentos', default='')

     sit_fecha_desde =  fields.Date(string='Fecha desde: ')
     sit_fecha_hasta =  fields.Date(string='Fecha hasta: ')
     sit_fecha_desde_recup =  fields.Date(string='Fecha desde: ')
     sit_fecha_hasta_recup =  fields.Date(string='Fecha hasta: ')
# grupo facturacion
     sit_fecha_exento_arba =  fields.Date(string='Fecha Exento ARBA')
     sit_gln_senasa = fields.Char('GLN Senasa')
     sit_gln_senasa_fecha =  fields.Date(string='GLN Senasa Fecha')

     sit_meta_objetivo = fields.Char('Meta objetivos')
     sit_n_ingresos_brutos = fields.Integer('Nro Ingresos Brutos')
     sit_observaciones = fields.Text('Observaciones')
     sit_porc_aplic_alicuota = fields.Char('Porc aplicado alicuota')
     sit_porc_de_descuento = fields.Char('Porc. de descuento')
     sit_porc_exento_arba = fields.Integer('Porcentaje exento ARBA')
     sit_problemas_cobranza_farmacos = fields.Selection([('S','Si'), ('N','No')],default='N',string='Problema de cobranza FARMACOS', tracking=True)
     sit_problemas_cobranza_farmacos_date =  fields.Date(string='Fecha Prob Framacos')
     sit_problemas_cobranza_alimentos = fields.Selection([('S','Si'), ('N','No')],default='N',string='Problema de cobranza ALIMENTOS', tracking=True)
     sit_problemas_cobranza_alimentos_date =  fields.Date(string='Fecha Prob Alimentos')

     sit_tipo_de_lista_farmaco = fields.Many2many('sit_tipo_lista_farmaco', 'tipo_list_f_rel', 'lista_farm_id', 'sit_tipo_lista_farmaco_id', string='Tipo de Lista FARMACOS')
     sit_tipo_de_lista_alimentos = fields.Many2many('sit_tipo_lista_alimento', 'tipo_list_a_rel', 'lista_alim_id', 'sit_tipo_lista_alimento_id', string='Tipo de Lista ALIMENTOS')

     sit_tipo_de_sociedad = fields.Selection([('H','Es Hombre'), ('M','Es Mujer'), ('S','Es Sociedad')],default='',string='Tipo de Sociedad', tracking=True)
     sit_transporte = fields.Char('Transporte')
     sit_transportes = fields.Many2many('sit_transporte2', 'tipo_transp_rel', 'lista_transp_id', 'sit_transporte_id', string='Transporte(s)')
     sit_dueno_regente = fields.Selection([('dueno','Dueño'), ('regente','Regente')], default='dueno', string='¿Dueño o Regente?', tracking=True)
# grupo dueño - regente
     sit_telefonos_adicionales = fields.Many2many('sit_telefonos_dueno', 'telefono_rel', 'tel_contact_id', 'telefon_id', string='Teléfonos adicionales')
     sit_correo2 = fields.Char('Correo electrónico 2')
     sit_habilitado = fields.Selection([('S','Si'), ('N','No')],default='S',string='Está Habilitado?', tracking=True)
     
# grupo dueño

# grupo regente
     sit_matrícula = fields.Char('Mátricula')
     sit_habilitacion_min = fields.Char('Habilitación Mínima')
     sit_cant_veterinarios_con_rt = fields.Char('Cantidad de veterinarios con RT')


# class sit_contacts(models.Model):
#     _name = 'sit_contacts.sit_contacts'
      # _inherit = "res.partner"
      # _description = 'sit_contacts.sit_contacts'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

