from app.portal import api
from flask_restx import fields

items_schema_post = api.schema_model('Items Schema Post', {
  "MethodView": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "newData": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "example": "1"
        },
        "description": {
          "type": "string",
          "example": "test"
        },
        "rental_period": {
          "type": "string",
          "example": "test"
        },
        "prg_location": {
          "type": "string",
          "example": "test"
        },
        "equipment_type": {
          "type": "string",
          "example": "test"
        },
        "offer_until": {
          "type": "string",
          "example": "test"
        }
      },
      "required": [
        "id",
        "description",
        "rental_period",
        "prg_location",
        "equipment_type",
        "offer_until"
      ]
    }
  },
  "required": [
    "newData"
  ]
})

items_schema_put = api.schema_model('Items Schema Put', {
  "MethodView": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "newData": {
      "type": "object",
      "properties": {
        "description": {
          "type": "string",
          "example": "test"
        },
        "rental_period": {
          "type": "string",
          "example": "test"
        },
        "prg_location": {
          "type": "string",
          "example": "test"
        },
        "equipment_type": {
          "type": "string",
          "example": "test"
        },
        "offer_until": {
          "type": "string",
          "example": "test"
        }
      },
      "required": [
        "description",
        "rental_period",
        "prg_location",
        "equipment_type",
        "offer_until"
      ]
    }
  },
  "required": [
    "newData"
  ]
})