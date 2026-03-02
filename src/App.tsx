import { useState, useEffect } from 'react';
import { Play } from 'lucide-react';
import './index.css';

import GlobeTracker from './components/GlobeTracker';
import EventOverlay from './components/EventOverlay';
import MarketPanel from './components/MarketPanel';
import Timeline from './components/Timeline';

import eventDataRaw from './data/events.json';

// We'll export these types or keep them here
interface EventCoordinate { lat: number; lng: number }
interface EventCoordinate { lat: number; lng: number }
interface EventAction { type: string; target?: string; source?: EventCoordinate; color?: string; }
export interface PulseEvent {
  id: string;
  date: string;
  title: string;
  description: string;
  category: string;
  involvedCountries: string[];
  impact: string;
  sources: { name: string; url: string; type: string }[];
  tags: string[];
  coordinates: EventCoordinate;
  action: EventAction | "none" | any; // allow any for simplicity parsing procedural gen
}

export interface MarketData {
  time: string;
  brent: number;
  gold: number;
}

const events: PulseEvent[] = eventDataRaw.events as any;
const markets: MarketData[] = eventDataRaw.markets;

function App() {
  const [activeIndex, setActiveIndex] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);

  const activeEvent = events[activeIndex];

  // Auto-play story mode
  useEffect(() => {
    let interval: any;
    if (isPlaying) {
      interval = setInterval(() => {
        setActiveIndex(prev => {
          if (prev >= events.length - 1) {
            setIsPlaying(false);
            return prev;
          }
          return prev + 1;
        });
      }, 4000); // 4 seconds per event in story mode
    }
    return () => clearInterval(interval);
  }, [isPlaying]);

  return (
    <div className="app-container">
      {/* 3D GLOBE LAYER */}
      <div className="globe-layer">
        <GlobeTracker activeEvent={activeEvent} />
      </div>

      {/* UI OVERLAY LAYER */}
      <div className="ui-layer">

        {/* CENTRAL TIME INDICATOR */}
        <div style={{
          position: 'absolute',
          top: '40px',
          left: '50%',
          transform: 'translateX(-50%)',
          pointerEvents: 'none',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          background: 'var(--glass-bg)',
          backdropFilter: 'blur(12px)',
          WebkitBackdropFilter: 'blur(12px)',
          border: '1px solid var(--glass-border)',
          padding: '12px 24px',
          borderRadius: '24px',
          zIndex: 9999,
          boxShadow: '0 8px 32px 0 rgba(0, 0, 0, 0.4)'
        }}>
          <span style={{ color: '#cbd5e1', fontSize: '1rem', fontWeight: 600, letterSpacing: '0.05em', textTransform: 'uppercase' }}>
            {new Date(activeEvent.date).toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })}
          </span>
          <span style={{ color: 'white', fontSize: '1.5rem', fontWeight: 700, letterSpacing: '0.1em' }}>
            {new Date(activeEvent.date).toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', timeZoneName: 'short' })}
          </span>
        </div>

        {/* TOP ROW */}
        <div className="top-row">
          <div className="header-title glass-panel ui-interactive">
            <h1 className="text-gradient">IRAN-US PULSE</h1>
            <p>Geopolitical & Macroeconomic Tracker</p>
          </div>
        </div>

        {/* MIDDLE ROW */}
        <div className="middle-row">
          <div className="market-panel glass-panel ui-interactive">
            <MarketPanel markets={markets} currentDateStr={activeEvent.date} />
          </div>

          <div className="event-details-panel glass-panel ui-interactive">
            <EventOverlay activeEvent={activeEvent} />
          </div>
        </div>

        {/* BOTTOM TIMELINE */}
        <div className="bottom-timeline glass-panel ui-interactive">
          <button
            onClick={() => setIsPlaying(!isPlaying)}
            style={{
              background: isPlaying ? 'rgba(255,255,255,0.1)' : 'var(--accent-red)',
              border: 'none', color: 'white', padding: '12px', borderRadius: '50%', cursor: 'pointer',
              display: 'flex', alignItems: 'center', justifyContent: 'center'
            }}
          >
            {isPlaying ? '⏸' : <Play size={20} fill="currentColor" />}
          </button>
          <div style={{ flex: 1, padding: '0 20px', color: '#888', minWidth: 0 }}>
            <Timeline events={events} activeIndex={activeIndex} setActiveIndex={setActiveIndex} />
          </div>
        </div>

      </div>
    </div>
  )
}

export default App
