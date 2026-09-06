from app import load_report, clean_text, generate_wordcloud


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


def test_generate_wordcloud(tmp_path):
    """Test that generate_wordcloud creates an output file."""
    input_text = "software engineering testing wordcloud"
    output_file = tmp_path / "test_wordcloud.png"
    
    generate_wordcloud(input_text, output_file)
    
    # Verify the file was created
    assert output_file.exists()
    # Verify it's not empty
    assert output_file.stat().st_size > 0