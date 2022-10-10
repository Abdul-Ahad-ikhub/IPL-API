from flask_restplus import Api

from .namespace1 import api as ns1
from .namespace2 import api as ns2
from .namespace3 import api as ns3
from .namespace4 import api as ns4
from .namespace5 import api as ns5


api = Api( 
		  version = "1.0", 
		  title = "IPL Database", 
		  description = "Manage all the IPL Teams,Playes,Games related Databse"
)


api.add_namespace(ns1)
api.add_namespace(ns2)
api.add_namespace(ns3)
api.add_namespace(ns4)
api.add_namespace(ns5)








