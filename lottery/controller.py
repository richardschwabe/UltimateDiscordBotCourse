from .model import LotteryDrawing


class LotteryController:

    def save(self, numbers, author=None):
        drawing = LotteryDrawing()
        drawing.numbers = numbers

        if author is not None:
            drawing.members_id = author.id
        else:
            drawing.dtype = LotteryDrawing.TYPE_SYSTEM

        drawing.save()

    def get_drawing_results(self):
        previous_drawing = LotteryDrawing.objects.filter(
            dtype=LotteryDrawing.TYPE_SYSTEM).order_by("-created_at")[:2][1]

        all_tickets = LotteryDrawing.objects.filter(
            created_at__gt=previous_drawing.created_at, dtype=LotteryDrawing.TYPE_USER)

        results = {
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 0,
            '6': 0,
        }

        for t in all_tickets:
            matching_numbers = set(t.numbers).intersection(
                self.get_last_drawing().numbers)
            matches = len(matching_numbers)
            if matches == 2:
                results['2'] += 1
            elif matches == 3:
                results['3'] += 1
            elif matches == 4:
                results['4'] += 1
            elif matches == 5:
                results['5'] += 1
            elif matches == 6:
                results['6'] += 1

        return results

    def get_my_drawings(self, author):
        drawings = LotteryDrawing.objects.filter(members_id=author.id)
        return drawings

    def get_last_drawing(self):
        last_drawing = LotteryDrawing.objects.filter(
            dtype=LotteryDrawing.TYPE_SYSTEM).order_by("-created_at").first()
        return last_drawing

    def draw_numbers(self):
        drawing = LotteryDrawing()
        numbers = drawing.draw_numbers()
        return numbers
