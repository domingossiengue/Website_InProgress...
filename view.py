from flask import Blueprint # use blueprint to separe the files
from flask import render_template 
class viewall:
    def __init__(self, view):
        self.view= view

    view = Blueprint('view', __name__) # defining a blueprint 


    @view.route('/') # when we go to the slash rout it will take us to the bellow code Home 
    def home(self):
        return render_template("home.html")