class Asker:
    @staticmethod
    def askall(lst):
        for i in lst:
            Sender.report()

class Sender:
    fl = True

    @classmethod
    def report(self):
        print("Greetings" if self.fl else "Get away!")
        self.fl = False

Asker.askall([Sender, Sender, Sender])
Asker.askall([Sender, Sender, Sender])

