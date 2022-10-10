from sqlalchemy.orm import relationship
from sqlalchemy.orm.relationships import foreign
from db import db

#Database Table Contents
class InjuryTable(db.Model):
    __tablename__ = "injury"

    id          = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(1000),nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id')) #Realtion with Player Table (one to one)(Child Table = Injury_Table , Parent_Table = Player_Table)


#Functions and Properties
class InjuryAccess(object):
    @property
    def injuries(self):
        return InjuryTable.query.all()

    def get(self, id):
        injury = InjuryTable.query.filter_by(id=id).first()
        if injury:
            return {
                "id"          : InjuryTable.id, 
                "description" : InjuryTable.description,
                "player_id"   : InjuryTable.player_id
                }
        else: print('Injury not found')

    def create(self, data):
        injury = InjuryTable(
            description = data['description'],
            player_id   = data['player_id']
            )      
        db.session.add(injury)
        db.session.commit()
        return injury

    def update(self, id, data):
        injury = InjuryTable.query.filter_by(id=id).first()
        injury.description = data['description'],
        injury.player_id   = data['player_id']
        db.session.commit()
        return injury

    def delete(self, id):
        injury = InjuryTable.query.filter_by(id=id).first()
        db.session.delete(injury)
        db.session.commit()