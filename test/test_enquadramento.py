from domain.logic import Enquadramento

def test_calcula_enquadramento():
    salario_base = 3751.05
    enquadramento = Enquadramento(salario_base)
    expectativa_base_calculo = "De 2.826,66 até 3.751,05"
    expectativa_aliquota = 15
    
    resultado_base_calculo = enquadramento.base_calculo
    resultado_aliquota = enquadramento.aliquota
    
    assert resultado_base_calculo == expectativa_base_calculo
    assert resultado_aliquota == expectativa_aliquota
