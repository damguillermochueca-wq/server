# -*- coding: utf-8 -*-
from odoo import models, fields

class Empresa(models.Model):
    _name = 'fpinformatica.empresa'
    _description = 'Empresa Colaboradora'

    name = fields.Char(string="Nombre", required=True)
    cif = fields.Char(string="CIF", required=True)
    contact_person = fields.Char(string="Persona de contacto", required=True)
    phone = fields.Char(string="Teléfono", required=True)
    email = fields.Char(string="Correo electrónico", required=True)
    address = fields.Char(string="Dirección", required=True)
    
    # Relación One2many hacia alumnos
    student_ids = fields.One2many('fpinformatica.alumno', 'company_id', string="Alumnos en prácticas")