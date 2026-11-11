import argparse
import re
import subprocess
from pathlib import Path


RELEASE_PATTERN = re.compile(r"^(furo-theme-showcase|use-guidance)-(\d+\.\d+\.\d+)$")
PAGE_BY_SECTION = {
    "furo-theme-showcase": "intro.html#furo-theme-showcase",
    "use-guidance": "use-guidance.html",
}


def get_releases() -> dict[str, list[str]]:
    tags = subprocess.run(
        ["git", "tag", "--list"], check=True, capture_output=True, text=True
    ).stdout.splitlines()
    releases = {section: [] for section in PAGE_BY_SECTION}

    for tag in tags:
        match = RELEASE_PATTERN.fullmatch(tag)
        if match:
            releases[match.group(1)].append(match.group(2))

    for versions in releases.values():
        versions.sort(key=lambda version: tuple(int(part) for part in version.split(".")))

    return releases


def write_index(output_dir: Path, releases: dict[str, list[str]]) -> None:
    links = []

    for section, versions in releases.items():
        if not versions:
            continue

        latest = versions[-1]
        page = PAGE_BY_SECTION[section]
        section_dir = output_dir / section
        section_dir.mkdir(parents=True, exist_ok=True)

        version_links = "\n".join(
            f'<li><a href="{version}/{page}">{version}</a></li>'
            for version in reversed(versions)
        )
        section_index = (
            "<!doctype html>\n"
            '<html lang="en"><head><meta charset="utf-8">'
            f'<meta http-equiv="refresh" content="0; url={latest}/{page}">'
            f"<title>{section} versions</title></head><body>"
            f"<h1>{section}</h1><p>Latest: <a href=\"{latest}/{page}\">{latest}</a></p>"
            f"<ul>{version_links}</ul></body></html>\n"
        )
        (section_dir / "index.html").write_text(section_index, encoding="utf-8")

        links.append(
            f'<li><a href="{section}/{latest}/{page}">{section} ({latest})</a>'
            f' | <a href="{section}/">all versions</a></li>'
        )

    index = (
        "<!doctype html>\n"
        '<html lang="en"><head><meta charset="utf-8">'
        "<title>Documentation versions</title></head><body>"
        "<h1>Documentation versions</h1>"
        f"<ul>{''.join(links)}</ul></body></html>\n"
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "index.html").write_text(index, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    write_index(args.output_dir, get_releases())


if __name__ == "__main__":
    main()