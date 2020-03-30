import unittest
from PowerFlow import PowerFlow
import pandas as pd

path_of_system = 'test/syste_test_IEEE13bus/IEEE13Nodeckt.dss'
value_of_kV = [115, 4.16, .48]
value_of_load_mult = 1

bus_names = ['sourcebus',	'650',	'rg60',	'633', '634', '671', '645', '646', '692', '675', '611', '652', '670', '632', '680',	'684']


distSys = PowerFlow(path = path_of_system, kV = value_of_kV, loadmult = value_of_load_mult)
distSys.run_power_flow()

class Verifica_meth_gets(unittest.TestCase):

    def test_get_path(self):
        self.assertTrue(distSys.get_path() == path_of_system)

    def test_get_kV(self):
        self.assertTrue(distSys.get_kV() == value_of_kV)

    def test_get_loadmult(self):
        self.assertTrue(distSys.get_loadmult() == value_of_load_mult)

    def test_get_all_bus_names(self):
        self.assertTrue(bus_names == distSys.get_all_bus_names())
    
    def test_get_erros(self):
        self.assertTrue('' == distSys.get_erros())

    def test_get_bus_v_pu_ang_pandas(self):
        data = {
            'bus_names': ['684'],
            'v_pu_a':[ 0.98087],
            'v_pu_b': [None],
            'v_pu_c': [0.96284],
            'ang_a': [-5.4],
            'ang_b': [None],
            'ang_c': [115.9],
            'phases': ['ac']
        }
        

        esperado = pd.DataFrame.from_dict(data)
        resultado = distSys.get_bus_v_pu_ang_pandas(['684'])


        self.assertTrue(all(esperado == resultado))

    def test_get_all_v_pu_ang_pandas(self):
        df_all_bus = distSys.get_all_v_pu_angle_pandas()
        df_buses_all = distSys.get_bus_v_pu_ang_pandas(bus_names)
        self.assertTrue(all(df_all_bus == df_buses_all))
