import scripts.preprocess as pp

def test_basic():
    text = '我喜欢 123 游戏!!!'
    assert pp.clean_text(text) == '喜欢 123 游戏'
