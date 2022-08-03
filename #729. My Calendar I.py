class MyCalendar:

    def __init__(self):
        self.l = []

    def book(self, start: int, end: int) -> bool:

        for first, last in self.l:
            if(first < end and start < last):
                return False
        self.l.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
