from src.main import calcular as acl
from src.main import validar as vl
from src.main import iniciar as ini

def test_login_aprovado():
    login_aprovado = ini.login("hradmin","hrtest")
    assert login_aprovado

def test_login_incorrecto():
    login_incorrecto=ini.login("hradmin22","hrtest22")
    assert not login_incorrecto

def test_comprobar_solo_numeros_aprovado():
    comprobar_aprovado=vl.comprobar(989)
    assert comprobar_aprovado

def test_comprobar_solo_numeros_incorrecto():
    comprobar_incorrecto=vl.comprobar("jj")
    assert not comprobar_incorrecto

def test_factorial():
    fact = acl.factorial(5)
    assert fact==120

def test_logaritmo():
    log = acl.logaritmo(100)
    assert log==2

def test_cubo():
    cub = acl.cubo(5)
    assert cub==125

def test_k():
    rk = acl.k(190)
    assert rk==9

