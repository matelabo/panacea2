# -*- coding: utf-8 -*-

from odoo import models, fields, api

 
class sit_tipo_lista_farmaco(models.Model):
     _name = 'sit_tipo_lista_farmaco'
     _rec_name = 'descripcion'
     _description = 'sit_tipo_lista_farmaco'
     codigo = fields.Integer('Código')
     numero = fields.Integer(string='Número', default='56')
     tipo_de_tabla = fields.Char(string='Tipo de tabla', default='Tipo de lista de FARMACOS')
     descripcion = fields.Char('Descripción')
     variable = fields.Char('Variable')
     importe = fields.Integer(string='Importe',default='30')

class sit_tipo_lista_alimento(models.Model):
     _name = 'sit_tipo_lista_alimento'
     _rec_name = 'descripcion'
     _description = 'sit_tipo_lista_alimento'
     codigo = fields.Integer('Código')
     numero = fields.Integer(string='Número', default='58')
     tipo_de_tabla = fields.Char(string='Tipo de tabla', default='Tipo de lista de FARMACOS')
     descripcion = fields.Char('Descripción')
     variable = fields.Char('Variable')
     importe = fields.Integer(string='Importe',default='30')

class sit_categoria_farmaco(models.Model):
     _name = 'sit_categoria_farmaco'
     _rec_name = 'descripcion'
     _description = 'sit_categoria_farmaco'
     codigo = fields.Integer('Código')
     numero = fields.Integer(string='Número', default='70')
     tipo_de_tabla = fields.Char(string='Tipo de tabla', default='CATEGORIA COMERCIAL DE CLIENTES')
     descripcion = fields.Char('Descripción')
     variable = fields.Char('Variable')
     importe = fields.Integer(string='Importe')
     
class sit_categoria_alimento(models.Model):
     _name = 'sit_categoria_alimento'
     _rec_name = 'descripcion'
     _description = 'sit_categoria_alimento'
     codigo = fields.Integer('Código')
     numero = fields.Integer(string='Número', default='72')
     tipo_de_tabla = fields.Char(string='Tipo de tabla', default='CATEGORIA DE CLIENTES DE ALIMENTOS')
     descripcion = fields.Char('Descripción')
     variable = fields.Char('Variable')
     importe = fields.Integer(string='Importe',default='0')

class sit_canales_venta(models.Model):
     _name = 'sit_canales_venta'
     _rec_name = 'descripcion'
     _description = 'sit_canales_venta'
     codigo = fields.Integer('Código')
     numero = fields.Integer(string='Número', default='3')
     tipo_de_tabla = fields.Char(string='Tipo de tabla', default='CANALES DE VENTA DE PRODUCTOS')
     descripcion = fields.Char('Descripción')
     variable = fields.Char('Variable')
     importe = fields.Integer(string='Importe',default='0')
     
class sit_telefonos_dueno(models.Model):
     _name = 'sit_telefonos_dueno'
     _rec_name = 'sit_telefono2'
     _description = 'sit_telefonos_dueno'
     sit_telefono2 = fields.Integer('Teléfonos adicionales del dueño')
     
class sit_transporte2(models.Model):
     _name = 'sit_transporte2'
     #_rec_name = 'name'
     _description = 'sit_transporte2'
     name = fields.Char('Nombre de Empresa de Transporte', required = True)
     n_de_transporte = fields.Integer('N° de transporte')
     n_de_cuit = fields.Integer('N° de CUIT')
     domicilio = fields.Char('Domicilio')
     localidad = fields.Char('Localidad')
     telefono = fields.Integer('Teléfono')
     horario_de_atencion = fields.Char('Horario de atención')
     forma_de_pago = fields.Char('Form de Pago')
     dado_de_baja = fields.Boolean('Dado de baja?')
