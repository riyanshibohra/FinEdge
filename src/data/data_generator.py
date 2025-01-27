import numpy as np
import pandas as pd
from datetime import datetime, timedelta

class FinancialDataGenerator:
    """Generate synthetic financial data for testing and development"""
    
    def __init__(self, start_date='2022-01-01', periods=365):
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.periods = periods
        
    def generate_revenue_data(self):
        """Generate daily revenue data with seasonal patterns"""
        dates = [self.start_date + timedelta(days=x) for x in range(self.periods)]
        
        # Base revenue with trend
        base_revenue = np.linspace(10000, 15000, self.periods)
        
        # Add seasonality
        seasonality = np.sin(np.linspace(0, 4*np.pi, self.periods)) * 2000
        
        # Add random noise
        noise = np.random.normal(0, 500, self.periods)
        
        revenue = base_revenue + seasonality + noise
        
        return pd.DataFrame({
            'date': dates,
            'revenue': revenue,
            'region': np.random.choice(['North', 'South', 'East', 'West'], size=self.periods),
            'product_line': np.random.choice(['Product A', 'Product B', 'Product C'], size=self.periods)
        })
    
    def generate_cost_data(self):
        """Generate daily cost data"""
        dates = [self.start_date + timedelta(days=x) for x in range(self.periods)]
        
        # Base costs (correlated with revenue but lower)
        base_costs = np.linspace(7000, 10000, self.periods)
        
        # Add random variations
        noise = np.random.normal(0, 300, self.periods)
        
        costs = base_costs + noise
        
        return pd.DataFrame({
            'date': dates,
            'cost_category': np.random.choice([
                'Raw Materials', 'Labor', 'Operations', 
                'Marketing', 'Administrative'
            ], size=self.periods),
            'amount': costs
        })

if __name__ == "__main__":
    # Test data generation
    generator = FinancialDataGenerator()
    revenue_df = generator.generate_revenue_data()
    cost_df = generator.generate_cost_data()
    
    print("Revenue Data Sample:")
    print(revenue_df.head())
    print("\nCost Data Sample:")
    print(cost_df.head()) 