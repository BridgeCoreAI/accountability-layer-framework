import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ROOT_FILES = ["README.md", "ALF_Executive_Summary.md", "CHANGELOG.md",
              "CITATION.cff", "LICENSE"]
ASSET = ROOT / "assets" / "alf-v4-accountability-layer-diagram.png"


def read(p):
    return p.read_text(encoding="utf-8")


class TestFilesExist(unittest.TestCase):
    def test_root_files(self):
        for name in ROOT_FILES:
            self.assertTrue((ROOT / name).is_file(), f"missing {name}")

    def test_diagram_asset_exists(self):
        self.assertTrue(ASSET.is_file(), "architecture diagram asset missing")


class TestVersionConsistency(unittest.TestCase):
    """v4.0 is canonical (CITATION.cff). README, summary, CHANGELOG, and
    the diagram asset must all agree. If this fails, the version story
    drifted — fix the text, or release a new version deliberately."""

    def test_single_version_everywhere(self):
        m = re.search(r"^version:\s*([0-9]+\.[0-9]+\.[0-9]+)",
                      read(ROOT / "CITATION.cff"), re.MULTILINE)
        self.assertIsNotNone(m, "CITATION.cff has no version field")
        ver = m.group(1)
        major = ver.split(".")[0]
        for name in ("README.md", "ALF_Executive_Summary.md"):
            self.assertIn(f"v{major}.0", read(ROOT / name),
                          f"{name} missing v{major}.0")
        self.assertIn(f"[{ver}]", read(ROOT / "CHANGELOG.md"),
                      f"CHANGELOG missing [{ver}]")
        self.assertIn(f"v{major}", ASSET.name,
                      "diagram asset filename not versioned")

    def test_no_stale_v1_claims(self):
        for name in ("README.md", "ALF_Executive_Summary.md"):
            text = read(ROOT / name)
            self.assertNotIn("Current Version:** v1", text,
                             f"{name} claims v1.0 as current")


class TestClaimsAreCalibrated(unittest.TestCase):
    def test_access_gate_is_stated(self):
        self.assertIn("available upon request",
                      read(ROOT / "ALF_Executive_Summary.md"))

    def test_no_retired_utility(self):
        self.assertFalse((ROOT / "fix_alf_readme.py").exists(),
                         "one-shot cleanup utility returned; retire it again")


class TestLicense(unittest.TestCase):
     def test_mit_license(self):
        self.assertIn("MIT License", read(ROOT / "LICENSE"))
        self.assertIn("license: MIT", read(ROOT / "CITATION.cff"))


class TestNoPlaceholders(unittest.TestCase):
    def test_no_todos(self):
        for p in ROOT.glob("*.md"):
            text = read(p)
            for marker in ("TODO", "TBD", "FIXME"):
                self.assertNotIn(marker, text,
                                 f"{p.name}: unfinished marker '{marker}'")


class TestLinks(unittest.TestCase):
    LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

    def test_internal_links_resolve(self):
        for p in ROOT.rglob("*.md"):
            if ".git" in p.parts:
                continue
            for raw in self.LINK_RE.findall(read(p)):
                if "://" in raw or raw.startswith(("#", "mailto:")):
                    continue
                target = raw.split("#")[0].strip()
                if target:
                    self.assertTrue((p.parent / target).resolve().exists(),
                                    f"{p.name}: broken link -> {raw}")
