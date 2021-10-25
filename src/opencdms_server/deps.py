from sqlalchemy.orm.session import Session
from opencdms_server.db import SessionLocal


def get_session():
    """
    Api dependency to provide database session to a request
    """
    session: Session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
    finally:
        session.close()
