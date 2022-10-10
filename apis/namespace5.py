from flask_restplus import Namespace, Resource, fields
from model.game import GameTable,GameAccess

#NameSpace Defination
api = Namespace('game_api',description = "Manage all CRUD operation performed on Game Table")

#API Model Definations
game_api = api.model('Game', {
    'id'         : fields.Integer(readOnly=True, description='Game ID'),
    'host_team_id'  : fields.String(Required=True, description='Host Team ID'),
    'guest_team_id' : fields.String(Required=True, description='Gueat Team ID'),
    'date'       : fields.String(required=True, description='Date when the game was played'),
    'targetscore'      : fields.String(required=True, description='Target set by the 1st inning completion'),
    'result' :fields.String(Required=True,description='Final result of the match')
})

#Object Declarations
obj_5 = GameAccess()

#Endpoints for Game Model
@api.route('/')
class game_list(Resource):
    @api.doc('list_games')
    @api.marshal_list_with(game_api)
    def get(self):
        '''List all Game Events in the Database'''
        return obj_5.games

    @api.doc('create_game')
    @api.expect(game_api)
    @api.marshal_with(game_api, code=201)
    def post(self):
        '''Create a Game Event'''
        return obj_5.create(api.payload), 201


@api.route('/<int:id>')
@api.response(404, 'Game not Found')
@api.param('id', 'Game ID')
class game_operation(Resource):
    
    @api.doc('get_game')
    @api.marshal_with(game_api)
    def get(self, id):
        '''Get a Game Event information with its ID'''
        return obj_5.get(id)

    @api.doc('delete_game')
    @api.response(204, 'Game Deleted')
    def delete(self, id):
        '''Delete a Game Event with its ID'''
        obj_5.delete(id)
        return '', 204

    @api.expect(game_api)
    @api.marshal_with(game_api)
    def put(self, id):
        '''Update a Game Event information with its ID'''
        return obj_5.update(id, api.payload)

