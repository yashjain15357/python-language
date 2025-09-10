from flask import Blueprint,request , redirect, render_template ,url_for ,flash ,Response
from app import db
from app.model import ImageBlob

galary_bp = Blueprint('galary',__name__)

@galary_bp.route('/galary', methods=['GET'])
def galary():
    images = ImageBlob.query.all()   # fetch all rows from the table
    return render_template("galary.html", images=images)

@galary_bp.route('/image/<int:image_id>')
def get_image(image_id):
    image = ImageBlob.query.get_or_404(image_id)
    return Response(image.data, mimetype=image.mimetype)

@galary_bp.route('/del_img/<int:image_id>')
def del_img(image_id):
    img = ImageBlob.query.get(image_id)
    if img:
        db.session.delete(img)
        db.session.commit()
        flash("Image delete")
    else:
        flash("Image not Avaliable")
    return redirect(url_for('galary.galary'))

@galary_bp.route('/image/<int:image_id>')
def view_image(image_id):
    return 
