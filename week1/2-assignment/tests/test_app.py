from app import load_report


def test_load_report(tmp_path):
    report = tmp_path / "sample.txt"
    report.write_text(
        "AI assists software engineering.",
        encoding="utf-8"
    )

    text = load_report(report)

    assert text == "AI assists software engineering."

def test_generate_wordcloud_creates_png(tmp_path):
    output_path = tmp_path / "wordcloud.png"

    generate_wordcloud("AI software engineering teamwork", output_path)

    assert output_path.exists()
    assert output_path.stat().st_size > 0