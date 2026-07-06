import json
from pathlib import Path

REPORT = Path("/app/report.json")

EXPECTED = {
    "total_requests": 6,
    "unique_ips": 3,
    "top_path": "/index.html",
}


def load_report():
    assert REPORT.exists(), "Expected /app/report.json to exist"
    with REPORT.open() as f:
        return json.load(f)


def test_report_is_valid_json_object():
    """The report must be a valid JSON object."""
    report = load_report()
    assert isinstance(report, dict), "report.json must contain a JSON object"


def test_report_has_exact_required_fields():
    """The report must contain exactly the requested fields and no extras."""
    report = load_report()
    assert set(report.keys()) == set(EXPECTED.keys())


def test_total_requests_matches_access_log():
    """The report must contain the correct number of non-empty log lines."""
    report = load_report()
    assert report["total_requests"] == EXPECTED["total_requests"]


def test_unique_ips_matches_access_log():
    """The report must contain the correct number of distinct client IPs."""
    report = load_report()
    assert report["unique_ips"] == EXPECTED["unique_ips"]


def test_top_path_matches_access_log():
    """The report must identify the most frequently requested path."""
    report = load_report()
    assert report["top_path"] == EXPECTED["top_path"]
