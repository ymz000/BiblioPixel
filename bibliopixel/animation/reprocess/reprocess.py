from .. import collection
from ... project import importer
from ... layout import cutter
from . import functions


class MatrixIndexer:
    cutter_class = cutter.Indexer

    def __init__(self, layout, by_row=True, function=None):
        self.layout = layout
        self.cutter = self.cutter_class(layout, by_row)
        self.function = function or functions.sorter

    def __call__(self):
        self.cutter.apply(self.function)


class Reprocess(collection.Collection):
    def __init__(self, *args, process=None, **kwds):
        super().__init__(*args, **kwds)
        self.preclear = False

        pname = '%s.%s' % (self.__module__, MatrixIndexer.__name__)

        process = process or pname
        if isinstance(process, str):
            typename = process
            process = {}
        else:
            typename = process.pop('typename', pname)

        datatype = importer.import_symbol(
            typename, 'bibliopixel.animation.reprocess')
        self.process = datatype(layout=self.layout, **process)

    def step(self, amt=1):
        anim = self.current_animation
        anim and anim.step(amt)
        self.process()