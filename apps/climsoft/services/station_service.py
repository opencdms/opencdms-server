import logging
from typing import List
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as models
from apps.climsoft.schemas import station_schema


logger = logging.getLogger("ClimsoftStationService")
logging.basicConfig(level=logging.INFO)


class FailedCreatingStation(Exception):
    pass


class FailedGettingStation(Exception):
    pass


class FailedGettingStationList(Exception):
    pass


class FailedUpdatingStation(Exception):
    pass


class FailedDeletingStation(Exception):
    pass


class StationDoesNotExist(Exception):
    pass


def create(db_session: Session, data: station_schema.CreateStation) -> station_schema.Station:
    try:
        station = models.Station(**data.dict())
        db_session.add(station)
        db_session.commit()
        return station_schema.Station.from_orm(station)
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        raise FailedCreatingStation("Failed creating station.")


def get(db_session: Session, station_id: str) -> station_schema.Station:
    try:
        station = db_session.query(models.Station).filter_by(stationId=station_id).first()

        if not station:
            raise StationDoesNotExist("Station does not exist.")

        return station_schema.Station.from_orm(station)
    except StationDoesNotExist:
        raise
    except Exception as e:
        logger.exception(e)
        raise FailedGettingStation("Failed getting station.")


def query(
        db_session: Session,
        station_id: str = None,
        station_name: str = None,
        wmoid: str = None,
        icaoid: str = None,
        latitude: float = None,
        longitude: float = None,
        qualifier: str = None,
        elevation: str = None,
        geolocation_method: str = None,
        geolocation_accuracy: str = None,
        opening_datetime: str = None,
        closing_datetime: str = None,
        country: str = None,
        authority: str = None,
        admin_region: str = None,
        drainage_basin: str = None,
        waca_selection: bool = None,
        cpt_selection: bool = None,
        station_operational: bool = None,
        limit: int = 25,
        offset: int = 0
) -> List[station_schema.Station]:
    try:
        q = db_session.query(models.Station)

        if station_id is not None:
            q = q.filter_by(stationId=station_id)

        if station_name is not None:
            q = q.filter_by(stationName=station_name)

        if wmoid is not None:
            q = q.filter_by(wmoid=wmoid)

        if icaoid is not None:
            q = q.filter_by(icaoid=icaoid)

        if latitude is not None:
            q = q.filter(models.Station.latitude >= latitude)

        if longitude is not None:
            q = q.filter(models.Station.longitude >= longitude)

        if qualifier is not None:
            q = q.filter(models.Station.qualifier.ilike(f"%{qualifier}%"))

        if elevation is not None:
            q = q.filter(models.Station.elevation.ilike(f"%{elevation}%"))

        if geolocation_accuracy is not None:
            q = q.filter(models.Station.geoLocationAccuracy >= geolocation_accuracy)

        if geolocation_method is not None:
            q = q.filter(models.Station.geoLocationMethod.ilike(f"%{geolocation_method}%"))

        if opening_datetime is not None:
            q = q.filter(models.Station.openingDatetime >= opening_datetime)

        if closing_datetime is not None:
            q = q.filter(models.Station.closingDatetime >= closing_datetime)

        if country is not None:
            q = q.filter_by(contry=country)

        if authority is not None:
            q = q.filter_by(authority=authority)

        if admin_region is not None:
            q = q.filter_by(adminRegion=admin_region)

        if drainage_basin is not None:
            q = q.filter_by(drainageBasin=drainage_basin)

        if waca_selection is not None:
            q = q.filter_by(wacaSelection=waca_selection)

        if cpt_selection is not None:
            q = q.filter_by(cptSelection=waca_selection)

        if station_operational is not None:
            q = q.filter_by(stationOperational=waca_selection)

        return [station_schema.Station.from_orm(s) for s in q.offset(offset).limit(limit).all()]
    except Exception as e:
        logger.exception(e)
        raise FailedGettingStationList("Failed getting station list.")


def update(db_session: Session, station_id: str, updates: station_schema.UpdateStation) -> station_schema.Station:
    try:
        db_session.query(models.Station).filter_by(stationId=station_id).update(updates.dict())
        db_session.commit()
        updated_station = db_session.query(models.Station).filter_by(stationId=station_id).first()
        return station_schema.Station.from_orm(updated_station)
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        raise FailedUpdatingStation("Failed updating station")


def delete(db_session: Session, station_id: str) -> bool:
    try:
        db_session.query(models.Station).filter_by(stationId=station_id).delete()
        db_session.commit()
        return True
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        raise FailedDeletingStation("Failed deleting station.")




