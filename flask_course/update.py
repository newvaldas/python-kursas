from app import db, Message

antanas = Message.query.get(2)  # email pakeitimas
antanas.email = 'geras.zmogus@lrs.lt'
db.session.add(antanas)
db.session.commit()
print(Message.query.all())