skills:
  - name: classify_complaint
    description: Classifies a single citizen complaint into category, priority, reason, and flag.
    input: A single complaint description string from the CSV file.
    output: category, priority, reason, and flag fields following the allowed schema.
    error_handling: If the complaint text is unclear or does not match any category, return category "Other" and set flag to "NEEDS_REVIEW".

  - name: batch_classify
    description: Reads a CSV file of complaints and applies classify_complaint to each row.
    input: Path to a CSV file containing complaint descriptions.
    output: A new CSV file with classification results including category, priority, reason, and flag.
    error_handling: Skip invalid rows and mark them with flag "NEEDS_REVIEW".