#!/usr/bin/env python3
"""
Task 00: Creating a Simple Templating Program
Generates personalized invitation files from a template and a list of attendees.
"""

import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PLACEHOLDERS = ("name", "event_title", "event_date", "event_location")


def generate_invitations(template, attendees):
    """
    Generate invitation files from a template and a list of attendee dicts.
    Writes output_1.txt, output_2.txt, ... with placeholders replaced.
    """
    if not isinstance(template, str):
        logger.error(
            "Invalid input type: template must be a string, got %s.",
            type(template).__name__,
        )
        return

    if not isinstance(attendees, list):
        logger.error(
            "Invalid input type: attendees must be a list of dictionaries, got %s.",
            type(attendees).__name__,
        )
        return

    if not all(isinstance(item, dict) for item in attendees):
        logger.error(
            "Invalid input type: attendees must be a list of dictionaries."
        )
        return

    if not template.strip():
        logger.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logger.error("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for key in PLACEHOLDERS:
            value = attendee.get(key)
            if value is None or value == "":
                value = "N/A"
            else:
                value = str(value)
            content = content.replace("{" + key + "}", value)
        filename = f"output_{index}.txt"
        if os.path.exists(filename):
            logger.warning("Overwriting existing file: %s", filename)
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
        except OSError as e:
            logger.error("Failed to write %s: %s", filename, e)
