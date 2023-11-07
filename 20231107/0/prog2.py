class A: pass
class B: pass

class C(A, B): pass
class D(B, A): pass

#class G(A, C): pass
#class E(B, C): pass
class F(D, C): pass
