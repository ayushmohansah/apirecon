import os
from jinja2 import Template

HTML_TEMPLATE = """
<html>
<head>
<title>APIX Recon Report</title>
</head>
<body>
<h1>APIX Reconnaissance Report</h1>

<h2>Findings</h2>

<ul>
{% for finding in findings %}
<li>
<strong>{{ finding }}</strong>
</li>
{% endfor %}
</ul>

</body>
</html>
"""

class HTMLReporter:

    @staticmethod
    def generate(scan_dir, findings):

        report_dir = os.path.join(scan_dir, "reports")

        os.makedirs(report_dir, exist_ok=True)

        template = Template(HTML_TEMPLATE)

        rendered = template.render(findings=findings)

        output_path = os.path.join(report_dir, "report.html")

        with open(output_path, "w") as file:
            file.write(rendered)

        return output_path
