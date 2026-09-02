from app import load_report, clean_text


def test_load_report(tmp_path):
    report = tmp_path / "sample.txt"
    report.write_text(
        "AI assists software engineering.",
        encoding="utf-8"
    )

    text = load_report(report)

    assert text == "AI assists software engineering."


def test_clean_text():
    text = "  HELLO  world!   This is a TEST.  "
    cleaned = clean_text(text)
    
    # Current behavior: returns text unchanged
    assert cleaned == text