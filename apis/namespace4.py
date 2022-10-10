from flask_restplus import Namespace, Resource, fields
from model.injury import InjuryTable,InjuryAccess

#NameSpace Defination
api = Namespace('injury_api',description = "Manage all CRUD operation performed on Injury Table")

#API Model Definations
injury_api = api.model('Injury', {
    'id'          : fields.Integer(readOnly=True, description='Injury ID'),
    'description' : fields.String(required=True, description='Description of the Injury'),
    'player_id'   : fields.String(required=True, description= 'Player ID reference')
})

#Object Declarations
obj_4 = InjuryAccess()

#Endpoints for Injury Model
@api.route('/')
class injury_list(Resource):
    @api.doc('list_injuries')
    @api.marshal_list_with(injury_api)
    def get(self):
        '''List all Injuries in the Database'''
        return obj_4.injuries

    @api.doc('create_injury')
    @api.expect(injury_api)
    @api.marshal_with(injury_api, code=201)
    def post(self):
        '''Create a Injury'''
        return obj_4.create(api.payload), 201


@api.route('/<int:id>')
@api.response(404, 'Injury not Found')
@api.param('id', 'Injury ID')
class injury_operation(Resource):
    
    @api.doc('get_injury')
    @api.marshal_with(injury_api)
    def get(self, id):
        '''Get an Injury information with its ID'''
        return obj_4.get(id)

    @api.doc('delete_injury')
    @api.response(204, 'Injury Deleted')
    def delete(self, id):
        '''Delete an Injury with its ID'''
        obj_4.delete(id)
        return '', 204

    @api.expect(injury_api)
    @api.marshal_with(injury_api)
    def put(self, id):
        '''Update an Injury information with its ID'''
        return obj_4.update(id, api.payload)

