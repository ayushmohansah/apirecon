from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import os

Base = declarative_base()

class Endpoint(Base):
    __tablename__ = "endpoints"

    id = Column(Integer, primary_key=True)
    url = Column(String)
    method = Column(String)
    status_code = Column(Integer)
    source = Column(String)
    content_type = Column(String)
    auth_required = Column(Boolean)

class Subdomain(Base):
    __tablename__ = "subdomains"

    id = Column(Integer, primary_key=True)
    subdomain = Column(String)
    source = Column(String)
    resolved_ip = Column(String)

class Technology(Base):
    __tablename__ = "technologies"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    confidence = Column(Integer)

class ScanMetadata(Base):
    __tablename__ = "scan_metadata"

    id = Column(Integer, primary_key=True)
    target = Column(String)
    aggressive = Column(Boolean)
    threads = Column(Integer)

class DatabaseManager:

    def __init__(self, db_path):
        self.db_path = db_path
        self.engine = None
        self.Session = None

    def initialize(self):

        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

        self.engine = create_engine(f"sqlite:///{self.db_path}")

        Base.metadata.create_all(self.engine)

        self.Session = sessionmaker(bind=self.engine)

    def insert_metadata(self, config):

        session = self.Session()

        try:
            metadata = ScanMetadata(
                target=config["target"],
                aggressive=config["aggressive"],
                threads=config["threads"]
            )

            session.add(metadata)
            session.commit()

        except SQLAlchemyError:
            session.rollback()

        finally:
            session.close()
