import logging

# Logging konfiqurasiyası
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def generate_invitations(template, attendees):
    """
    Template və attendees siyahısından fərdi dəvət faylları yaradır.

    :param template: str - placeholder-ləri olan şablon mətn
    :param attendees: list of dict - hər qonaq üçün məlumat
    """

    # 1. Tip yoxlaması
    if not isinstance(template, str):
        logging.error("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error("Invalid input: attendees must be a list of dictionaries.")
        return

    # 2. Boş input yoxlaması
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    # 3. Hər qonaq üçün fayl yarat
    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        output = template

        for key in placeholders:
            value = attendee.get(key)

            # Dəyər None və ya yoxdursa "N/A" istifadə et
            if value is None:
                value = "N/A"

            output = output.replace("{" + key + "}", str(value))

        # Faylı yaz
        filename = f"output_{index}.txt"
        with open(filename, 'w') as f:
            f.write(output)

        logging.info(f"Generated: {filename} for {attendee.get('name', 'N/A')}")
