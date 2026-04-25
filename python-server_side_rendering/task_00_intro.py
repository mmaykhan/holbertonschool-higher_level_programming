import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of attendees.
    """
    # Giris tipl?rini yoxlayiriq
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Bos daxiletm?l?ri yoxlayiriq
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # H?r bir istirakçi üçün d?v?tnam? yaradiriq
    for index, attendee in enumerate(attendees, start=1):
        processed_template = template
        
        # Sablondaki placeholders: name, event_title, event_date, event_location
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            
            # Placeholder ?v?zl?m?
            processed_template = processed_template.replace(f"{{{key}}}", str(value))
        
        # Çixis faylini yaradiriq
        file_name = f"output_{index}.txt"
        try:
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(processed_template)
        except Exception as e:
            print(f"Error writing to {file_name}: {e}")
