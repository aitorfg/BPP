import pytest

def test_operaciones():
    Enero = 11523
    Febrero = 39
    Marzo = -7969
    Abril = -18933
    Mayo = 10304
    Junio = -1477
    Julio = 7698
    Agosto = -8735
    Septiembre = -10948
    Octubre = 3412
    Noviembre = 1157
    Diciembre = -3044
    Meses = Enero + Febrero + Marzo + Abril + Mayo + Junio + Julio + Agosto + Septiembre + Octubre + Noviembre + Diciembre
    Resultado = -16973
    assert Meses == Resultado

def gastos():
    Enero = -18162
    Febrero = -24398
    Marzo = -26960
    Abril = -34133
    Mayo = -17200
    Junio = -24197
    Julio = -18992
    Agosto = -29013
    Septiembre = -29151
    Octubre = -22957
    Noviembre = -24180
    Diciembre = -25861
    Meses = Enero + Febrero + Marzo + Abril + Mayo + Junio + Julio + Agosto + Septiembre + Octubre + Noviembre + Diciembre
    Resultado = -297934
    assert Meses == Resultado

def media_gastos():
    Enero = -18162
    Febrero = -24398
    Marzo = -26960
    Abril = -34133
    Mayo = -17200
    Junio = -24197
    Julio = -18992
    Agosto = -29013
    Septiembre = -29151
    Octubre = -22957
    Noviembre = -24180
    Diciembre = -25861
    Meses = Enero + Febrero + Marzo + Abril + Mayo + Junio + Julio + Agosto + Septiembre + Octubre + Noviembre + Diciembre
    num_meses = 12
    Resultado = -24827.8333
    assert Meses/num_meses == Resultado


def ingresos():
    Enero = 29685
    Febrero = 24437
    Marzo = 21721
    Abril = 15200
    Mayo = 27504
    Junio = 22720
    Julio = 26690
    Agosto = 20278
    Septiembre = 18203
    Octubre = 26369
    Noviembre = 25337
    Diciembre = 22817
    Meses = Enero + Febrero + Marzo + Abril + Mayo + Junio + Julio + Agosto + Septiembre + Octubre + Noviembre + Diciembre
    Resultado = 280961
    assert Meses == Resultado

def media_ingresos():
    Enero = 29685
    Febrero = 24437
    Marzo = 21721
    Abril = 15200
    Mayo = 27504
    Junio = 22720
    Julio = 26690
    Agosto = 20278
    Septiembre = 18203
    Octubre = 26369
    Noviembre = 25337
    Diciembre = 22817
    Meses = Enero + Febrero + Marzo + Abril + Mayo + Junio + Julio + Agosto + Septiembre + Octubre + Noviembre + Diciembre
    num_meses = 12
    Resultado = 23413.4166
    assert Meses/num_meses == Resultado