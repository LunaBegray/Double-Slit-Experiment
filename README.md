# **Quantum Wave Explorer**  
_An Interactive Double-Slit Experiment Simulator with Heatmap Visualizations_  

## **Overview**  
**Quantum Wave Explorer** is an interactive physics simulator that brings the famous **Double-Slit Experiment** to life. With this program, you can explore the duality of quantum particles behaving as **waves** or **particles**, depending on the presence of a detector. The experiment is visualized through an intuitive **heatmap display**, making the mysterious world of quantum mechanics accessible and engaging.

---

## **Features**  
1. **Real-Time Simulation**:
   - Observe particles traveling through the double slits and impacting a detection screen.
   - Watch how the presence or absence of a detector influences their behavior.
   
2. **Wave-Particle Duality**:
   - **Detector ON**: See particles form clusters behind the slits, mimicking classical behavior.
   - **Detector OFF**: Watch a beautiful **wave interference pattern** emerge on a broad detection screen.

3. **Heatmap Visualization**:
   - Particle impacts are visualized as a dynamic **heatmap**, showing regions of high and low impact density.

4. **Interactive Controls**:
   - Toggle the quantum **detector** with a single keypress to explore the wave-particle duality in real time.

5. **Enhanced Physics Simulation**:
   - Implements probabilistic wave interference based on phase differences.
   - A Gaussian spread ensures realistic, broad wave behavior.

---

## **How to Use**  
### **Setup**  
1. Ensure **Python 3.10+** and **Pygame** are installed on your system.
   - Install Pygame using:  
     ```
     pip install pygame
     ```

2. Download and run the script:
   ```
   python quantum_wave_explorer.py
   ```

### **Interactive Controls**  
- **`D` Key**: Toggle the detector ON or OFF.
  - Detector ON: Simulates particle behavior (no interference pattern).
  - Detector OFF: Simulates wave-like behavior with interference.  
- **Escape or Close Button**: Exit the program.

---

## **Screenshots**  
### 1. **Detector ON**  
Clusters of particle impacts appear directly behind each slit, demonstrating particle-like behavior.

### 2. **Detector OFF**  
A broad wave interference pattern emerges, visualized as bright and dark regions on the detection canvas.

---

## **Technical Details**  
1. **Physics Simulation**:
   - Particles are simulated with probabilistic trajectories and adjusted using wave interference calculations.
   - A **cosine function** models the interference pattern based on phase differences.

2. **Heatmap Implementation**:
   - The screen is divided into a grid of cells. Each particle's impact updates the heatmap in real time.
   - The heatmap visualizes high-density areas in **red** and low-density areas in **dark red**.

3. **Slits and Detector**:
   - Two slits with adjustable positions simulate a real double-slit setup.
   - The detector enforces "which-path" knowledge, removing wave interference when active.

---

## **Inspirations**  
This program is inspired by the famous **Quantum Double-Slit Experiment**, which revealed the wave-particle duality of quantum particles. It’s designed for educational purposes, sparking curiosity about quantum mechanics and visualization techniques.

---

## **Planned Future Enhancements**  
- Adjustable **slit width**, **separation**, and **wavelength**.
- A **settings menu** for customizing simulation parameters.
- Advanced visualizations like **3D interference patterns**.
- Real-time tracking of individual particle paths.
