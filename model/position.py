from sqlalchemy.orm import relationship
from sqlalchemy.orm.relationships import foreign
from db import db

#Database Table Contents
class PositionTable(db.Model):
    __tablename__ = "position"

    id            = db.Column(db.Integer, primary_key=True)
    position_name = db.Column(db.String(100),nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id')) #Relationship with Player Table (one to one)(Child Table = Position_Table , Parent Table = Player_Table)

   
   

         

#Functions and Properties
class PositionAccess(object):
    @property
    def positions(self):
        return PositionTable.query.all()

    def get(self, id):
        position = PositionTable.query.filter_by(id=id).first()
        if position:
            return {
                "id"            : PositionTable.id, 
                "position_name" : PositionTable.position_name,
                "player_id"     : PositionTable.player_id
                }
        else: print('Position not found')

    def create(self, data):
        position = PositionTable(
            position_name = data['position_name'],
            player_id     = data['player_id']
            )      
        db.session.add(position)
        db.session.commit()
        return position

    def update(self, id, data):
        position = PositionTable.query.filter_by(id=id).first()
        position.position_name = data['position_name'],
        position.player_id     = data['player_id']
        db.session.commit()
        return position

    def delete(self, id):
        position = PositionTable.query.filter_by(id=id).first()
        db.session.delete(position)
        db.session.commit()