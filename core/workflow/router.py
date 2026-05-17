class WorkflowRouter:

    @staticmethod
    def determine_modules(target_info):

        modules = {
            "passive": True,
            "amass": True,
            "nmap": True,
            "httpx": True,
            "swagger": True,
            "graphql": True,
            "javascript": True
        }

        if target_info["is_local"] or target_info["is_private_ip"]:
            modules["passive"] = False
            modules["amass"] = False

        return modules
