"""`1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?`"""

import groq
import json
import prompts
import json
import re

def parse_json_from_string(s):
    try:
        data = json.loads(s)
        print(data)
        return data
    except json.JSONDecodeError:
        # Use regex to find content between ```json``` markers
        match = re.search(r'```json\s+([\s\S]+?)\s+```', s)
        
        if match:
            json_str = match.group(1).strip()  # Extract the JSON content
            
            # Validate and parse JSON
            try:
                data = json.loads(json_str)
                return data
            except json.JSONDecodeError:
                print("Invalid JSON format.")
                return None
        else:
            print("No JSON found between ```json``` markers.")
            return None


client = groq.Client(
    api_key="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"
)

def parse_report(report: str) -> dict:
  
    """Parse the report from the Groq query"""
    chat_complitions = client.chat.completions.create(
        messages=[{"role": "system", "content": prompts.PARSE.format(report)}],
        model="llama-3.1-70b-versatile"
    )
    try:
      return parse_json_from_string(chat_complitions.choices[0].message.content)
    except Exception:
      return None

test = """*Tesla Car Assembly Line Maintenance Report*

---

### Report Summary
*Date:* 2024-11-01  
*Prepared By:* Alex Martinez  
*Location:* Fremont, California Assembly Line

---

### 1. Overview
This report provides a comprehensive analysis of the maintenance status for the Tesla car assembly line. The following areas are examined: equipment condition, production efficiency, and potential issues impacting the assembly process.

---

### 2. Key Areas of Maintenance

#### a. *Machinery and Equipment*
- *Robotic Arms*  
  *Status:* Functional  
  *Observations:* The robotic arms are operating within standard parameters. Minor calibration adjustments were made to ensure precise component fitting. No major issues observed.

- *Conveyor System*  
  *Status:* Operational with minor wear  
  *Observations:* The conveyor belt is exhibiting minor wear and tear, especially at high-friction points near Station 3 and Station 5. Lubrication applied, and belts are scheduled for replacement on 2024-11-15.

- *Battery Installation System*  
  *Status:* Requires attention  
  *Observations:* The battery module installation system has intermittent delays, likely due to a misalignment issue detected at Station 7. Adjustments and realignments are scheduled for 2024-11-07.

#### b. *Quality Control (QC) Systems*
- *Inspection Cameras*  
  *Status:* Operational  
  *Observations:* QC cameras functioning as expected, though minor software updates are recommended to enhance defect detection sensitivity. Update to be completed by 2024-11-05.

- *Laser Alignment System*  
  *Status:* Needs Calibration  
  *Observations:* Calibration slightly off at Station 4, leading to minor discrepancies in door panel placements. Calibration scheduled for 2024-11-10.

#### c. *Safety Systems*
- *Emergency Stop Mechanisms*  
  *Status:* Fully Operational  
  *Observations:* Emergency stops were tested at each station and found functional. Regular drills for team readiness are scheduled for 2024-11-20.  

- *Fire Suppression System*  
  *Status:* Requires Testing  
  *Observations:* Inspection reveals all systems in place; testing scheduled on 2024-11-09 to ensure response times meet safety standards.

---

### 3. Maintenance Actions Taken
- *Lubrication* applied to conveyor and robotic joints at Stations 2 and 5.
- *Calibration* adjustments made on battery installation and laser alignment systems at Station 7.
- *Software Updates* for QC inspection cameras are scheduled for 2024-11-05.

---

### 4. Scheduled Maintenance

| Equipment/System                | Maintenance Date | Task                 | Priority   |
|---------------------------------|------------------|----------------------|------------|
| Battery Installation System     | 2024-11-07      | Realignment          | High       |
| Laser Alignment System          | 2024-11-10      | Calibration          | Medium     |
| Conveyor Belt                   | 2024-11-15      | Replacement          | Medium     |
| Fire Suppression System         | 2024-11-09      | Full Testing         | High       |

---

### 5. Summary of Recommendations
1. *Increase frequency of conveyor maintenance* to reduce wear and prolong the system's lifespan.
2. *Implement additional training* for maintenance staff on recent software updates for QC cameras.
3. *Conduct regular calibration checks* on laser alignment systems to prevent minor panel misalignments.

---

### 6. Conclusion
Overall, the Tesla assembly line remains fully operational with minor adjustments required. With proactive maintenance, production efficiency and safety will continue to meet Tesla's high standards.

---

*Reviewed and Approved by:*  
*Michael Johnson*  
*Operations Supervisor*  
*Signature:* _[Signature Here]_"""

# print(parse_report(test))

def sort_machine_parts(machine_data):
    # Define severity priority
    severity_order = {"Critical": 0,"High": 1, "Medium": 2, "Low": 3, "None": 4}

    # Sort the issues in each part by severity
    for part in machine_data["machine"]["parts"]:
        part["issues"].sort(key=lambda issue: severity_order.get(issue["severity"], 4))

    # Sort the parts by the highest severity issue in each part, if available
    machine_data["machine"]["parts"].sort(
        key=lambda part: severity_order.get(part["issues"][0]["severity"], 4) if part["issues"] else 4
    )

    return machine_data

# print(sort_machine_parts(parse_report(test)))