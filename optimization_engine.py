from scipy.optimize import minimize
import numpy as np

class StructureOptimizer:
    def __init__(self, initial_params):
        self.current_params = initial_params
        self.best_result = float('inf')
        
    def objective_function(self, params):
        """最適化目的関数"""
        thickness, damping, preload = params
        
        # ANSYSモデルの更新と解析実行
        response = self.run_analysis(thickness, damping, preload)
        
        # 評価基準の計算
        acceleration_penalty = np.max(response['accelerations'])
        mass_penalty = self.calculate_mass(thickness)
        stress_penalty = np.max(response['stresses'])
        
        return (acceleration_penalty * 0.5 + 
                mass_penalty * 0.3 + 
                stress_penalty * 0.2)
    
    def optimize(self):
        """最適化実行"""
        constraints = [
            {'type': 'ineq', 'fun': lambda x: 5.0 - x[0]},  # max thickness
            {'type': 'ineq', 'fun': lambda x: x[0] - 1.0},  # min thickness
            {'type': 'ineq', 'fun': lambda x: 2000 - x[2]}, # max preload
        ]
        
        result = minimize(
            self.objective_function,
            self.current_params,
            method='SLSQP',
            constraints=constraints,
            bounds=((1.0, 5.0), (0.01, 0.05), (500, 2000))
        )
        
        return result.x, result.fun 