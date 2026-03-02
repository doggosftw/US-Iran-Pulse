import { useRef, useEffect } from 'react';
import { ChevronLeft, ChevronRight } from 'lucide-react';
import type { PulseEvent } from '../App';

interface TimelineProps {
    events: PulseEvent[];
    activeIndex: number;
    setActiveIndex: (index: number) => void;
}

export default function Timeline({ events, activeIndex, setActiveIndex }: TimelineProps) {
    const scrollContainerRef = useRef<HTMLDivElement>(null);
    const activeItemRef = useRef<HTMLDivElement>(null);

    // Auto-scroll the active item into view when activeIndex changes
    useEffect(() => {
        if (activeItemRef.current && scrollContainerRef.current) {
            // Scroll the active item to the center of the viewport smoothly
            activeItemRef.current.scrollIntoView({
                behavior: 'smooth',
                block: 'nearest',
                inline: 'center'
            });
        }
    }, [activeIndex]);

    const goPrev = () => {
        if (activeIndex > 0) setActiveIndex(activeIndex - 1);
    };

    const goNext = () => {
        if (activeIndex < events.length - 1) setActiveIndex(activeIndex + 1);
    };

    const getCategoryColor = (cat: string) => {
        switch (cat) {
            case 'Kinetic Strike': return 'var(--accent-red)';
            case 'War': return 'var(--accent-red)';
            case 'Cyber': return 'var(--accent-blue)';
            case 'Macroeconomic': return 'var(--accent-gold)';
            case 'Diplomacy': return 'var(--accent-purple)';
            default: return '#94a3b8';
        }
    };

    return (
        <div style={{ display: 'flex', alignItems: 'center', width: '100%', gap: '12px', overflow: 'hidden' }}>

            <button
                onClick={goPrev}
                disabled={activeIndex === 0}
                style={{
                    background: 'rgba(255,255,255,0.05)', border: 'none', color: activeIndex === 0 ? '#444' : 'white',
                    padding: '8px', borderRadius: '50%', cursor: activeIndex === 0 ? 'not-allowed' : 'pointer', flexShrink: 0,
                    zIndex: 10
                }}
            >
                <ChevronLeft size={20} />
            </button>

            {/* Scrollable Container with strict bounds */}
            <div
                ref={scrollContainerRef}
                style={{ flex: 1, display: 'flex', alignItems: 'center', overflowX: 'auto', overflowY: 'hidden', padding: '40px 0', scrollbarWidth: 'none', minWidth: 0 }}
            >
                <div style={{ display: 'flex', alignItems: 'center', position: 'relative', padding: '0 24px', gap: '64px', minWidth: '100%' }}>

                    {/* Continuous Track Line */}
                    <div style={{ position: 'absolute', top: '50%', transform: 'translateY(-50%)', left: 0, right: 0, height: '2px', backgroundColor: 'rgba(255,255,255,0.1)', zIndex: 0 }} />

                    {events.map((ev, idx) => {
                        const isActive = idx === activeIndex;
                        const isPassed = idx < activeIndex;
                        const color = getCategoryColor(ev.category);
                        const dateObj = new Date(ev.date);

                        // Group dates logic
                        const prevEv = idx > 0 ? events[idx - 1] : null;
                        const prevDateObj = prevEv ? new Date(prevEv.date) : null;
                        const isSameDay = prevDateObj &&
                            dateObj.getDate() === prevDateObj.getDate() &&
                            dateObj.getMonth() === prevDateObj.getMonth();

                        return (
                            <div
                                key={ev.id}
                                ref={isActive ? activeItemRef : null}
                                onClick={() => setActiveIndex(idx)}
                                style={{
                                    position: 'relative',
                                    zIndex: 1,
                                    display: 'flex',
                                    flexDirection: 'column',
                                    alignItems: 'center',
                                    cursor: 'pointer',
                                    flexShrink: 0, // Prevent shrinking
                                    opacity: (isPassed || isActive) ? 1 : 0.4,
                                    transition: 'all 0.3s'
                                }}
                            >
                                {/* Node Dot */}
                                <div style={{
                                    width: isActive ? '16px' : '10px',
                                    height: isActive ? '16px' : '10px',
                                    borderRadius: '50%',
                                    backgroundColor: isActive ? color : (isPassed ? color : 'rgba(255,255,255,0.2)'),
                                    border: isActive ? `2px solid white` : 'none',
                                    boxShadow: isActive ? `0 0 12px ${color}` : 'none',
                                    transition: 'all 0.3s'
                                }} />

                                {/* Date Label (Show if date changes OR active) */}
                                {(!isSameDay || isActive) && (
                                    <div style={{
                                        position: 'absolute',
                                        top: '24px', // Below the dot
                                        whiteSpace: 'nowrap',
                                        fontSize: isActive ? '0.8rem' : '0.7rem',
                                        color: isActive ? 'white' : '#cbd5e1',
                                        fontWeight: isActive ? 700 : 500,
                                        background: isActive ? 'rgba(0,0,0,0.5)' : 'transparent',
                                        padding: isActive ? '2px 6px' : '0',
                                        borderRadius: '4px'
                                    }}>
                                        {dateObj.toLocaleDateString('en-US', { month: 'short', day: 'numeric' })}
                                    </div>
                                )}

                                {/* Granular Time Label (Only show when active to prevent overlap) */}
                                {isActive && (
                                    <div style={{
                                        position: 'absolute',
                                        top: '-24px', // Above the dot
                                        whiteSpace: 'nowrap',
                                        fontSize: '0.65rem',
                                        color: color,
                                        fontWeight: 700,
                                        opacity: 1
                                    }}>
                                        {dateObj.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' })}
                                    </div>
                                )}

                            </div>
                        );
                    })}
                </div>
            </div>

            <button
                onClick={goNext}
                disabled={activeIndex === events.length - 1}
                style={{
                    background: 'rgba(255,255,255,0.05)', border: 'none', color: activeIndex === events.length - 1 ? '#444' : 'white',
                    padding: '8px', borderRadius: '50%', cursor: activeIndex === events.length - 1 ? 'not-allowed' : 'pointer', flexShrink: 0
                }}
            >
                <ChevronRight size={20} />
            </button>

        </div>
    );
}
