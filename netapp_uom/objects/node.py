from netapp_uom.objects.base import NetApp_UOM_ObjectBase

class NetApp_UOM_Node(NetApp_UOM_ObjectBase):
    """
    Class representing a single NetApp node.
    """
    def __init__(self, object_json):
        super().__init__(object_json)
