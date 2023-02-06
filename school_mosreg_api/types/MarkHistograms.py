from .model import Type

class markNumbers_mark(Type):
    value: str
    count: int


class markNumbers(Type):
    markNumber: int
    marks: list[markNumbers_mark]


class MarksHistogram(Type):
    """Деперсонализированная гистограма оценок всего класса"""


    markNumbers: list[markNumbers]


class WORK(Type):
    workId: int
    workId_str: str
    markNumbers: list[markNumbers]


class MarksHistogramByPeriod(Type):
    """Деперсонализированная гистограма оценок всего класса за отчетный период"""
    
    works: list[WORK]