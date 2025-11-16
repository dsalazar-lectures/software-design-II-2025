from abc import ABC, abstractmethod


class Specification(ABC):
    """Interfaz base para especificaciones"""
    
    @abstractmethod
    def is_satisfied_by(self, candidate):
        pass
    
    def and_(self, other):
        return AndSpecification(self, other)
    
    def or_(self, other):
        return OrSpecification(self, other)
    
    def not_(self):
        return NotSpecification(self)


class AndSpecification(Specification):
    """Combina dos especificaciones con AND lógico"""
    
    def __init__(self, spec1: Specification, spec2: Specification):
        self.spec1 = spec1
        self.spec2 = spec2
    
    def is_satisfied_by(self, candidate):
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)


class OrSpecification(Specification):
    """Combina dos especificaciones con OR lógico"""
    
    def __init__(self, spec1: Specification, spec2: Specification):
        self.spec1 = spec1
        self.spec2 = spec2
    
    def is_satisfied_by(self, candidate):
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)


class NotSpecification(Specification):
    """Niega una especificación"""
    
    def __init__(self, spec: Specification):
        self.spec = spec
    
    def is_satisfied_by(self, candidate):
        return not self.spec.is_satisfied_by(candidate)
