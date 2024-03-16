# This script reads the replay files and evaluates the performance.

import os
import sys
sys.path.append(os.getcwd())

from EVsSimulator.vizuals.evaluator_plot import plot_total_power, plot_comparable_EV_SoC
from EVsSimulator.vizuals.evaluator_plot import plot_total_power_V2G, plot_actual_power_vs_setpoint
from EVsSimulator.vizuals.evaluator_plot import plot_comparable_EV_SoC_single, plot_prices
from EVsSimulator.vizuals.evaluator_plot import plot_comparable_CS_Power

from EVsSimulator.baselines.gurobi_models.profit_max import V2GProfitMaxOracleGB
from EVsSimulator.baselines.gurobi_models.tracking_error import PowerTrackingErrorrMin
from sb3_contrib import TQC, TRPO, ARS, RecurrentPPO
from stable_baselines3 import PPO, A2C, DDPG, SAC, TD3
# from EVsSimulator.baselines.mpc.V2GProfitMax import V2GProfitMaxOracle, V2GProfitMaxLoadsOracle
# from EVsSimulator.baselines.mpc.eMPC import eMPC_V2G, eMPC_G2V
# from EVsSimulator.baselines.mpc.occf_mpc import OCMF_V2G, OCMF_G2V
from EVsSimulator.baselines.heuristics import ChargeAsFastAsPossibleToDesiredCapacity
from EVsSimulator.baselines.heuristics import RoundRobin, ChargeAsLateAsPossible, ChargeAsFastAsPossible
from EVsSimulator import ev_city
from EVsSimulator.utilities.arg_parser import arg_parser
import yaml
import os
import pickle
from copy import deepcopy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time



# For results table and SoC, Charger
env_path = "E:/GitHub/EVsSimulator/results/eval_30cs_1tr_V2G_MPC2_5_algos_1_exp_2024_03_14_305094/plot_results_dict.pkl"

# Total power
env_path = "E:/GitHub/EVsSimulator/results/eval_30cs_1tr_V2G_MPC2_5_algos_1_exp_2024_03_16_207848/plot_results_dict.pkl"


# env_path = "E:/GitHub/EVsSimulator/results/eval_30cs_1tr_V2G_MPC2_5_algos_1_exp_2024_03_14_995836/plot_results_dict.pkl"
save_path = "E:/GitHub/EVsSimulator/results/eval_30cs_1tr_V2G_MPC2_5_algos_1_exp_2024_03_14_995836/"

algorithms = [ChargeAsFastAsPossibleToDesiredCapacity,
              'OCMF_V2G',
              'OCMF_G2V',
              'eMPC_V2G',
              'eMPC_G2V',
              ]
algorithm_names = []
for algorithm in algorithms:
    # if class has attribute .name, use it
    if hasattr(algorithm, 'algo_name'):
        algorithm_names.append(algorithm.algo_name)
    elif type(algorithm) == str:
        algorithm_names.append(algorithm)
    else:
        algorithm_names.append(algorithm.__name__)
        
algorithm_names[0] = "As Fast As Possible"

plot_total_power_V2G(results_path=env_path,
                     save_path=save_path,
                     algorithm_names=algorithm_names)
plot_comparable_EV_SoC_single(results_path=env_path,
                              save_path=save_path,
                              algorithm_names=algorithm_names)

plot_comparable_CS_Power(results_path=env_path,
                         save_path=save_path,
                         algorithm_names=algorithm_names)
plot_prices(results_path=env_path,
            save_path=save_path,
            algorithm_names=algorithm_names)
