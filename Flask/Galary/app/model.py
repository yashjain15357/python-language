from app import db

class ImageBlob(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)  # original filename
    data = db.Column(db.LargeBinary, nullable=False)  # stores actual image bytes
    mimetype = db.Column(db.String(50), nullable=False)  # e.g., "image/png"
