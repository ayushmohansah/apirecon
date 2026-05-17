import json
import os

class JSONExporter:

    @staticmethod
    def export(scan_dir, filename, data):

        export_dir = os.path.join(scan_dir, "exports")

        os.makedirs(export_dir, exist_ok=True)

        filepath = os.path.join(export_dir, filename)

        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)

        return filepath
