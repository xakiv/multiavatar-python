import logging
from collections import defaultdict
from hashlib import sha256
import re

from jinja2 import Environment, PackageLoader, select_autoescape

logger = logging.getLogger(__name__)


def main():
    env = Environment(
        loader=PackageLoader("multiavatar"), autoescape=select_autoescape()
    )
    template = env.get_template("avatar.svg")
    print(template.render({"proto": "Robo"}))


if __name__ == "__main__":
    main()
