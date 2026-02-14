def score_job(description):

    rigging_keywords = ["rigging", "lifting", "crane", "mooring", "riser"]
    rope_keywords = ["rope access", "IRATA", "inspection"]
    bolting_keywords = ["hydraulic bolting", "torque", "tension", "flange"]

    score = 0
    category = "General"

    for word in rigging_keywords:
        if word.lower() in description.lower():
            score += 10
            category = "Rigging"

    for word in rope_keywords:
        if word.lower() in description.lower():
            score += 10
            category = "Rope Access"

    for word in bolting_keywords:
        if word.lower() in description.lower():
            score += 10
            category = "Bolting"

    return score, category