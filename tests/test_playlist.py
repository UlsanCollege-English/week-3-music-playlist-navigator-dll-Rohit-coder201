from src.playlist import Playlist

def test_add_play_nav_insert_remove():
    p = Playlist()
    for t in ["A", "B", "C"]:
        p.add_song(t)
    assert p.to_list() == ["A", "B", "C"]
    assert p.play_first() == "A"
    assert p.next() == "B"
    p.insert_after_current("Bx")
    assert p.to_list() == ["A", "B", "Bx", "C"]
    assert p.next() == "Bx"
    assert p.next() == "C"
    assert p.next() == "C"   # stays at tail
    assert p.prev() == "Bx"
    assert p.remove_current() is True
    assert p.to_list() == ["A", "B", "C"]