from core.database.db import Endpoint, Technology

class EndpointRepository:

    def __init__(self, db_manager):
        self.db = db_manager

    def insert_endpoint(self, endpoint_data):

        session = self.db.Session()

        endpoint = Endpoint(
            url=endpoint_data.get("url"),
            method=endpoint_data.get("method", "GET"),
            status_code=endpoint_data.get("status_code"),
            source=endpoint_data.get("source", "unknown"),
            content_type=endpoint_data.get("content_type", "unknown"),
            auth_required=endpoint_data.get("auth_required", False)
        )

        session.add(endpoint)
        session.commit()
        session.close()

class TechnologyRepository:

    def __init__(self, db_manager):
        self.db = db_manager

    def insert_technology(self, technology_name, confidence=80):

        session = self.db.Session()

        tech = Technology(
            name=technology_name,
            confidence=confidence
        )

        session.add(tech)
        session.commit()
        session.close()
