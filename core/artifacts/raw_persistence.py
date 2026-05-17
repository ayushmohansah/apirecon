import os

class RawArtifactPersistence:

    @staticmethod
    def write(scan_dir, name, content):

        output_dir = os.path.join(scan_dir, 'raw')

        os.makedirs(output_dir, exist_ok=True)

        filepath = os.path.join(output_dir, name)

        with open(filepath, 'w', encoding='utf-8', errors='ignore') as file:
            file.write(content)

        return filepath
