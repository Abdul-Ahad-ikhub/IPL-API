from model.player import PlayerTable,PlayerAccess
from flask_restplus import Namespace, Resource, fields

#NameSpace Defination
api = Namespace('player_api',description = "Manage all CRUD operation performed on Player Table")

#API Model Definations
player_api = api.model('Player', {
    'id'      : fields.Integer(readOnly=True, description='Player ID'),
    'name'    : fields.String(required=True, description='Player Name '),
    'skill'   : fields.String(required=True, description='Player Skill'),
    'team_id' : fields.String(required=True,description = 'Team refernce ID')
})

#Object Declarations
obj_2 = PlayerAccess()

#Endpoints for Player Model
@api.route('/')
class player_list(Resource):
    @api.doc('list_players')
    @api.marshal_list_with(player_api)
    def get(self):
        '''List all Players in the Database'''
        return obj_2.players

    @api.doc('create_player')
    @api.expect(player_api)
    @api.marshal_with(player_api, code=201)
    def post(self):
        '''Create a Player'''
        return obj_2.create(api.payload), 201


@api.route('/<int:id>')
@api.response(404, 'Player not Found')
@api.param('id', 'Player ID')
class player_operation(Resource):
    
    @api.doc('get_player')
    @api.marshal_with(player_api)
    def get(self, id):
        '''Get a Player information with its ID'''
        return obj_2.get(id)

    @api.doc('delete_player')
    @api.response(204, 'Player Deleted')
    def delete(self, id):
        '''Delete a Player with its ID'''
        obj_2.delete(id)
        return '', 204

    @api.expect(player_api)
    @api.marshal_with(player_api)
    def put(self, id):
        '''Update a Player information with its ID'''
        return obj_2.update(id, api.payload)


