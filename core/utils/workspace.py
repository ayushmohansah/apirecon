import os
from datetime import datetime

def initialize_workspace(target):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    safe_target = target.replace("https://", "").replace("/", "_")

    scan_dir = f"scans/{safe_target}_{timestamp}"

    os.makedirs(scan_dir, exist_ok=True)

    subdirs = [
        "raw",
        "parsed",
        "reports",
        "artifacts"
    ]

    for subdir in subdirs:
        os.makedirs(os.path.join(scan_dir, subdir), exist_ok=True)

    return scan_dir
