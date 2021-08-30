import json

from flask import request
from flask_restx import Resource
from app.portal.models import ITEMS_SCHEMA, Items
# from app.portal.swagger_schemas import items_schema_put, items_schema_post


class ItemsAPI(Resource):
    def get(self, *args, **kwargs):
        items = ITEMS_SCHEMA.dump(Items.get_list())
        return items, 200

    # @api.expect(items_schema_put)
    def put(self, *args, **kwargs):
        request_params = json.loads(request.data)
        items_data = request_params.get('newData')
        description = items_data.get('description')
        rental_period = items_data.get('rental_period')
        prg_location = items_data.get('prg_location')
        equipment_type = items_data.get('equipment_type')
        offer_until = items_data.get('offer_until')
        new_item = Items()
        new_item.create(description=description, rental_period=rental_period, prg_location=prg_location,
                        equipment_type=equipment_type, offer_until=offer_until)

    # @api.expect(items_schema_post)
    def post(self, *args, **kwargs):
        request_params = json.loads(request.data)
        items_data = request_params.get('newData')
        item_id = items_data.get('id')
        description = items_data.get('description')
        rental_period = items_data.get('rental_period')
        prg_location = items_data.get('prg_location')
        equipment_type = items_data.get('equipment_type')
        offer_until = items_data.get('offer_until')
        item = Items.qury.filter_by(id=item_id).one_or_none()
        item.update(id=item_id, description=description, rental_period=rental_period, prg_location=prg_location,
                    equipment_type=equipment_type, offer_until=offer_until)
        return 'ok', 200

    def delete(self, *args, **kwargs):
        request_params = json.loads(request.data)
        item_id = request_params.get('id')
        item = Items.query.filter_by(id=item_id).one_or_none()
        item.delete_item()
        return 'ok', 200