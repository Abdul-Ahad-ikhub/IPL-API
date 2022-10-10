from db import db

#Database Table Contents
class GameTable(db.Model):
    __tablename__ = "game"

    id            = db.Column(db.Integer, primary_key=True)
    host_team_id  = db.Column(db.Integer, db.ForeignKey('teams.id'))
    guest_team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    date          = db.Column(db.String(100),nullable = False)
    targetscore   = db.Column(db.String(100),nullable = False)
    result        = db.Column(db.String(100),nullable = False)
         

#Functions and Properties
class GameAccess(object):
    @property
    def games(self):
        return GameTable.query.all()

    def get(self, id):
        game = GameTable.query.filter_by(id=id).first()
        if game:
            return {
                "id"            : GameTable.id, 
                "host_team_id"  : GameTable.host_team_id,
                "guest_team_id" : GameTable.guest_team_id,
                "date"          : GameTable.date,
                "targetscore"   : GameTable.targetscore,
                "result"        :GameTable.result
                }
        else: print('Game record not found')

    def create(self, data):
        game = GameTable(
            host_team_id  = data['host_team_id'],
            guest_team_id = data['guest_team_id'],
            date          = data['date'],
            targetscore   = data['targetscore'],
            result        = data['result']
            )      
        db.session.add(game)
        db.session.commit()
        return game

    def update(self, id, data):
        game = GameTable.query.filter_by(id=id).first()
        game.host_team_id  = data['host_team_id'],
        game.guest_team_id = data['guest_team_id'],
        game.date          = data['date'],
        game.targetscore   = data['targetscore'],
        game.result        = data['result']
        db.session.commit()
        return game

    def delete(self, id):
        game = GameTable.query.filter_by(id=id).first()
        db.session.delete(game)
        db.session.commit()