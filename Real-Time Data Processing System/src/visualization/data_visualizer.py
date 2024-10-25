import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from datetime import date, datetime, timedelta
import matplotlib.dates as mdates
from collections import defaultdict
import numpy as np

class DataVisualizer:
    def __init__(self, on_closing):
        self.root = tk.Tk()
        self.root.title("Weather Monitoring App")
        self.root.protocol("WM_DELETE_WINDOW", on_closing)
        self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1, figsize=(14, 18))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(expand=True, fill=tk.BOTH)

    def plot_daily_summary(self, day: date, summary, alerts):
        self.ax1.clear()
        if not summary:
            self.ax1.text(0.5, 0.5, "No data available", ha='center', va='center')
            return

        cities = list(summary.keys())
        avg_temps = [data['temp'] for data in summary.values()]
        max_temps = [data['max_temp'] for data in summary.values()]
        min_temps = [data['min_temp'] for data in summary.values()]

        y = range(len(cities))
        height = 0.25

        self.ax1.barh([i - height for i in y], min_temps, height, label='Min Temp', color='blue', alpha=0.7)
        self.ax1.barh(y, avg_temps, height, label='Avg Temp', color='green', alpha=0.7)
        self.ax1.barh([i + height for i in y], max_temps, height, label='Max Temp', color='red', alpha=0.7)

        self.ax1.set_xlabel('Temperature (°C)')
        self.ax1.set_title(f'Daily Weather Summary - {day}')
        self.ax1.set_yticks(y)
        self.ax1.set_yticklabels(cities)
        self.ax1.legend(loc='lower right')

        for i, city in enumerate(cities):
            condition = summary[city]['dominant_condition']
            color = 'red' if city in alerts else 'black'
            self.ax1.text(max_temps[i], i + height, f"{max_temps[i]:.1f}°C", va='center', ha='left', color=color)
            self.ax1.text(avg_temps[i], i, f"{avg_temps[i]:.1f}°C", va='center', ha='left', color=color)
            self.ax1.text(min_temps[i], i - height, f"{min_temps[i]:.1f}°C", va='center', ha='left', color=color)
            self.ax1.text(max(max_temps) + 1, i, condition, va='center', ha='left', color=color)

        self.ax1.set_xlim(min(min_temps) - 5, max(max_temps) + 10)
        self.ax1.invert_yaxis()  # Invert y-axis to show cities from top to bottom

    def plot_historical_trends(self, historical_data):
        self.ax2.clear()
        if not historical_data:
            self.ax2.text(0.5, 0.5, "No historical data available", ha='center', va='center')
            return

        city_data = defaultdict(list)
        all_dates = set()
        for date_str, city, temp in historical_data:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
            if temp is not None:
                city_data[city].append((date_obj, temp))
                all_dates.add(date_obj)

        if not all_dates:
            self.ax2.text(0.5, 0.5, "No temperature data available", ha='center', va='center')
            return

        unique_dates = sorted(list(all_dates))
        colors = plt.cm.tab10(np.linspace(0, 1, len(city_data)))
        
        for (city, data), color in zip(city_data.items(), colors):
            dates, temps = zip(*sorted(data))
            self.ax2.plot(dates, temps, '-', color=color, linewidth=2, alpha=0.7)
            self.ax2.scatter(dates, temps, s=50, color=color, zorder=5, label=city)

        self.ax2.set_xlabel('Date', fontsize=12, fontweight='bold')
        self.ax2.set_ylabel('Average Temperature (°C)', fontsize=12, fontweight='bold')
        self.ax2.set_title('Historical Temperature Trends', fontsize=16, fontweight='bold')
        
        # Improve legend
        legend = self.ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10)
        for handle in legend.legendHandles:
            handle.set_sizes([50.0])

        # Improve grid
        self.ax2.grid(True, linestyle='--', alpha=0.7, which='major')
        self.ax2.set_axisbelow(True)

        # Improve x-axis
        self.ax2.set_xticks(unique_dates)
        self.ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
        plt.setp(self.ax2.xaxis.get_majorticklabels(), rotation=45, ha='right')

        # Set limits
        self.ax2.set_xlim(min(unique_dates) - timedelta(days=0.5), max(unique_dates) + timedelta(days=0.5))
        y_min, y_max = self.ax2.get_ylim()
        y_range = y_max - y_min
        self.ax2.set_ylim(y_min - 0.1*y_range, y_max + 0.1*y_range)

        # Remove spines
        for spine in self.ax2.spines.values():
            spine.set_visible(False)

        # Add temperature annotations
        for city, data in city_data.items():
            for date, temp in data:
                self.ax2.annotate(f'{temp:.1f}°C', (date, temp), 
                                  xytext=(0, 5), textcoords='offset points',
                                  ha='center', va='bottom', fontsize=8)

        self.ax2.tick_params(axis='both', which='both', length=0)

    def update(self, day, summary, historical_data, alerts):
        self.plot_daily_summary(day, summary, alerts)
        self.plot_historical_trends(historical_data)
        plt.tight_layout()
        self.canvas.draw()
        
        plt.savefig(f'weather_summary_{day}.png', dpi=300, bbox_inches='tight')
        print(f"Weather summary plot saved as weather_summary_{day}.png")

    def run(self):
        self.root.mainloop()
