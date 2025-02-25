# Portfolio Analysis and Optimization Project

This project is aimed at preparing and analyzing a low-risk, moderate return portfolio. The system supports the sourcing, analysis, and visualization of stock data along with an optimization workflow. The project involved creating a diversified investment portfolio combining fixed income assets and growth stocks, aimed at maximizing returns while minimizing risks. The project utilized machine learning and statistics for risk optimization and maximizing equity returns.

## Key Highlights
Portfolio Composition:
 - 40% in Growth Stocks and ETFs: Focused on sectors with high growth potential, including technology, sustainability, and pharmaceuticals.
 - 60% in Fixed Income Assets: Invested in US Treasury Bonds and Hong Kong Green Bonds to ensure stability and predictable returns.

Risk Management:
 - Employed hedging strategies, such as collar positions, to mitigate risks associated with market volatility.
 - Conducted correlation analysis to ensure the diversification of assets, minimizing the risk of simultaneous losses.

Performance Optimization:
 - Used 20,000 Monte-Carlo simulations to find the risk and return profiles of the configurations. 
 - Utilized Markowitz optimization to determine the optimal weightings for securities, achieving an expected annual return of 18.3% with an 11.5% volatility.

Benchmark Comparison:
 - The portfolio consistently outperformed the S&P 500 over time, demonstrating superior returns with lower volatility.
 - The portfolio projected roughly 60% higher returns than the S&P500 with a 70% probability of outperforming the S&P500 in 10 years.

## Project Structure
- **src/**: Contains the analysis script (`analyze.py`) that:
    - Sources data from the Yahoo yfinance API.
    - Generates analysis plots including:
        - Trend analysis and seasonal decomposition.
        - Differencing of prices (i.e., returns) and corresponding partial autocorrelation.
        - Auto correlation and partial autocorrelation for stock prices.
- **src/data/**: Stores the sourced data for each ticker.
- **src/plots/**: Holds the generated analysis plots.
- **src/requirements.txt**: Lists all the Python package dependencies.
- **src/tickers.txt**: Contains user-provided tickers to parse, source, and create data.
- **optimization/optim.ipynb**: Contains the notebook for portfolio optimization:
    - Implements Markowitz optimization.
    - Performs Monte Carlo simulations for benchmarking equity performance against the S&P500.
    - Includes methodologies for dollar cost averaging, projecting returns, and estimating the probability of outperformance.

## Getting Started
1. **Clone the Repository**  
      ```
   git clone <repository-url>
   ```

2. **Install Dependencies**  
   Run the following command to install required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Setup Ticker Symbols**  
   Edit `tickers.txt` to include your target ticker symbols (e.g., AAPL, GOOG4 MSFT).
     
4. Running the Analysis
    Execute the analysis script from the project root:
     ```
    python src/analyze.py
     ```

5. Portfolio Optimization

    Explore the notebook in the `optimization/` directory to:
    - Test different portfolio allocation strategies.
    - Compare portfolio performance against benchmark indices.
    - Utilize Monte Carlo methods for risk simulation.

## Presentation Materials

For an overview of the project and detailed explanations, refer to:
- [Project Presentation (PDF)](./GE2260G7.pdf)
- [Project Video Explanation](https://drive.google.com/file/d/1B-Y17R-3CZmWDVcAB368evj0cL1ToSFe/view?usp=sharing)
