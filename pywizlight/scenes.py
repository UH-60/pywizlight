"""Definition of the supported bulb effects."""
SCENES = {
    1: "Ocean",
    2: "Romance",
    3: "Sunset",
    4: "Party",
    5: "Fireplace",
    6: "Cozy",
    7: "Forest",
    8: "Pastel Colors",
    9: "Wake up",
    10: "Bedtime",
    11: "Warm White",
    12: "Daylight",
    13: "Cool white",
    14: "Night light",
    15: "Focus",
    16: "Relax",
    17: "True colors",
    18: "TV time",
    19: "Plantgrowth",
    20: "Spring",
    21: "Summer",
    22: "Fall",
    23: "Deepdive",
    24: "Jungle",
    25: "Mojito",
    26: "Club",
    27: "Christmas",
    28: "Halloween",
    29: "Candlelight",
    30: "Golden white",
    31: "Pulse",
    32: "Steampunk",
    1000: "Rhythm",
}
SCENE_NAME_TO_ID = {scene_name: scene_id for (scene_id, scene_name) in SCENES.items()}


def get_id_from_scene_name(scene: str) -> int:
    """Return the id of an given scene name.

    :param scene: Name of the scene
    :raises ValueError: Return if not in scene list
    :return: ID of the scene
    """
    scene_id = SCENE_NAME_TO_ID.get(scene)
    if not scene_id:
        raise ValueError(f"Scene '{scene}' not in scene list.")
    return scene_id
