import numpy as np
import pandas as pd
from datetime import datetime, timedelta

class FinancialDataGenerator:
    """Generate synthetic financial data for testing and development"""
    
    def __init__(self, start_date='2022-01-01', periods=365):
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.periods = periods
        
        # Define constant parameters
        self.regions = ['North', 'South', 'East', 'West']
        self.product_lines = {
            'Product A': {'base_price': 100, 'base_cost': 60},
            'Product B': {'base_price': 150, 'base_cost': 85},
            'Product C': {'base_price': 200, 'base_cost': 120}
        }
        self.customer_segments = ['Enterprise', 'SMB', 'Consumer']
        self.cost_categories = {
            'Raw Materials': {'base_percent': 0.4, 'volatility': 0.1},
            'Labor': {'base_percent': 0.25, 'volatility': 0.05},
            'Operations': {'base_percent': 0.15, 'volatility': 0.07},
            'Marketing': {'base_percent': 0.12, 'volatility': 0.15},
            'Administrative': {'base_percent': 0.08, 'volatility': 0.03}
        }

    def add_market_factors(self):
        """Generate market condition factors"""
        # Market growth trend
        trend = np.linspace(1, 1.2, self.periods)
        
        # Seasonal factors (stronger in summer, weaker in winter)
        seasonal = 1 + 0.2 * np.sin(np.linspace(0, 2*np.pi, self.periods))
        
        # Market volatility
        volatility = np.random.normal(1, 0.05, self.periods)
        
        return trend * seasonal * volatility

    def generate_revenue_data(self):
        """Generate daily revenue data with seasonal patterns and customer segments"""
        dates = [self.start_date + timedelta(days=x) for x in range(self.periods)]
        market_factors = self.add_market_factors()
        
        data = []
        for day in range(self.periods):
            # Generate multiple transactions per day
            daily_transactions = np.random.poisson(20)  # Average 20 transactions per day
            
            for _ in range(daily_transactions):
                product = np.random.choice(list(self.product_lines.keys()))
                region = np.random.choice(self.regions)
                segment = np.random.choice(self.customer_segments)
                
                # Base price with market factor adjustment
                base_price = self.product_lines[product]['base_price']
                
                # Add segment-specific pricing
                segment_multiplier = 1.2 if segment == 'Enterprise' else 1.1 if segment == 'SMB' else 1.0
                
                # Calculate final price with market factors
                price = base_price * segment_multiplier * market_factors[day]
                
                # Add some random variation
                price *= np.random.normal(1, 0.05)
                
                data.append({
                    'date': dates[day],
                    'product_line': product,
                    'region': region,
                    'customer_segment': segment,
                    'revenue': price,
                    'units_sold': np.random.randint(1, 10)
                })
        
        return pd.DataFrame(data)

    def generate_cost_data(self):
        """Generate daily cost data with realistic cost structures"""
        dates = [self.start_date + timedelta(days=x) for x in range(self.periods)]
        market_factors = self.add_market_factors()
        
        data = []
        for day in range(self.periods):
            daily_base_cost = 5000 * market_factors[day]  # Base daily operational cost
            
            for category, params in self.cost_categories.items():
                # Calculate cost with base percentage and add volatility
                category_cost = (daily_base_cost * params['base_percent'] * 
                               np.random.normal(1, params['volatility']))
                
                # Add seasonal and trend effects
                if category == 'Raw Materials':
                    # Raw materials more expensive in winter
                    seasonal_factor = 1 + 0.15 * np.cos(2 * np.pi * day / 365)
                    category_cost *= seasonal_factor
                
                data.append({
                    'date': dates[day],
                    'cost_category': category,
                    'amount': category_cost,
                    'market_factor': market_factors[day]
                })
        
        return pd.DataFrame(data)

    def generate_metrics(self):
        """Generate key business metrics"""
        revenue_df = self.generate_revenue_data()
        cost_df = self.generate_cost_data()
        
        # Aggregate by date
        daily_revenue = revenue_df.groupby('date')['revenue'].sum().reset_index()
        daily_costs = cost_df.groupby('date')['amount'].sum().reset_index()
        
        # Calculate metrics
        metrics = pd.merge(daily_revenue, daily_costs, on='date', suffixes=('_revenue', '_costs'))
        metrics['gross_profit'] = metrics['revenue'] - metrics['amount']
        metrics['profit_margin'] = (metrics['gross_profit'] / metrics['revenue']) * 100
        
        return metrics

if __name__ == "__main__":
    # Test data generation
    generator = FinancialDataGenerator()
    
    # Generate and display sample data
    revenue_df = generator.generate_revenue_data()
    cost_df = generator.generate_cost_data()
    metrics_df = generator.generate_metrics()
    
    print("\nRevenue Data Sample:")
    print(revenue_df.head())
    print("\nCost Data Sample:")
    print(cost_df.head())
    print("\nMetrics Sample:")
    print(metrics_df.head()) 