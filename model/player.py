from sqlalchemy.orm import backref, relation, relationship
from sqlalchemy.orm.relationships import foreign
from db import db

#Database Table Contents
class PlayerTable(db.Model):
    __tablename__ = "players"

    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(100),nullable=False)
    skill   = db.Column(db.String(100),nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))#Relationship with Team Table (many to one)(Child Table = Player_Table ,Parent Table = Team_Table)
    position = db.relationship('PositionTable' , backref = 'players' , cascade = 'all,delete,delete-orphan' , uselist = False)#Relation with Position Table (one to one)(Parent Table = Player_table , Child Table = Position_Table)
    injury = db.relationship('InjuryTable' , backref = 'players' , cascade = 'all,delete,delete-orphan' , uselist = False)#Relationship with Injury Table (one to one)(Parent Table = Player_Table , Child Table = Injury_Table)

    

    
    
     

#Functions and Properties
class PlayerAccess(object):
    @property
    def players(self):
        return PlayerTable.query.all()

    def get(self, id):
        player = PlayerTable.query.filter_by(id=id).first()
        if player:
            return {
                "id"      : PlayerTable.id, 
                "name"    : PlayerTable.name,
                "skill"   : PlayerTable.skill,
                "team_id" : PlayerTable.team_id
                }
        else: print('Player not found')

    def create(self, data):
        player = PlayerTable(
            name    = data['name'],
            skill   = data['skill'],
            team_id = data['team_id']
            )      
        db.session.add(player)
        db.session.commit()
        return player

    def update(self, id, data):
        player = PlayerTable.query.filter_by(id=id).first()
        player.name  = data['name'],
        player.skill = data['skill'],
        player.team_id = data['team_id']
        db.session.commit()
        return player

    def delete(self, id):
        player = PlayerTable.query.filter_by(id=id).first()
        db.session.delete(player)
        db.session.commit()