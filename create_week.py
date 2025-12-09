#!/usr/bin/env python3
import os
from textwrap import dedent

TEMPLATES = {
    "objectives.md": dedent("""\
        # Weekly Objectives

        Primary Goal:
        [Describe the main focus for the week]

        Secondary Goal:
        [Supporting goals or complementary exercises]

        Success Criteria:
        - [Measurable outcomes you expect to achieve]
        - [...]
        - [...]
        """),

    "tools.md": dedent("""\
        # Tools Used – Weekly Template

        List all tools, systems, and environments used during the week:

        - Operating System:
        - Packet Analysis Tools:
        - Reconnaissance Tools:
        - Virtual Machines:
        - Additional Utilities:
        """),

    "daily-log.md": dedent("""\
        # Daily Log

        ## Day 1
        Activity:
        - [...]

        Observations:
        - [...]

        Questions:
        - [...]

        ---

        ## Day 2
        Activity:
        - [...]

        Observations:
        - [...]

        Questions:
        - [...]

        ---

        ## Day 3
        Activity:
        - [...]

        Observations:
        - [...]

        Questions:
        - [...]

        (Add more days as needed)
        """),

    "findings.md": dedent("""\
        # Weekly Findings

        Summarize your notable findings for the week:

        - [...]
        - [...]
        - [...]
        """),

    "lessons-learned.md": dedent("""\
        # Weekly Lessons Learned

        Reflect on:

        - What worked well
        - What didn’t work
        - What surprised you
        - Mistakes you corrected
        - What you will improve next week
        """),
}


def main():
    week_input = input("Enter week number (e.g. 1, 2, 03): ").strip()

    try:
        week_num = int(week_input)
    except ValueError:
        print(f"Invalid week number: {week_input}")
        return

    folder_name = f"week-{week_num:02d}"
    folder_path = os.path.join(os.getcwd(), folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"[+] Created folder: {folder_name}")
    else:
        print(f"[!] Folder {folder_name} already exists")

    for filename, content in TEMPLATES.items():
        file_path = os.path.join(folder_path, filename)
        if os.path.exists(file_path):
            print(f"[!] Skipping existing file: {folder_name}/{filename}")
            continue

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[+] Created file: {folder_name}/{filename}")

    print("\nDone. Review and edit the new week's files as needed.")


if __name__ == "__main__":
    main()
