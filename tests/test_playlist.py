# /src/playlist.py

class _DNode:
    __slots__ = ("title", "prev", "next")
    def __init__(self, title):
        self.title = title
        self.prev = None
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_song(self, title):
        """Append song at the end."""
        node = _DNode(title)
        if not self.head:  # empty playlist
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def play_first(self):
        """Set current to head and return its title, or None if empty."""
        if not self.head:
            self.current = None
            return None
        self.current = self.head
        return self.current.title

    def next(self):
        """Move current to next if possible; return current title."""
        if not self.current:
            return None
        if self.current.next:
            self.current = self.current.next
        return self.current.title

    def prev(self):
        """Move current to prev if possible; return current title."""
        if not self.current:
            return None
        if self.current.prev:
            self.current = self.current.prev
        return self.current.title

    def insert_after_current(self, title):
        """Insert new node after current; if no current, append at end."""
        node = _DNode(title)
        if not self.current:
            # behaves like add_song
            if not self.head:
                self.head = self.tail = node
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            return

        nxt = self.current.next
        self.current.next = node
        node.prev = self.current
        node.next = nxt
        if nxt:
            nxt.prev = node
        else:
            self.tail = node  # inserted at end

    def remove_current(self):
        """Remove current song; move current to next if possible, else prev."""
        if not self.current:
            return False

        prev_node, next_node = self.current.prev, self.current.next

        # adjust head/tail
        if self.current == self.head:
            self.head = next_node
        if self.current == self.tail:
            self.tail = prev_node

        # unlink current
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node

        # move current pointer
        if next_node:
            self.current = next_node
        else:
            self.current = prev_node

        return True

    def to_list(self):
        """Return playlist as Python list from head to tail."""
        res = []
        cur = self.head
        while cur:
            res.append(cur.title)
            cur = cur.next
        return res
