"""
UC-0A — Complaint Classifier
Starter file. Build this using the RICE → agents.md → skills.md → CRAFT workflow.
"""
import argparse
import csv

severity_keywords = ["injury","child","school","hospital","ambulance","fire","hazard","fell","collapse"]

allowed_categories = [
"Pothole","Flooding","Streetlight","Waste","Noise",
"Road Damage","Heritage Damage","Heat Hazard","Drain Blockage","Other"
]

def classify_complaint(row: dict) -> dict:

    description = row.get("description","").lower()

    category = "Other"

    if "pothole" in description:
        category = "Pothole"
    elif "flood" in description or "water" in description:
        category = "Flooding"
    elif "light" in description:
        category = "Streetlight"
    elif "garbage" in description or "waste" in description:
        category = "Waste"
    elif "noise" in description:
        category = "Noise"
    elif "drain" in description:
        category = "Drain Blockage"

    priority = "Standard"

    for word in severity_keywords:
        if word in description:
            priority = "Urgent"

    reason = f'Based on complaint text containing: "{description[:40]}"'

    flag = ""
    if category == "Other":
        flag = "NEEDS_REVIEW"

    return {
        "complaint_id": row.get("complaint_id",""),
        "category": category,
        "priority": priority,
        "reason": reason,
        "flag": flag
    }


def batch_classify(input_path: str, output_path: str):

    results = []

    with open(input_path, newline="") as infile:
        reader = csv.DictReader(infile)

        for row in reader:
            try:
                result = classify_complaint(row)
                results.append(result)
            except Exception:
                results.append({
                    "complaint_id": row.get("complaint_id",""),
                    "category": "Other",
                    "priority": "Low",
                    "reason": "Row processing failed",
                    "flag": "NEEDS_REVIEW"
                })

    with open(output_path, "w", newline="") as outfile:

        fieldnames = ["complaint_id","category","priority","reason","flag"]

        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(results)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UC-0A Complaint Classifier")
    parser.add_argument("--input",  required=True, help="Path to test_[city].csv")
    parser.add_argument("--output", required=True, help="Path to write results CSV")
    args = parser.parse_args()
    batch_classify(args.input, args.output)
    print(f"Done. Results written to {args.output}")
