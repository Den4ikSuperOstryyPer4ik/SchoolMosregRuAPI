from pydantic import BaseModel

class markNumbers_mark(BaseModel):
    value: str
    count: int


class markNumbers(BaseModel):
    markNumber: int
    marks: list[markNumbers_mark]


class MarksHistogram(BaseModel):
    """Деперсонализированная гистограма оценок всего класса"""


    markNumbers: list[markNumbers]


class WORK(BaseModel):
    workId: int
    workId_str: str
    markNumbers: list[markNumbers]


class MarksHistogramByPeriod(BaseModel):
    """Деперсонализированная гистограма оценок всего класса за отчетный период"""
    
    works: list[WORK]