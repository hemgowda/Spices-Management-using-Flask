from flask_wtf import Form 
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField 
from wtforms import validators, ValidationError 
from flask import Flask, render_template, request, flash
 
class ContactForm(Form): 
 name = SelectField('name', choices = [('black pepper', 'black pepper'),('cardamom', 'cardamom'),('cloves', 'cloves'),('ginger powder', 'ginger powder'),('mustard seeds', 'mustard seeds'),])
 price = SelectField('price', choices = [('20', '20'),('50', '50'),('100', '100'),('500', '500'),])   
 no_of_packs = TextField("no_of_packs",[validators.Required("Please enter required field")])
 Quality = SelectField('Quality', choices = [('first', 'first'),('second', 'second'),('original', 'original'),('high', 'high'),])
 origin = SelectField('origin', choices = [('india', 'india'),('germany', 'germany'),('china', 'china'),('pakistan', 'pakistan'),])
 submit = SubmitField("Submit") 