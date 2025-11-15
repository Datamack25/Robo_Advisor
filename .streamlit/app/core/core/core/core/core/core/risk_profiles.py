def map_profile_to_risk(profile):
    """
    Convertit le profil de risque utilisateur en volatilité cible
    """
    mapping = {
        "Conservateur": 0.10,
        "Modéré": 0.15,
        "Agressif": 0.25
    }
    return mapping.get(profile, 0.15)
