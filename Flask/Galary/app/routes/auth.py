from flask import Blueprint, request, render_template, Response, redirect, url_for,flash
from app import db
from app.model import ImageBlob

auth_bp = Blueprint('auth',__name__)

@auth_bp.route ('/', methods=["POST" , 'GET'])
def upload():
    if request.method=='POST':
        if 'image' not in request.files:
            flash("No file uploaded!")
            return render_template('upload.html')
        image_file = request.files.getlist('image')
        for f in image_file:
            if f.filename =="":
                continue
            new_image = ImageBlob(name = f.filename , 
                                  data = f.read() , 
                                  mimetype = f.mimetype)
            db.session.add(new_image)
        db.session.commit()
        return redirect(url_for("galary.galary"))
    return render_template('upload.html')

 