def check_patient_eligibility(age, condition, medication, rag):
    # Enterprise rules (not LLM)
    eligible = True
    reasons = []

    if age < 18:
        eligible = False
        reasons.append("Patient is under 18")

    allowed_conditions = ["diabetes", "hypertension"]
    if condition.lower() not in allowed_conditions:
        eligible = False
        reasons.append("Condition not in trial scope")

    if medication.lower() == "steroids":
        eligible = False
        reasons.append("Medication conflicts with trial protocol")

    kb_note = rag.lookup("clinical_trial_rules")

    return {
        "eligible": eligible,
        "reasons": reasons,
        "knowledge_base_reference": kb_note
    }


def generate_maintenance_schedule(hours_used, last_service_days, rag):
    actions = []

    if hours_used > 1000:
        actions.append("Perform full inspection")

    if last_service_days > 150:
        actions.append("Replace critical components")

    guideline = rag.lookup("maintenance_guidelines")

    return {
        "recommended_actions": actions,
        "next_service_in_days": 30,
        "guideline_reference": guideline
    }
