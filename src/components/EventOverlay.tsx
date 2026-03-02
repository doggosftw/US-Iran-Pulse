import { ExternalLink, Crosshair, AlertTriangle, FileText, ChevronRight } from 'lucide-react';
import type { PulseEvent } from '../App';

interface EventOverlayProps {
    activeEvent: PulseEvent;
}

export default function EventOverlay({ activeEvent }: EventOverlayProps) {
    if (!activeEvent) return null;

    // Determine accent color based on category
    const getCategoryColor = (cat: string) => {
        switch (cat) {
            case 'Kinetic Strike': return 'var(--accent-red)';
            case 'Cyber': return 'var(--accent-blue)';
            case 'Macroeconomic': return 'var(--accent-gold)';
            case 'Diplomacy': return 'var(--accent-purple)';
            default: return '#94a3b8';
        }
    };

    const accentColor = getCategoryColor(activeEvent.category);

    return (
        <div className="event-details animate-fade-in" key={activeEvent.id}>
            <div
                className="category-badge"
                style={{
                    display: 'inline-block',
                    padding: '4px 12px',
                    borderRadius: '20px',
                    backgroundColor: `${accentColor}22`,
                    color: accentColor,
                    border: `1px solid ${accentColor}44`,
                    fontSize: '0.75rem',
                    fontWeight: 600,
                    marginBottom: '16px',
                    textTransform: 'uppercase'
                }}
            >
                {activeEvent.category}
            </div>

            <h2 style={{ fontSize: '1.25rem', marginBottom: '12px', lineHeight: 1.4 }}>
                {activeEvent.title}
            </h2>

            <p style={{ color: '#94a3b8', fontSize: '0.9rem', lineHeight: 1.6, marginBottom: '20px' }}>
                {activeEvent.description}
            </p>

            {/* Involved Nations */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '24px' }}>
                <Crosshair size={16} color="#64748b" />
                <span style={{ fontSize: '0.85rem', color: '#cbd5e1' }}>
                    <strong>Involved:</strong> {activeEvent.involvedCountries.join(' • ')}
                </span>
            </div>

            <hr style={{ border: 'none', borderTop: '1px solid var(--glass-border)', margin: '20px 0' }} />

            {/* Impact Section */}
            {activeEvent.impact && (
                <div style={{ backgroundColor: 'rgba(239, 68, 68, 0.05)', borderLeft: '3px solid var(--accent-red)', padding: '12px', borderRadius: '4px', marginBottom: '24px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '6px' }}>
                        <AlertTriangle size={14} color="var(--accent-red)" />
                        <strong style={{ fontSize: '0.85rem', color: 'var(--accent-red)' }}>Macro Impact</strong>
                    </div>
                    <p style={{ fontSize: '0.85rem', color: '#cbd5e1' }}>{activeEvent.impact}</p>
                </div>
            )}

            {/* Sources */}
            <div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '12px' }}>
                    <FileText size={14} color="#64748b" />
                    <h3 style={{ fontSize: '0.85rem', color: '#94a3b8', textTransform: 'uppercase' }}>Verified Sources</h3>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                    {activeEvent.sources.map((s, idx) => (
                        <a
                            key={idx}
                            href={s.url}
                            target="_blank"
                            rel="noreferrer"
                            style={{
                                display: 'flex', alignItems: 'center', justifyContent: 'space-between',
                                padding: '10px 12px', backgroundColor: 'rgba(255,255,255,0.03)',
                                borderRadius: '6px', textDecoration: 'none', color: '#e2e8f0',
                                fontSize: '0.85rem', border: '1px solid rgba(255,255,255,0.05)',
                                transition: 'background 0.2s'
                            }}
                            onMouseEnter={(e) => e.currentTarget.style.backgroundColor = 'rgba(255,255,255,0.08)'}
                            onMouseLeave={(e) => e.currentTarget.style.backgroundColor = 'rgba(255,255,255,0.03)'}
                        >
                            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                <ExternalLink size={14} color="#64748b" />
                                <span>{s.name}</span>
                            </div>
                            <ChevronRight size={14} color="#64748b" />
                        </a>
                    ))}
                </div>
            </div>
        </div>
    );
}
