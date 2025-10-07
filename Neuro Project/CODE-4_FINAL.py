pip install neuron

import numpy as np
import matplotlib.pyplot as plt

# [Keep all your existing functions: simulate_realistic_response, 
#  calculate_peak_and_persistence, calculate_latency exactly as they are]

# Main simulation parameters
time_points = np.linspace(0, 20, 2000)
currents = np.linspace(0.1, 1.0, 10)

# Prepare data
responses = []
metrics_table_data = []

for current in currents:
    response = simulate_realistic_response(current, time_points)
    responses.append(response)
    peak_value, persistence_time = calculate_peak_and_persistence(response, time_points)
    latency = calculate_latency(response, time_points)
    
    if latency is not None:
        metrics_table_data.append([f'{current:.2f} mA', f'{peak_value:.2f} mV', 
                                 f'{persistence_time:.2f} ms', f'{latency:.2f} ms'])
    else:
        metrics_table_data.append([f'{current:.2f} mA', f'{peak_value:.2f} mV', 
                                 f'{persistence_time:.2f} ms', 'No Response'])

# Create figure with proper layout
fig = plt.figure(figsize=(18, 8))  # Increased width for better spacing
gs = fig.add_gridspec(1, 2, width_ratios=[2, 1])  # 2:1 width ratio
ax_plot = fig.add_subplot(gs[0])
ax_table = fig.add_subplot(gs[1])

# Plot responses
for current, response in zip(currents, responses):
    ax_plot.plot(time_points, response, label=f'{current:.2f} mA')
ax_plot.set(xlabel='Time (ms)', ylabel='Membrane Potential (mV)', 
          title='Axon Response to DBS Stimulation')
ax_plot.grid(True)
ax_plot.legend(bbox_to_anchor=(1.02, 1), loc='upper left')  # Moved legend outside

# Create table with proper formatting
ax_table.axis('off')
columns = ['Current (mA)', 'Peak (mV)', 'Persistence (ms)', 'Latency (ms)']
table = ax_table.table(cellText=metrics_table_data,
                      colLabels=columns,
                      loc='center',
                      cellLoc='center',
                      bbox=[0.1, 0, 0.9, 1])  # Proper bounding box

# Format table
table.auto_set_font_size(False)
table.set_fontsize(9)
for key, cell in table.get_celld().items():
    cell.set_linewidth(0.5)
    cell.set_height(0.15)  # Reduce row height

plt.subplots_adjust(wspace=0.4)  # Add horizontal spacing
plt.tight_layout()
plt.show()
