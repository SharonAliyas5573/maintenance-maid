PARSE = """{0} Given the above data, find all the parts of the machine, make it into a json and make a report of the reported issues. The report should be in the following json format!!: {{
    "machine": {{
        "name": "Machine Name",
        "parts": [
            {{
                "name": "Part Name",
                "issues": [
                    {{
                        "description": "Detailed Description including the location of the issue",
                        "severity": "Severity Level"
                        "group": "Group Name" # This is the group name of the issue, like "Electrical", "Mechanical", etc.
                    }}
                ]
            }}
        ]
    }}
}}
ONLY JSON NOthing else!!
"""


