# src/playlist.py

class _DNode:
    _slots_ = ("title", "prev", "next")
    def _init_(self, title):
        self.title = title
        self.prev = None
        self.next = None

class Playlist:
    def _init_(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_song(self, title):
        node = _DNode(title)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def play_first(self):
        self.current = self.head
        return self.current.title if self.current else None

    def next(self):
        if self.current and self.current.next:
            self.current = self.current.next
        return self.current.title if self.current else None

    def prev(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
        return self.current.title if self.current else None

    def insert_after_current(self, title):
        if not self.current:
            return  # No current song
        node = _DNode(title)
        nxt = self.current.next
        node.prev = self.current
        node.next = nxt
        self.current.next = node
        if nxt:
            nxt.prev = node
        else:
            # Inserted at tail
            self.tail = node

    def remove_current(self):
        if not self.current:
            return False
        prev_node = self.current.prev
        next_node = self.current.next

        # Update links
        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node

        if next_node:
            next_node.prev = prev_node
        else:
            self.tail = prev_node

        # Move current
        self.current = next_node if next_node else prev_node
        return True

    def to_list(self):
        result = []
        node = self.head
        while node:
            result.append(node.title)
            node = node.next
        return result