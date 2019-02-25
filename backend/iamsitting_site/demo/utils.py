import math

A_TERMINO_K = 0.45
PRETERMINO_K = 0.38
LACTANTE_K = 0.5
NIVEL_VALLE = 30.00
NIVELES_OPTIMOS = 20


def get_patient_dose(patient):

  # depuracion
  dep_a_termino = (A_TERMINO_K * patient.height) / float(patient.creatinine)
  dep_pretermino = (PRETERMINO_K * patient.height) / float(patient.creatinine)
  dep_lactante = (LACTANTE_K * patient.height) / float(patient.creatinine)

  area_sup_cord = math.sqrt((patient.weight * patient.height) / 3600.0)

  # metodo con niveles valle
  vd = patient.weight * 0.8

  # niveles plasmaticos
  c_peak = NIVEL_VALLE + (patient.dose / vd)
  ke_np = math.log(c_peak / NIVEL_VALLE) / patient.frequency
  t1_2 = 0.693 / ke_np
  ci_vanco = ke_np * vd
  d_manta = t1_2 * ci_vanco * NIVELES_OPTIMOS

  # metodo con niveles valle
  # ke_nv = ci_vanco / vd
  # t1_2_nv = 0.693 * vd / ci_vanco
  auc = (patient.dose * patient.frequency / 24) / ci_vanco
  auc_cim = auc / 0.5

  # toma de niveles
  cf_cp = NIVELES_OPTIMOS / NIVEL_VALLE
  ln_cf_cp = math.log(cf_cp) * -1
  toma_en_dias = ln_cf_cp / ke_np

  return {
    'Area de superficie': area_sup_cord,
    'Depuracion - A termino': dep_a_termino,
    'Depuracion - Pretermino': dep_pretermino,
    'Depuracion - Lactante': dep_lactante,
    'AUC / CIM': auc_cim,
    'D. Mantanimiento': d_manta,
    'Toma': toma_en_dias
  }
