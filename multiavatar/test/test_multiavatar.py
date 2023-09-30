from pathlib import Path

from multiavatar.multiavatar import multiavatar


def html_renderer(seed):
    html = (
        "<!doctype html>"
        "<html> <head>"
        '<meta charset="utf-8">'
        '<meta http-equiv="x-ua-compatible" content="ie=edge">'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">'
        "<title>Multiavatar - All 48 Initial Avatar Designs</title>"
        "<style>body, html{width:100%; height:100%;}body{background-color: #fff; overflow-x: hidden; padding:0px; margin:0px;}*{box-sizing: border-box;}.container{width: 100%; height: 100%; padding: 20px;}.avatar{width: 110px; height:110px; float:left; margin: 10px;}</style>"
        "</head>"
        "<body>"
        '<div id="container" class="container">'
    )
    for val in range(16):
        for theme in ["A", "B", "C"]:
            avatar = multiavatar(seed, False, {"value": val, "theme": theme})
            html += '<div class="avatar">'
            html += avatar
            html += "</div>"

    html += '</div><div style="height:40px;clear:both;"></div></body></html>'
    return html


def test_initial_designs():
    """
    Will generates a results/Starcrasher.html file that can be compared manually
    with reference_sample.html
    """
    seed = "Starcrasher"
    test_directory = Path(__file__).parent
    test_result = test_directory / "results" / f"{seed}.html"
    with test_result.open(mode="w") as result:
        html = html_renderer(seed)
        result.write(html)


def test_new_hash():
    test_directory = Path(__file__).parent
    seed = "SimpleHash"
    test_result = test_directory / "results" / f"{seed}.svg"
    with test_result.open(mode="w") as result:
        avatar = multiavatar(seed, discard_env=False, sha256_randomizer=False)
        result.write(avatar)
    seed = "LegitHash"
    test_result = test_directory / "results" / f"{seed}.svg"
    with test_result.open(mode="w") as result:
        avatar = multiavatar(seed, discard_env=False, sha256_randomizer=True)
        result.write(avatar)
