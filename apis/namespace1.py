from model.team import TeamTable,TeamAccess
from flask_restplus import Namespace, Resource, fields

#NameSpace Defination
api = Namespace('team_api',description = "Manage all CRUD operation performed on Teams Table")

#API Model Definations
team_api = api.model('Teams', {
    'id'          : fields.Integer(readOnly=True, description='Team ID'),
    'team_name'   : fields.String(required=True, description='Team Name '),
    'team_coach'  : fields.String(required=True, description='Team Coach'),
    'team_captain': fields.String(required=True, description='Team Captain')
})

#Object Declarations
obj_1 = TeamAccess()

#Endpoints for Team Model
@api.route('/')
class team_list(Resource):
    @api.doc('list_teams')
    @api.marshal_list_with(team_api)
    def get(self):
        '''List all Teams in the Database'''
        return obj_1.teams

    @api.doc('create_team')
    @api.expect(team_api)
    @api.marshal_with(team_api, code=201)
    def post(self):
        '''Create a Team'''
        return obj_1.create(api.payload), 201


@api.route('/<int:id>')
@api.response(404, 'Team not Found')
@api.param('id', 'Team ID')
class team_operation(Resource):
    
    @api.doc('get_team')
    @api.marshal_with(team_api)
    def get(self, id):
        '''Get a Team information with its ID'''
        return obj_1.get(id)

    @api.doc('delete_team')
    @api.response(204, 'Team Deleted')
    def delete(self, id):
        '''Delete a Team with its ID'''
        obj_1.delete(id)
        return '', 204

    @api.expect(team_api)
    @api.marshal_with(team_api)
    def put(self, id):
        '''Update a Team information with its ID'''
        return obj_1.update(id, api.payload)


