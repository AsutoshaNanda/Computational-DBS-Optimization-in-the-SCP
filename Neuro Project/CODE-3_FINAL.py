pip install neuron

import numpy as np
import matplotlib.pyplot as plt

def simulate_response(current, time_points):
    """Simulate membrane potential response for a given current."""
    base_potential = -65.0
    response = base_potential + (current * 1.0) * np.exp(-(time_points - 5)**2 / 10)  # Increased scaling factor
    return response

def calculate_persistence_time(response, time_points):
    """Time membrane potential stays within ±1% of peak value."""
    peak_value = np.max(response)
    tol = 0.01 * np.abs(peak_value)
    indices_near_peak = np.where((response >= peak_value - tol) & (response <= peak_value + tol))[0]
    return time_points[indices_near_peak[-1]] - time_points[indices_near_peak[0]] if indices_near_peak.size > 0 else 0.0

def calculate_latency(response, time_points, threshold=-64.0):
    """Time from t=0 until first crossing of threshold."""
    crossings = np.where(response > threshold)[0]
    return time_points[crossings[0]] if crossings.size > 0 else None

# Main execution
if __name__ == "__main__":
    # Simulation setup
    time_points = np.linspace(0, 20, 1000)  # 0-20ms
    currents = np.linspace(0.1, 1.0, 10)     # 0.1-1.0 mA

    # Calculate metrics
    results = []
    for current in currents:
        response = simulate_response(current, time_points)
        peak = np.max(response)
        persistence = calculate_persistence_time(response, time_points)
        latency = calculate_latency(response, time_points)
        results.append({
            'current': current,
            'peak': peak,
            'persistence': persistence,
            'latency': latency if latency is not None else "No Response"
        })

    # Create visualization
    fig, (ax_plot, ax_table) = plt.subplots(1, 2, figsize=(16, 6))

    # Plot responses
    for result in results:
        response = simulate_response(result['current'], time_points)
        ax_plot.plot(time_points, response, label=f"{result['current']:.2f} mA")
    
    ax_plot.set(xlabel='Time (ms)', ylabel='Membrane Potential (mV)', 
               title='Axon Response to DBS Stimulation')
    ax_plot.grid(True)
    ax_plot.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    # Create table
    table_data = [[
        f"{res['current']:.2f}",
        f"{res['peak']:.2f}",
        f"{res['persistence']:.2f}",
        f"{res['latency']:.2f}" if isinstance(res['latency'], float) else res['latency']
    ] for res in results]

    ax_table.table(cellText=table_data,
                  colLabels=['Current (mA)', 'Peak (mV)', 'Persistence (ms)', 'Latency (ms)'],
                  loc='center')
    ax_table.axis('off')

    plt.tight_layout()
    plt.show()
