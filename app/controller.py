import datetime
from sqlalchemy.exc import IntegrityError, InterfaceError
from sqlalchemy import desc, func
from app.extentions import db

class AbsModel(db.Model):
    __abstract__ = True

    @property
    def fields(self):
        return self.__table__.columns

    @classmethod
    def get_next_row(cls):
        if cls.id:
            new_id = db.session.query(func.max(cls.id)).scalar() + 1
        else:
            new_id = len(cls.get_all()) + 1
        return new_id

    @classmethod
    def create(cls, **kwargs):
        if not kwargs.get('id'):
            kwargs['id'] = cls.get_next_row()

        obj = cls(**kwargs)
        try:
            db.session.add(obj)
            db.session.commit()
            return obj
        except (IntegrityError, InterfaceError) as err:
            print(err)
            db.session.rollback()
            raise Exception(f'There was an error in {cls} '
                              f'with params {kwargs} while creating record')
        except Exception as exp:
            db.session.rollback()
            raise exp.__class__

    def update(self, **kwargs):
        if 'updated_at' in self.fields.keys():
            kwargs['updated_at'] = kwargs.pop('updated_at',
                                              datetime.datetime.now())
        for field, value in kwargs.items():
            if field in set(self.fields.keys()) or field in self.Meta.fields:
                self.__setattr__(field, value)
        try:
            db.session.commit()
        except (IntegrityError, InterfaceError):
            db.session.rollback()
            raise Exception(f'There was an error in {self} '
                              f'with params {kwargs} while updating record')
        except Exception as exp:
            db.session.rollback()
            raise exp.__class__

    @classmethod
    def drop_all(cls):
        try:
            db.session.query(cls).delete()
            db.session.commit()

        except (IntegrityError, InterfaceError):
            db.session.rollback()
            raise Exception(f'There was an error in {cls} '
                              f'while deleting all records')
        except Exception as exp:
            db.session.rollback()
            raise exp.__class__

    def delete_item(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except (IntegrityError, InterfaceError):
            db.session.rollback()
            raise Exception(f'There was an error in {self} '
                              f'while deleting record')
        except Exception as exp:
            db.session.rollback()
            raise exp.__class__

    @classmethod
    def get_list(cls, sort=None, **kwrags):
        if sort:
            return list(
                cls.query.filter_by(**kwrags).order_by(desc(cls.created_at)))
        query_list = list(cls.query.filter_by(**kwrags))
        return query_list

    @classmethod
    def get(cls, **kwrags):
        query_result = cls.query.filter_by(**kwrags).first()
        return query_result

    @classmethod
    def outer_join(cls, cl1, **kwrags):
        query_result = cls.query.outerjoin(cl1, **kwrags)
        return query_result

    @classmethod
    def get_limit(cls, amount):
        return cls.query.limit(amount).all()

    @classmethod
    def get_all(cls):
        query_result = cls.query.all()
        return query_result

    def get_dict(self, meta_fields=False):
        result_dict = dict()
        fields = self.Meta.fields if meta_fields else set(self.fields.keys())
        for field in fields:
            result_dict[field] = self.__getattribute__(field)
            if isinstance(result_dict[field], datetime.datetime):
                result_dict[field] = str(result_dict[field])
        return result_dict


class ApplyQuery():
    @classmethod
    def make_query(cls, query):
        try:
            result = db.session.execute(query)
            result_as_list = result.fetchall()
        except Exception as i:
            print(i)
            return
        print(result)
        return (result_as_list)

