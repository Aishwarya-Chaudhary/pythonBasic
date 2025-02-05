class pycharm:
    def execute(self):
        print('execute on pycharm')

class myeditor:
    def execute(self):
        print('execute on myeditor')

class laptop:
    def code(self,ide):
        ide.execute()
        print('in laptop')
ide=pycharm()
c=laptop()
c.code(ide)