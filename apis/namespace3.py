from flask_restplus import Namespace, Resource, fields
from model.position import PositionTable,PositionAccess

#NameSpace Defination
api = Namespace('position_api',description = "Manage all CRUD operation performed on Position Table")

#API Model Definations
position_api = api.model('Position', {
    'id'            : fields.Integer(readOnly=True, description='Position ID'),
    'position_name' : fields.String(required=True, description='Position Name of the Player'),
    'player_id'     : fields.String(required=True, description= 'Player ID reference')
})

#Object Declarations
obj_3 = PositionAccess()

#Endpoints for Position Model
@api.route('/')
class position_list(Resource):
    @api.doc('list_positions')
    @api.marshal_list_with(position_api)
    def get(self):
        '''List all Position in the Database'''
        return obj_3.positions

    @api.doc('create_position')
    @api.expect(position_api)
    @api.marshal_with(position_api, code=201)
    def post(self):
        '''Create a Position'''
        return obj_3.create(api.payload), 201


@api.route('/<int:id>')
@api.response(404, 'Position not Found')
@api.param('id', 'Position ID')
class position_operation(Resource):
    
    @api.doc('get_position')
    @api.marshal_with(position_api)
    def get(self, id):
        '''Get a Positon information with its ID'''
        return obj_3.get(id)

    @api.doc('delete_position')
    @api.response(204, 'Position Deleted')
    def delete(self, id):
        '''Delete a Position with its ID'''
        obj_3.delete(id)
        return '', 204

    @api.expect(position_api)
    @api.marshal_with(position_api)
    def put(self, id):
        '''Update a Position information with its ID'''
        return obj_3.update(id, api.payload)


