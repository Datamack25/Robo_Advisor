# core/risk_profiles.py
def map_profile_to_risk(profile):
    mapping = {
        "Conservateur": 0.08,
        "Modéré": 0.15,
        "Agressif": 0.25
    }
    return mapping.get(profile, 0.15)

