from watch import parse


def test_standard_embed():
    assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"


def test_embed_with_attributes_around():
    html = '<iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ" title="Video" frameborder="0"></iframe>'
    assert parse(html) == "https://youtu.be/dQw4w9WgXcQ"


def test_no_match():
    assert parse("<p>No video here</p>") == None


def test_wrong_domain():
    assert parse('<iframe src="https://vimeo.com/embed/12345"></iframe>') == None


def test_youtu_be_link_not_matched():
    # parse() should specifically match the /embed/ format, not youtu.be links
    assert parse('<a href="https://youtu.be/xvFZjo5PgG0">Watch</a>') == None
