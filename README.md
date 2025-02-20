Supply Chain Optimization App 🚚
================================

Welcome to the **Supply Chain Optimization App**, an interactive and educational tool designed to demonstrate supply chain optimization techniques. This app is built with [Streamlit](https://streamlit.io/) and [PuLP](https://coin-or.github.io/pulp/), allowing users to explore how to optimize shipping strategies in a supply chain network. Whether you're a student, developer, or supply chain enthusiast, this project provides a hands-on learning experience.

📖 Overview
-----------

The **Supply Chain Optimization App** enables users to:

*   Configure a supply chain with multiple warehouses, products, and customers.
    
*   Input demand and cost data (randomized or manually entered).
    
*   Solve an optimization problem using linear programming to minimize total shipping costs.
    
*   Visualize the optimal shipping plan and compare it to a worst-case scenario.
    

This project is perfect for **learning purposes** and **prototyping optimization models** in supply chain analytics.

🎯 Features
-----------

*   **Interactive Configuration**
    
    *   Set the number of warehouses, products, and customers.
        
    *   Customize your supply chain parameters.
        
*   **Flexible Data Input**
    
    *   Randomly generate demand and cost matrices for quick prototyping.
        
    *   Manually input data for custom scenarios.
        
*   **Optimization Modeling**
    
    *   Solve a linear programming problem using PuLP to:
        
        *   Minimize total shipping costs (optimal solution).
            
        *   Maximize costs (worst-case scenario) for comparison.
            
*   **Results Visualization**
    
    *   Display optimal shipping quantities from each warehouse.
        
    *   Calculate total shipping cost and savings percentage.
        

🛠️ Technologies Used
---------------------

*   **Programming Language:** Python
    
*   **Framework:** Streamlit
    
*   **Optimization Library:** PuLP
    
*   **Data Manipulation:** Pandas
    
*   **Visualization:** Streamlit's built-in components
    

📦 Installation Guide
---------------------

Follow these steps to set up the project locally:
git clone https://github.com/Omega-84/Supply-Chain-Optimization.git  
cd Supply-Chain-Optimization  
python -m venv env  
source env/bin/activate  
pip install -r requirements.txt  
streamlit run main.py   `

🔄 Steps to Recreate the Project
--------------------------------

If you'd like to recreate this project from scratch, follow these steps:

1\. Set Up Your Environment
---------------------------

*   Install Python (preferably version 3.7+).
    
*   Create a new directory for your project.
    

2\. Install Required Libraries
------------------------------

Install the following libraries using pip:

pip install -r requirements.txt   `

3\. Create the Main App File (app.py)
-------------------------------------

Write your main Streamlit app logic in app.py. Include:

1.  A settings page to configure warehouses, products, and customers.
    
2.  An input data page for demand and cost matrices (randomized or manual).
    
3.  A modeling page that uses PuLP for optimization.
    

4\. Add Dependencies (requirements.txt)
---------------------------------------

Generate a requirements.txt file with all dependencies:
pip freeze > requirements.txt   `

Ensure it includes:

streamlit  pulp  pandas  numpy   `

5\. Test Locally
----------------

Run your app locally using:

streamlit run main.py   `

6\. Push to GitHub
------------------

Initialize a Git repository, commit your files, and push them to GitHub:
git init  
git add .  
git commit -m "Initial commit"  
git branch -M main  
git remote add origin https://github.com/[your-username]/Supply-Chain-Optimization.git  
git push -u origin main   `

7\. Deploy on Streamlit Cloud (Optional)
----------------------------------------

Deploy your app on [Streamlit Cloud](https://share.streamlit.io/) by linking it to your GitHub repository.

📚 Learning Objectives
----------------------

This project helps you learn:

1.  The basics of linear programming and optimization using PuLP.
    
2.  How to build interactive dashboards with Streamlit.
    
3.  The fundamentals of supply chain analytics and modeling.
    
4.  Prototyping solutions for real-world optimization problems.
    

🔮 Future Enhancements
----------------------

Here are some ideas for extending this project:

1.  Add constraints like warehouse capacity or delivery time windows.
    
2.  Visualize results with charts (e.g., bar plots for shipping quantities).
    
3.  Enable exporting results (e.g., CSV or Excel files).
    
4.  Add multi-objective optimization (e.g., minimize cost while maximizing service level).
    

🤝 Contributing
---------------

Contributions are welcome! If you have ideas for improvements or spot any issues, feel free to open an issue or submit a pull request.

📜 License
----------

This project is licensed under the [MIT License](https://www.perplexity.ai/search/LICENSE).
