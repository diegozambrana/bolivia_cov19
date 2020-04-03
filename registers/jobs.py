from .utils import get_data
from .models import Departamento, Registro
from datetime import datetime


def read_data_from_cov19():
    data = get_data()
    date = datetime.strptime(data['fecha'], '%d/%m/%y %H:%M')
    deps = Departamento.objects.all()

    for dep in deps:
        print('---- dep.codigo:')
        print(dep)
        data_dep = data['departamento'][dep.codigo]
        print('data_dep:')
        print(data_dep)
        reg, c = Registro.objects.get_or_create(
            fecha=date,
            departamento=dep
        )
        print(c)
        # if c:
            # reg.departamento = dep
        reg.confirmados = data_dep['contador']['confirmados']
        reg.decesos = data_dep['contador']['decesos']
        reg.recuperados = data_dep['contador']['recuperados']
        reg.sospechosos = data_dep['contador']['sospechosos']
        reg.descartados = data_dep['contador']['descartados']
        reg.total = data_dep['total']
        reg.save()
        print(reg)
        print('SAVED')
