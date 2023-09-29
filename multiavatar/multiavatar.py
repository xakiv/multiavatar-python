import json
import logging
import random
import re
from hashlib import sha256
from pathlib import Path

from jinja2 import Environment, PackageLoader, select_autoescape

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class MultiAvatarBuilder:
    def __init__(self, seed, discard_env=False, sha256_randomizer=True):
        self.seed = str(seed)
        self.discard_env = discard_env
        self.sha256_randomizer = sha256_randomizer
        super().__init__()

    def avatar_rendering(self, context):
        env = Environment(
            loader=PackageLoader("multiavatar"), autoescape=select_autoescape()
        )
        template = env.get_template("avatar.svg")
        return template.render(context)

    def value_randomizer(self):
        if not self.sha256_randomizer:
            # Get a string of digits from a given seed
            random.seed(self.seed)
            number = random.randint(0, 10**12)
            hash_key = str(f"{number:012d}")
        else:
            # Create hash from a given seed and get the string of the firsts digits
            numbers = re.sub("\D", "", sha256(self.seed.encode("utf-8")).hexdigest())
            hash_key = numbers[0:12]

        return {
            "env": int(round((47 / 100) * int(hash_key[0:2]))),
            "clo": int(round((47 / 100) * int(hash_key[2:4]))),
            "head": int(round((47 / 100) * int(hash_key[4:6]))),
            "mouth": int(round((47 / 100) * int(hash_key[6:8]))),
            "eyes": int(round((47 / 100) * int(hash_key[8:10]))),
            "top": int(round((47 / 100) * int(hash_key[10:12]))),
        }

    def get_context(self):
        base_path = Path(__file__).parent
        themes_fp = Path(base_path, "data/themes.json")
        if themes_fp.exists():
            themes = json.load(themes_fp.open())

        shapes_selector = self.value_randomizer()

        if self.discard_env:
            shapes_selector.pop("env", None)

        def encode_value(part, value):
            if value > 31:
                value = value - 32
                theme = "C"
                colors = themes[value].get(theme).get(part, [])
                return {"value": value, "theme": theme, "colors": colors}

            elif value > 15:
                value = value - 16
                theme = "B"
                colors = themes[value].get(theme).get(part, [])
                return {"value": value, "theme": theme, "colors": colors}

            else:
                theme = "A"
                colors = themes[value].get(theme).get(part, [])
                return {"value": value, "theme": theme, "colors": colors}

        themed_shapes = {
            key: encode_value(key, value) for key, value in shapes_selector.items()
        }
        return themed_shapes

    def get_avatar(self):
        context = self.get_context()
        return self.avatar_rendering(context)


def multiavatar(seed, discard_env=False, sha256_randomizer=True):
    """
    Create an SVG avatar from a given seed
    seed = A string from which the SVG styles are going to be generated
    discard_env = Allows removing background
    sha256_randomizer =
    """

    builder = MultiAvatarBuilder(str(seed), discard_env, sha256_randomizer)
    avatar = builder.get_avatar()
    logger.debug(avatar)
    return avatar
