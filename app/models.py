from . import db 
#from flask import Flask, request

#db = Flask(__name__)
class Properties(db.Model):

     __tablename__ = 'properties'

     propertyid = db.Column(db.Integer, primary_key=True)
     Title = db.Column(db.String(180),nullable=False)
     Location = db.Column(db.String(280),nullable=False)
     No_Room = db.Column(db.Integer,nullable=False)
     No_Bathrooms = db.Column(db.Integer,nullable=False)
     Price = db.Column(db.Integer,nullable=False)
     Property_Type = db.Column(db.String(15))
     Description = db.Column(db.String(800))
     Photo = db.Column(db.String(255),nullable=False)


     def __init__(self,Title, Location,No_Bathrooms,No_Room, Price,Property_Type,Description,Photo):
         self.Title = Title 
         self.Location = Location
         self.No_Bathrooms = No_Bathrooms
         self.No_Room = No_Room
         self.Price = Price  
         self.Property_Type = Property_Type
         self.Photo= Photo
         self.Description = Description