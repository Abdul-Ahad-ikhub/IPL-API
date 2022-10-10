from sqlalchemy.orm import backref, relationship
from sqlalchemy.orm.relationships import foreign
from db import db

#Database Table Contents
class TeamTable(db.Model):
    __tablename__ = "teams"

    id           = db.Column(db.Integer, primary_key=True)
    team_name    = db.Column(db.String(100),nullable=False)
    team_coach   = db.Column(db.String(100),nullable=False)
    team_captain = db.Column(db.String(100),nullable=False)
    player = db.relationship('PlayerTable' , backref='teams' , cascade='all,delete,delete-orphan')#Realtionship with player table (one to many)(Parent Table = Team_Table , Child Table = Player_Table)
    hostteam = db.relationship('GameTable' , backref='teams1' , cascade='all,delete,delete-orphan'  , uselist=False , foreign_keys="[GameTable.host_team_id]")#Relationship with game table (one to one )(Parent Table  = Team_Table , Child Table  = Game Table)
    guestteam = db.relationship('GameTable' , backref='teams2' , cascade='all,delete,delete-orphan' , uselist=False , foreign_keys="[GameTable.host_team_id]")#Relationship with game table (one to one )(Parent Table  = Team_Table , Child Table  = Game Table)


#Functions and Properties
class TeamAccess(object):
    @property
    def teams(self):
        return TeamTable.query.all()

    def get(self, id):
        team = TeamTable.query.filter_by(id=id).first()
        if team:
            return {
                "id"           : TeamTable.id, 
                "team_name"    : TeamTable.team_name,
                "team_coach"   : TeamTable.team_coach,
                "team_captain" : TeamTable.team_captain
                }
        else: print('Team not found')

    def create(self, data):
        team = TeamTable(
            team_name    = data['team_name'],
            team_coach   = data['team_coach'],
            team_captain = data['team_captain']
            )      
        db.session.add(team)
        db.session.commit()
        return team

    def update(self, id, data):
        team = TeamTable.query.filter_by(id=id).first()
        team.team_name    = data['team_name'],
        team.team_coach   = data['team_coach'],
        team.team_captain = data['team_captain']
        db.session.commit()
        return team

    def delete(self, id):
        team = TeamTable.query.filter_by(id=id).first()
        db.session.delete(team)
        db.session.commit()