# Iran-US Pulse 🌍

A high-fidelity, interactive 3D geopolitical and macroeconomic tracking dashboard. This project visualizes a hypothetical timeline of escalating tensions and conflict between Iran and the United States from January 1, 2026, to March 1, 2026.

## 🎯 Key Features

- **3D Globe Visualizations**: Utilizes `react-globe.gl` and `three.js` to map complex, multi-category events (Diplomacy, Kinetic Strikes, Cyber, War, Macroeconomics) to a 3D globe. Includes advanced WebGL layers for missile arcs, impact ripples, and glowing cyberattack nodes.
- **Glassmorphism UI**: A premium, dark-themed dashboard styled with blurred glass panels and a robust responsive layout.
- **Interactive Timeline**: A custom horizontal timeline for scrubbing and navigating through a dense sequence of geopolitical events spanning 60 days.
- **Macroeconomic Tracking**: Integrates daily closing prices for Brent Crude and Gold, correlated to specific geopolitical events and displayed using `recharts`.
- **Procedural Data Pipeline**: Includes a Python-based data generation script (`generate_data_v2.py`) to procedurally generate a logically progressing narrative with dense event metadata and precise geographic coordinates.

## 🛠️ Tech Stack

- **Frontend Framework**: React 19, TypeScript, Vite
- **3D Visualization**: `react-globe.gl`, `three.js`
- **Charting**: `recharts`
- **Icons**: `lucide-react`
- **Data Generation**: Python

## 🚀 Getting Started

### Prerequisites
- Node.js (v18 or higher recommended)
- npm or yarn

### Installation

1. Clone the repository (if applicable) and navigate to the project directory:
```bash
cd iranUSpulse
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Build for production:
```bash
npm run build
```

## 📈 Data Pipeline

The project includes a procedural data generation pipeline. A python script (`generate_data_v2.py`) is responsible for generating the timeline of events, including precise coordinates, event types, and impact severity. Real-world market data for Brent Crude and Gold is also mapped to the timeline to simulate economic impact. The pipeline is a one time data extraction to prepare a static historical dataset.

## 🤝 Contributing

Contributions are NOT welcome! This is a vibe coded side project. Please feel free to fork or clone if you want to build on top of it.
